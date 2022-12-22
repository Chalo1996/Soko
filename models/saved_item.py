#!/usr/bin/python3
""" SavedItem class module
        Definition of SavedItem class, it attributes,
        and methods
"""
from models.base_model import Base, BaseModel
from sqlalchemy import Column, ForeignKey, Integer, String


class SavedItem(Base, BaseModel):
    """ SavedItem class representing saved_items table
        Attributes:
                customer_id (str): foreign key to customer table's
                                   id field
                product_id (str):  product's id
                product_image(str): product's main image
                product_name (str):  product's name
    """
    __tablename__ = "saved_items"

    customer_id = Column(String(60), ForeignKey("customers.id"),
                         nullable=False)
    product_id = Column(String(60), nullable=False)
    product_name = Column(String(128), nullable=False)
    product_image = Column(String(128), nullable=False)
    quantity = Column(Integer, nullable=False)

    def __init__(self, **kwargs):
        """Instantiates a SavedItem object."""
        super().__init__(**kwargs)
