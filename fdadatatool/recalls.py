# Copyright (c) 2020 Jonathan Hildenbrand
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import csv
import os
from datetime import datetime as dt

import requests

from .data_factory import factory

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


class RecallData:
    def __init__(self):
        self._base = "https://api.fda.gov/food/enforcement.json"
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

    def get_data(self):
        while self._skip < self._total:
            params = {'skip': self._skip, 'limit': self._limit}
            re = requests.get(self._base, params)
            response = re.json()
            idx = 0
            for r in response['results']:
                self.data.append(r)
                idx += 1
                self._skip += 1

    def to_csv(self):
        path = os.path.join('data', 'recalls.csv')
        with open(path, 'w') as f:
            w = csv.DictWriter(f, fieldnames=FIELDNAMES)
            w.writeheader()
            for row in self.data:
                w.writerow(row)

    def to_db(self):


class RecallDataBuilder:
    def __init__(self):
        self._instance = None

    def __call__(self):
        if not self._instance:
            self._instance = RecallData()
        return self._instance


factory.register_builder("RECALLS", RecallDataBuilder())
