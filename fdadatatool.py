# Copyright (c) 2020 Jonathan Hildenbrand
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from fdadatatool import factory, db_session

citations = factory.create(
    'CITATIONS', filename='./data/excel_files/citations.xlsx')
citations.get_data()
citations.to_csv()

recalls = factory.create('RECALLS')
recalls.get_data()
recalls.to_csv()

session = db_session()
recalls.to_db(session)
citations.to_db(session)
