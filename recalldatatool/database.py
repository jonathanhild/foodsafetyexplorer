# Copyright (c) 2020 Jonathan Hildenbrand
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import os

import sqlalchemy as db
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker

from .mappings import Base


def pgsql_env_file(env_path=None):
    """
    Load environmental variables with PostgreSQL credentials from .pgsqlenv file.

    Args:
        env_path (string, optional): Filepath to the environment variables file. Defaults to None.
    """
    if not env_path:
        env_path = os.path.join('./', '.pgsqlenv')
    load_dotenv(dotenv_path=env_path)


def pgsql_get_vars():
    username = os.getenv('PGSQL_USERNAME')
    password = os.getenv('PGSQL_PASSWORD')
    return username, password


def pgsql_conn_str(username, password):
    pgsql_url = f'postgresql+psycopg2://{username}:{password}@localhost:5432/recalls'
    return pgsql_url


def sqlite_conn_str(filepath=None):
    if not os.path.exists('./data'):
        os.mkdir('./data')
    if not filepath:
        filepath = os.path.join('data', 'recalls.sqlite')
    sqlite_url = f'sqlite:///{filepath}'
    return sqlite_url


def create_session(engine_url, create_all=False):
    """
    Create a PostgreSQL database session.

    Args:
        engine_url (str, optional): A URL database connection string.

    Returns:
        Session: A SQLAlchemy session instance.
    """
    engine = db.create_engine(engine_url)

    if create_all:
        Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    return Session()


if __name__ == '__main__':
    pgsql_env_file()
    username, password = pgsql_get_vars()
    pgsql_conn = pgsql_conn_str(username, password)
    session = create_session(pgsql_conn, create_all=True)
    sqlite_conn = sqlite_conn_str()
    session = create_session(sqlite_conn, create_all=True)
