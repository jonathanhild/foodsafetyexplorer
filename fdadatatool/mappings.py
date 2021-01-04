# Copyright (c) 2020 Jonathan Hildenbrand
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Citation(Base):
    """
    SQLAlchemy declarative model for Citations.

    Args:
        Base (Base Object): SQLAlchemy declarative base.

    Returns:
        Model Object: SQLAlchemy declarative model.
    """

    __tablename__ = 'citation'

    id = db.Column(db.Integer, primary_key=True)
    inspection_id = db.Column(db.Integer)
    fei_number = db.Column(db.Integer)
    legal_name = db.Column(db.String)
    inspection_end_date = db.Column(db.String)
    program_area = db.Column(db.String)
    act_cfr_number = db.Column(db.String)
    short_description = db.Column(db.String)
    long_description = db.Column(db.String)
    firm_profile = db.Column(db.String)

    def __init__(self, data=None):
        if data:
            for key, val in data.items():
                setattr(self, key, val)

    def __iter__(self):
        return iter([self.id,
                     self.inspection_id,
                     self.fei_number,
                     self.legal_name,
                     self.inspection_end_date,
                     self.program_area,
                     self.act_cfr_number,
                     self.short_description,
                     self.long_description,
                     self.firm_profile])


class ComplianceAction(Base):
    """
    SQLAlchemy declarative model for Compliance Actions.

    Args:
        Base (Base Object): SQLAlchemy declarative base.

    Returns:
        Model Object: SQLAlchemy declarative model.
    """
    __tablename__ = 'compliance_action'

    id = db.Column(db.Integer, primary_key=True)
    fei_number = db.Column(db.Integer)
    firm_name = db.Column(db.String)
    firm_state = db.Column(db.String)
    country_area = db.Column(db.String)
    product_type = db.Column(db.String)
    action_taken_date = db.Column(db.String)
    action_type = db.Column(db.String)
    case_id = db.Column(db.Integer)
    firm_profile = db.Column(db.String)

    def __init__(self, data=None):
        if data:
            for key, val in data.items():
                setattr(self, key, val)

    def __iter__(self):
        return iter([self.id,
                     self.fei_number,
                     self.firm_name,
                     self.firm_state,
                     self.country_area,
                     self.product_type,
                     self.action_taken_date,
                     self.action_type,
                     self.case_id,
                     self.firm_profile])


class FirmProfile(Base):
    """
    SQLAlchemy declarative model for Firm Profiles.

    Args:
        Base (Base Object): SQLAlchemy declarative base.

    Returns:
        Model Object: SQLAlchemy declarative model.
    """

    __tablename__ = 'firm_profile'

    id = db.Column(db.Integer, primary_key=True)
    fei_number = db.Column(db.Integer)
    firm_name = db.Column(db.String)
    firm_address1 = db.Column(db.String)
    firm_address2 = db.Column(db.String)
    firm_address3 = db.Column(db.String)

    def __init__(self, data):
        if data:
            for key, val in data.items():
                setattr(self, key, val)

    def __iter__(self):
        return iter([self.id,
                     self.fei_number,
                     self.firm_name,
                     self.firm_address1,
                     self.firm_address2,
                     self.firm_address3])


class ImportRefusal(Base):
    """
    SQLAlchemy declarative model for Import Refusals.

    Args:
        Base (Base Object): SQLAlchemy declarative base.

    Returns:
        Model Object: SQLAlchemy declarative model.
    """

    __tablename__ = 'import_refusal'

    id = db.Column(db.Integer, primary_key=True)
    fei_number = db.Column(db.Integer)
    firm_legal_name = db.Column(db.String)
    firm_address = db.Column(db.String)
    product_code_and_description = db.Column(db.String)
    refused_date = db.Column(db.String)
    import_division = db.Column(db.String)
    shipment_id = db.Column(db.String)
    fda_sample_analysis = db.Column(db.String)
    private_lab_analysis = db.Column(db.String)
    refusal_charges = db.Column(db.String)
    firm_profile = db.Column(db.String)

    def __init__(self, data):
        if data:
            for key, val in data.items():
                setattr(self, key, val)

    def __iter__(self):
        return iter([self.id,
                     self.fei_number,
                     self.firm_legal_name,
                     self.firm_address,
                     self.product_code_and_description,
                     self.refused_date,
                     self.import_division,
                     self.shipment_id,
                     self.fda_sample_analysis,
                     self.private_lab_analysis,
                     self.refusal_charges,
                     self.firm_profile])


class ImportSummary(Base):
    """
    SQLAlchemy declarative model for Import Summarys.

    Args:
        Base (Base Object): SQLAlchemy declarative base.

    Returns:
        Model Object: SQLAlchemy declarative model.
    """

    __tablename__ = 'import_summary'

    id = db.Column(db.Integer, primary_key=True)
    fiscal_year = db.Column(db.Integer)
    product_category = db.Column(db.String)
    total_lines = db.Column(db.Integer)
    refused_lines = db.Column(db.Integer)
    examined_lines = db.Column(db.Integer)
    sampled_lines = db.Column(db.Integer)

    def __init__(self, data):
        if data:
            for key, val in data.items():
                setattr(self, key, val)

    def __iter__(self):
        return iter([self.id,
                     self.fiscal_year,
                     self.product_category,
                     self.total_lines,
                     self.refused_lines,
                     self.examined_lines,
                     self.sampled_lines])


class Inspection(Base):
    """
    SQLAlchemy declarative model for Inspections.

    Args:
        Base (Base Object): SQLAlchemy declarative base.

    Returns:
        Model Object: SQLAlchemy declarative model.
    """

    __tablename__ = 'inspection'

    id = db.Column(db.Integer, primary_key=True)
    fei_number = db.Column(db.Integer)
    legal_name = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String)
    zip_code = db.Column(db.String)
    country_area = db.Column(db.String)
    fiscal_year = db.Column(db.Integer)
    inspection_id = db.Column(db.Integer)
    posted_citations = db.Column(db.String)
    inspection_end_date = db.Column(db.String)
    classification = db.Column(db.String)
    project_area = db.Column(db.String)
    product_type = db.Column(db.String)
    firm_profile = db.Column(db.String)

    def __init__(self, data):
        if data:
            for key, val in data.items():
                setattr(self, key, val)

    def __iter__(self):
        return iter([self.id,
                     self.fei_number,
                     self.legal_name,
                     self.city,
                     self.state,
                     self.zip_code,
                     self.country_area,
                     self.fiscal_year,
                     self.inspection_id,
                     self.posted_citations,
                     self.inspection_end_date,
                     self.classification,
                     self.project_area,
                     self.product_type,
                     self.firm_profile])


class Recall(Base):
    """
    SQLAlchemy declarative model for Recalls.

    Args:
        Base (Base Object): SQLAlchemy declarative base.

    Returns:
        Model Object: SQLAlchemy declarative model.
    """

    __tablename__ = 'recall'

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
