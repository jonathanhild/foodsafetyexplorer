# Copyright (c) 2020 Jonathan Hildenbrand
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from datetime import datetime as dt

import requests
from tqdm import tqdm

from .data_factory import factory
from .mappings import OpenFDARecall


class OpenFDARecallBuilder:
    def __init__(self):
        self._url = 'https://api.fda.gov/food/enforcement.json'
        self._skip = 0
        self._limit = 1000
        self._total = 0
        self._last_updated = None
        self.data = []

        self.get_metadata()

    def get_metadata(self):
        re = requests.get(self._url)
        json = re.json()
        json = json["meta"]
        self._skip = json['results']['skip']
        self._total = json['results']['total']
        self._last_updated = dt.strptime(
            json['last_updated'], "%Y-%m-%d")

    def get_events(self, record_limit=None):
        if record_limit is None:
            record_limit = self._total
        while self._skip < record_limit:
            params = {'skip': self._skip, 'limit': self._limit}
            re = requests.get(self._url, params)
            responses = re.json()
            message = f'Downloading {self._skip} of {record_limit}'
            for response in tqdm(iterable=responses['results'],
                                 leave=True, desc=message):
                recall = OpenFDARecall(response)
                self.data.append(recall)
                self._skip += 1

    def to_db(self, session):
        for d in self.data:
            session.add(d)
        print('Inserting recall records into database.')
        session.commit()


class IOpenFDARecallBuilder:
    def __init__(self):
        self._instance = None

    def __call__(self, **kwargs):
        if not self._instance:
            self._instance = OpenFDARecall(**kwargs)
        return self._instance


factory.register_builder('OPENFDA_RECALL', IOpenFDARecallBuilder())
