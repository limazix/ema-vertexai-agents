"""This module define the sub agents responsible for building the report.

Atrributes:
    data_scientst_agent: Senior Data Scientist specializing in electrical power quality data from devices like PowerNET PQ-600 G4.
    electric_engineer_agent: Senior Electric Engineer specializing in electrical power quality data from devices like PowerNET PQ-600 G4and ANEEL regulations, responsible for generating a detailed and well-structured technical compliance report.
    reviewer_agent: Expert and meticulous Reviewer, focusing on electrical engineering technical documents and ANEEL regulatory compliance.
"""

from .data_scientist_agent import data_scientst_agent
from .electric_engineer_agent import electric_engineer_agent
from .reviewer_agent import reviewer_agent

__all__ = ["data_scientst_agent", "electric_engineer_agent", "reviewer_agent"]
