from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from backend.database.mysql import Base


class UploadedFile(Base):
    __tablename__ = "uploaded_files"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String(255), nullable=False)
    upload_time = Column(DateTime, default=datetime.utcnow)