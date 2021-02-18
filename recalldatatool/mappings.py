# Copyright (c) 2020 Jonathan Hildenbrand
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

Base = declarative_base()


class USFDARecall(Base):

    __tablename__ = 'usfda_recall'

    def __init__(self, data):

        if data:
            for key, val in data.items():
                setattr(self, key, val)

    id = db.Column(db.Integer, primary_key=True)
    recall_number = db.Column(db.String)
    report_date = db.Column(db.Date)
    recall_initiation_date = db.Column(db.Date)
    center_classification_date = db.Column(db.Date)
    termination_date = db.Column(db.Date)
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


class CFIARecall(Base):

    __tablename__ = 'cfia_recall'

    def __init__(self, data):

        if data:
            for key, val in data.items():
                setattr(self, key, val)

    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.Date)
    date_published = db.Column(db.Date)
    subtype = db.Column(db.String)
    subcategory = db.Column(db.String)
    classification = db.Column(db.String)
    source = db.Column(db.String)
    recalling_firm = db.Column(db.String)
    distribution = db.Column(db.String)
    extent_distribution = db.Column(db.String)
    cfia_reference_number = db.Column(db.Integer)
    product_details = relationship('CFIAProductDetail')


class CFIAProductDetail(Base):

    __tablename__ = 'cfia_product_detail'

    def __init__(self, data):

        if data:
            for key, val in data.items():
                setattr(self, key, val)

    id = db.Column(db.Integer, primary_key=True)
    recall_id = db.Column(db.Integer, ForeignKey('cfia_recall.id'))
    brand_name = db.Column(db.String)
    common_name = db.Column(db.String)
    size = db.Column(db.String)
    product_codes = db.Column(db.String)
    upc = db.Column(db.String)


class UKFSARecall(Base):

    __tablename__ = 'ukfsa_recall'

    def __init__(self, data):

        if data:
            for key, val in data.items():
                setattr(self, key, val)

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    short_title = db.Column(db.String)
    description = db.Column(db.String)
    created = db.Column(db.Date)
    modified = db.Column(db.DateTime)
    notation = db.Column(db.String)
    action_taken = db.Column(db.String)
    consumer_advice = db.Column(db.String)
    alert_url = db.Column(db.String)
    country = db.Column(db.String)  # country.label
    status_label = db.Column(db.String)
    recall_type = db.Column(db.String)
    reporting_business = db.Column(db.String)
    other_business = db.Column(db.String)
    risk_statement = db.Column(db.String)
    allergen = db.Column(db.String)
    allergen_label = db.Column(db.String)
    allergen_notation = db.Column(db.String)
    allergen_risk_statement = db.Column(db.String)
    hazard_category = db.Column(db.String)
    hazard_category_label = db.Column(db.String)
    hazard_category_notation = db.Column(db.String)
    pathogen_risk = db.Column(db.String)
    pathogen_label = db.Column(db.String)
    pathogen_notation = db.Column(db.String)
    pathogen_risk_pathogen = db.Column(db.String)
    pathogen_risk_statement = db.Column(db.String)
    reason = db.Column(db.String)
    reason_label = db.Column(db.String)
    reason_notation = db.Column(db.String)
    product_details = relationship('UKFSAProductDetail')


class UKFSAProductDetail(Base):

    __tablename__ = 'ukfsa_product_detail'

    def __init__(self, data):

        if data:
            for key, val in data.items():
                setattr(self, key, val)

    id = db.Column(db.Integer, primary_key=True)
    reacll_id = db.Column(db.Integer, ForeignKey('ukfsa_recall.id'))
    product_name = db.Column(db.String)
    product_code = db.Column(db.String)
    pack_size_description = db.Column(db.String)
    allergen = db.Column(db.String)
    batch_description = db.Column(db.String)
    product_category = db.Column(db.String)


class EFSARecall(Base):

    __tablename__ = 'efsa_recall'

    def __init__(self, data):

        if data:
            for key, val in data.items():
                setattr(self, key, val)

    id = db.Column(db.Integer, primary_key=True)
    reference = db.Column(db.String)
    notification_date = db.Column(db.Date)
    last_update = db.Column(db.Date)
    notification_country = db.Column(db.String)
    classification = db.Column(db.String)
    risk_decision = db.Column(db.String)
    notification_type = db.Column(db.String)
    action_taken = db.Column(db.String)
    distribution_status = db.Column(db.String)
    product = db.Column(db.String)
    product_category = db.Column(db.String)
    product_detail_url = db.Column(db.String)
    country_origin = db.Column(db.String)
    country_distribution = db.Column(db.String)
    country_concern = db.Column(db.String)
    hazards = relationship('EFSAProductDetail')


class EFSARecallHazard(Base):

    __tablename__ = 'efsa_hazard'

    def __init__(self, data):

        if data:
            for key, val in data.items():
                setattr(self, key, val)

    id = db.Column(db.Integer, primary_key=True)
    recall_id = db.Column(db.Integer, ForeignKey('efsa_recall.id'))
    substance_hazard = db.Column(db.String)
    category = db.Column(db.String)
    analytical_result = db.Column(db.String)
    units = db.Column(db.String)
    sampling_date = db.Column(db.Date)
