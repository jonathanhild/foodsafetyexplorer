# Copyright (c) 2020 Jonathan Hildenbrand
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import os

import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from .mappings import Base

username = None
password = None

db_path = os.path.join('.', 'data', 'fdadata.sqlite')
sqlite_uri = f'sqlite:///{db_path}'
pgsql_uri = f'postgresql+psycopg2://{username}:{password}@localhost/recalls'


def db(engine_uri, create=False):
    """
    Create  PostgreSQL or SQLite database instance.

    Args:
        engine_uri (str, optional): A URL database connection string.

    Returns:
        Engine: A SQLAlchemy
    """

    engine = db.create_engine(engine_uri)

    if create:
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        return Session()
    else:
        Session = sessionmaker(bind=engine)
        return Session()
