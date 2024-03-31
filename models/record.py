from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, sql
from sqlalchemy.orm import relationship, backref
from core.db import Base


class DiagnosisRecord(Base):
    __tablename__ = "diagnosis_record"
    id = Column(Integer, primary_key=True, index=True, unique=True)
    diagnostic_person = Column(Integer, comment="诊断人")
