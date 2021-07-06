# Copyright (c) 2020 Jonathan Hildenbrand
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class OpenFDARecall(Base):

    __tablename__ = 'recall'

    def __init__(self, data):

        if data:
            for key, val in data.items():
                setattr(self, key, val)

    id = Column(Integer, primary_key=True)
    recall_number = Column(String)
    report_date = Column(Date)
    recall_initiation_date = Column(Date)
    center_classification_date = Column(Date)
    termination_date = Column(Date)
    classification = Column(String)
    voluntary_mandated = Column(String)
    initial_firm_notification = Column(String)
    status = Column(String)
    # openfda = Column(String)
    event_id = Column(Integer)
    recalling_firm = Column(String)
    address_1 = Column(String)
    address_2 = Column(String)
    city = Column(String)
    state = Column(String)
    postal_code = Column(String)
    country = Column(String)
    product_type = Column(String)
    product_description = Column(String)
    product_quantity = Column(String)
    code_info = Column(String)
    more_code_info = Column(String)
    reason_for_recall = Column(String)
    distribution_pattern = Column(String)

    def __iter__(self):
        return iter([self.id,
                     self.recall_number,
                     self.report_date,
                     self.recall_initiation_date,
                     self.center_classification_date,
                     self.termination_date,
                     self.classification,
                     self.voluntary_mandated,
                     self.initial_firm_notification,
                     self.status,
                     #  self.openfda,
                     self.event_id,
                     self.recalling_firm,
                     self.address_1,
                     self.address_2,
                     self.city,
                     self.state,
                     self.postal_code,
                     self.country,
                     self.product_type,
                     self.product_description,
                     self.product_quantity,
                     self.code_info,
                     self.more_code_info,
                     self.reason_for_recall,
                     self.distribution_pattern])


class AdverseEvent(Base):

    __tablename__ = 'adverse_event'

    def __init__(self, data):

        if data:
            for key, val in data.items():
                setattr(self, key, val)

    id = Column(Integer, primary_key=True)
    report_number = Column(String)
    outcomes = Column(String)
    date_created = Column(Date)
    reactions = relationship('AdverseEventReaction')
    products = relationship('AdverseEventProduct')
    consumer_age = Column(String)
    consumer_age_unit = Column(String)
    consumer_gender = Column(String)


class AdverseEventReaction(Base):

    __tablename__ = 'adverse_event_reaction'

    id = Column(Integer, primary_key=True)
    adverse_event_id = Column(Integer, ForeignKey('adverse_event.id'))

    def __iter__(self):
        return ([])


class AdverseEventProduct(Base):

    __tablename__ = 'adverse_event_product'

    id = Column(Integer, primary_key=True)
    adverse_event_id = Column(Integer, ForeignKey('adverse_event.id'))

    def __iter__(self):
        return ([])
