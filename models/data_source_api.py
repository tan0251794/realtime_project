from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Integer, String

from library.database import Base


class DataSourceAPI(Base):
    __tablename__ = "tms_data_source_api"

    ID = Column(Integer, primary_key=True, index=True)
    CREATED_AT = Column(DateTime, default=datetime.now)
    MODIFIED_AT = Column(DateTime, default=datetime.now)
    CREATED_BY = Column(String)
    MODIFIED_BY = Column(String)
    NAME = Column(String)
    C_METHOD_TYPE = Column(Integer, default=1)
    URL = Column(String)
    C_AUTH_TYPE = Column(Integer, default=1)
    ACTIVE_FLAG = Column(Boolean, default=True)
    API_TYPE = Column(Integer, default=1)
    REQUEST_BODY_EXAMPLE = Column(String(2000), nullable=True)
    RESPONSE_BODY_EXAMPLE = Column(String(2000), nullable=True)
    RESPONSE_FIELD_LIST = Column(String(2000), nullable=True)
    DATA_SOURCE_API_GROUP_ID = Column(Integer)
    CODE = Column(String)
    AUTH_JSON = Column(String(2000))
    HEADER_LIST = Column(String(2000))
    PARAMETER_LIST = Column(String(2000))
    REQUEST_BODY = Column(String(2000), nullable=True)
