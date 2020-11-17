# Copyright (c) 2020 Jonathan Hildenbrand
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Date, Integer, String

Base = declarative_base()


class Citation(Base):
    __tablename__ = 'citation'

    id = Column(Integer, primary_key=True)
    inspection_id = Column(Integer)
    fei_number = Column(Integer)
    legal_name = Column(String)
    inspection_end_date = Column(Date)
    program_area = Column(String)
    act_cfr_number = Column(String)
    short_description = Column(String)
    long_description = Column(String)
    firm_profile = Column(String)


class ComplianceAction(Base):
    __tablename__ = 'compliance_action'

    id = Column(Integer, primary_key=True)
    fei_number = Column(Integer)
    firm_name = Column(String)
    firm_state = Column(String)
    country_area = Column(String)
    product_type = Column(String)
    action_taken_date = Column(Date)
    action_type = Column(String)
    case_id = Column(Integer)
    firm_profile = Column(String)


class FirmProfile(Base):
    __tablename__ = 'firm_profile'

    id = Column(Integer, primary_key=True)
    fei_number = Column(Integer)
    firm_name = Column(String)
    firm_address1 = Column(String)
    firm_address2 = Column(String)
    firm_address3 = Column(String)


class ImportRefusal(Base):
    __tablename__ = 'import_refusal'

    id = Column(Integer, primary_key=True)
    fei_number = Column(Integer)
    firm_legal_name = Column(String)
    firm_address = Column(String)
    product_code_and_description = Column(String)
    refused_date = Column(Date)
    import_division = Column(String)
    shipment_id = Column(String)
    fda_sample_analysis = Column(String)
    private_lab_analysis = Column(String)
    refusal_charges = Column(String)
    firm_profile = Column(String)


class ImportSummary(Base):
    __tablename__ = 'import_summary'

    id = Column(Integer, primary_key=True)
    fiscal_year = Column(Integer)
    product_category = Column(String)
    total_lines = Column(Integer)
    refused_lines = Column(Integer)
    examined_lines = Column(Integer)
    sampled_lines = Column(Integer)


class Inspection(Base):
    __tablename__ = 'inspection'

    id = Column(Integer, primary_key=True)
    fei_number = Column(Integer)
    legal_name = Column(String)
    city = Column(String)
    state = Column(String)
    zip_code = Column(String)
    country_area = Column(String)
    fiscal_year = Column(Integer)
    inspection_id = Column(Integer)
    posted_citations = Column(String)
    inspection_end_date = Column(Date)
    classification = Column(String)
    project_area = Column(String)
    product_type = Column(String)
    firm_profile = Column(String)


class Recall(Base):
    __tablename__ = 'recall'

    def __init__(self, data):

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
    openfda = Column(String)
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
                     self.openfda,
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
