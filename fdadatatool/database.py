# Copyright (c) 2020 Jonathan Hildenbrand
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import os

import sqlalchemy as db
from sqlalchemy.orm import sessionmaker

from .mappings import Base

db_path = os.path.join('.', 'data', 'fdadata.sqlite')
engine = db.create_engine(f'sqlite:///{db_path}')


def db_session():
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()


if __name__ == '__main__':
    db_session()
