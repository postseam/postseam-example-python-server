from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import BigInteger
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class ProductModel(Base):
    __tablename__ = "product"

    id = Column(String, primary_key=True)
    store_id = Column(String, nullable=False)
    product_name = Column(String, nullable=False)
    product_description = Column(String, nullable=False)
    create_time = Column(BigInteger, nullable=False)
    update_time = Column(BigInteger)
