# Copyright (c) 2020 Jonathan Hildenbrand
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from datetime import time

from fdadatatool import factory, create_db, create_session

recalls = factory.create('RECALLS')
recalls.get_data()
recalls.to_csv()

create_db()

session = create_session()

recalls.to_db(session)


time.sleep(1)
