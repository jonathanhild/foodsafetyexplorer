# Copyright (c) 2020 Jonathan Hildenbrand
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from datetime import time
from fdadatatool import factory

recalls = factory.create('RECALLS')
recalls.get_data(1)
recalls.to_csv()

time.sleep(1)
