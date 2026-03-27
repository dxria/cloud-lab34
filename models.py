from sqlalchemy import Boolean, Column, Float, Integer, String
from database import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(String(255), nullable=True)
    price = Column(Float, nullable=False, default=0)
    on_offer = Column(Boolean, default=False)
