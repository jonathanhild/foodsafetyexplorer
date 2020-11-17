# Copyright (c) 2020 Jonathan Hildenbrand
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from fdadatatool import factory

recalls = factory.create('RECALLS')
recalls.get_data()
recalls.to_csv()
