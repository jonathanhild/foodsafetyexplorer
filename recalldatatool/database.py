# Copyright (c) 2020 Jonathan Hildenbrand
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import os

import sqlalchemy as db
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker

from .mappings import Base


def _pgsql_env_file(pgsql_env_file=None):
    """
    Load environmental variables with PostgreSQL credentials from .pgsqlenv file.

    Args:
        env_path (string, optional): Filepath to the environment variables file. Defaults to None.
    """
    if not pgsql_env_file:
        pgsql_env_file = os.path.join('./', '.pgsqlenv')
    load_dotenv(dotenv_path=pgsql_env_file)


def _pgsql_get_vars():
    username = os.getenv('PGSQL_USERNAME')
    password = os.getenv('PGSQL_PASSWORD')
    return username, password


def _pgsql_conn(username, password):
    pgsql_url = f'postgresql+psycopg2://{username}:{password}@localhost:5432/recalls'
    engine = db.create_engine(pgsql_url)
    return engine


def _sqlite_conn(dbpath=None):
    if not os.path.exists('./data'):
        os.mkdir('./data')
    if not dbpath:
        dbpath = os.path.join('data', 'recalls.sqlite')
    sqlite_url = f'sqlite:///{dbpath}'
    engine = db.create_engine(sqlite_url)
    return engine


def create_session(database='sqlite', path=None):
    if database == 'pgsql':
        _pgsql_env_file(pgsql_env_file=path)
        username, password = _pgsql_get_vars()
        engine = _pgsql_conn(username=username, password=password)
    if database == 'sqlite':
        engine = _sqlite_conn(dbpath=path)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    return Session()
