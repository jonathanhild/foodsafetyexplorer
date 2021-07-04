# Copyright (c) 2020 Jonathan Hildenbrand
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from datetime import datetime as dt

import requests
from tqdm import tqdm

from .data_factory import factory
from .mappings import CFIARecall


class CFIARecallBuilder:
    def __init__(self):
        self._url = 'https://healthycanadians.gc.ca/recall-alert-rappel-avis/api/search?search='
        self._event_urls = []

    def get_event_urls(self):
        params = {'cat': 1, 'lim': 0}
        re = requests.get(self._url, params)
        responses = re.json()
        for response in responses:
            self.event_urls.append(response['url'])

    def get_events(self):
        for event in self._event_urls:
            re = requests.get(event)
            response = re.json()
            response['start_time'] = dt.fromtimestamp(response['start_time'])
            response['date_published'] = dt.fromtimestamp(response['date_published'])
            pass

    def get_product_details(self):
        pass

    def to_db(self, session):
        for d in self.data:
            session.add(d)
        print('Inserting recall records into database.')
        session.commit()

    # TODO: create method to update metadata table


class ICFIARecallBuilder:
    def __init__(self):
        self._instance = None

    def __call__(self, **kwargs):
        if not self._instance:
            self._instance = CFIARecallBuilder(**kwargs)
        return self._instance


factory.register_builder('USFDA_RECALL', ICFIARecallBuilder())
