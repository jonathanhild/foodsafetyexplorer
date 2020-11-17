# Copyright (c) 2020 Jonathan Hildenbrand
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import csv
import os
from datetime import datetime as dt

import requests

from .data_factory import factory
from .mappings import Recall

FIELDNAMES = ['country',
              'city',
              'address_1',
              'reason_for_recall',
              'address_2',
              'product_quantity',
              'code_info',
              'center_classification_date',
              'distribution_pattern',
              'state',
              'product_description',
              'report_date',
              'classification',
              'openfda',
              'recalling_firm',
              'recall_number',
              'initial_firm_notification',
              'product_type',
              'event_id',
              'termination_date',
              'more_code_info',
              'recall_initiation_date',
              'postal_code',
              'voluntary_mandated',
              'status']


class RecallBuilder:
    def __init__(self):
        self._base = 'https://api.fda.gov/food/enforcement.json'
        self._skip = 0
        self._limit = 1000
        self._total = 0
        self._last_updated = None
        self.data = []

        self.get_metadata()

    def get_metadata(self):
        re = requests.get(self._base)
        json = re.json()
        json = json["meta"]
        self._skip = json['results']['skip']
        self._total = json['results']['total']
        self._last_updated = dt.strptime(
            json['last_updated'], "%Y-%m-%d")

    def get_data(self, record_limit=None):
        if record_limit is None:
            record_limit = self._total
        while self._skip < record_limit:
            params = {'skip': self._skip, 'limit': self._limit}
            re = requests.get(self._base, params)
            responses = re.json()
            for response in responses['results']:
                recall = Recall(response)
                self.data.append(recall)
                print(f'Object {self._skip}')
                self._skip += 1

    def to_csv(self, filename=None):
        if filename is None:
            filename = 'recalls.csv'
        filepath = os.path.join('.', 'data', filename)
        with open(filepath, 'w') as f:
            w = csv.writer(f,
                           delimiter=',',
                           quotechar='"',
                           quoting=csv.QUOTE_MINIMAL)
            w.writerow(self.data[0].__table__.columns)
            for row in self.data:
                w.writerow(list(row))

    def to_db(self, db_session):
        pass


class IRecallBuilder:
    def __init__(self):
        self._instance = None

    def __call__(self):
        if not self._instance:
            self._instance = RecallBuilder()
        return self._instance


factory.register_builder('RECALLS', IRecallBuilder())
