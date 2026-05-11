from sqlalchemy import Column, Integer, String, Text
from database.mysql import Base

class ThreatReport(Base):
    __tablename__ = "threat_reports"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    content = Column(Text)
    severity = Column(String(50))