# Copyright (c) 2020 Jonathan Hildenbrand
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from fdadatatool import factory, db_session

recalls = factory.create('RECALLS')
recalls.get_data()
recalls.to_csv()

session = db_session()

recalls.to_db(session)
