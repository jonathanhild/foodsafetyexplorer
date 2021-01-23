# Copyright (c) 2020 Jonathan Hildenbrand
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class UsFdaRecall(Base):
    """
    SQLAlchemy declarative model for US FDA Recalls.

    Args:
        Base (Base Object): SQLAlchemy declarative base.

    Returns:
        Model Object: SQLAlchemy declarative model.
    """

    __tablename__ = 'usfda_recall'

    def __init__(self, data):

        if data:
            for key, val in data.items():
                setattr(self, key, val)

    id = db.Column(db.Integer, primary_key=True)
    recall_number = db.Column(db.String)
    report_date = db.Column(db.String)
    recall_initiation_date = db.Column(db.String)
    center_classification_date = db.Column(db.String)
    termination_date = db.Column(db.String)
    classification = db.Column(db.String)
    voluntary_mandated = db.Column(db.String)
    initial_firm_notification = db.Column(db.String)
    status = db.Column(db.String)
    # openfda = db.Column(db.String)
    event_id = db.Column(db.Integer)
    recalling_firm = db.Column(db.String)
    address_1 = db.Column(db.String)
    address_2 = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String)
    postal_code = db.Column(db.String)
    country = db.Column(db.String)
    product_type = db.Column(db.String)
    product_description = db.Column(db.String)
    product_quantity = db.Column(db.String)
    code_info = db.Column(db.String)
    more_code_info = db.Column(db.String)
    reason_for_recall = db.Column(db.String)
    distribution_pattern = db.Column(db.String)

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


class CfiaRecall(Base):
    """
    SQLAlchemy declarative model for CFIA Recalls.

    Args:
        Base ([type]): [description]
    """
    __tablename__ = 'cfia_recall'


class UkFsaRecall(Base):
    """
    SQLAlchemy declarative model for UK FSA Recalls.

    Args:
        Base ([type]): [description]
    """
    __tablename__ = 'ukfsa_recall'


class EfsaRecall(Base):
    """
    SQLAlchemy declarative model for EFSA RASFF Recalls.

    Args:
        Base ([type]): [description]
    """
    __tablename__ = 'rasff_recall'
