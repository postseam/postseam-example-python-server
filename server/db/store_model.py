from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class StoreModel(Base):
    __tablename__ = "store"

    id = Column(String, primary_key=True)
    email = Column(String, nullable=False)
    business_name = Column(String, nullable=False)
