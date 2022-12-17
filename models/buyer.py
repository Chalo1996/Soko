#!/usr/bin/python3
""" Buyer class module
        Definition of Buyer class, it attributes,
        and methods
"""
from sqlalchemy.orm import relationship
import models
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, Numeric, CheckConstraint, ForeignKey, Text
from models.base_model import Base, BaseModel


class Buyer(Base, BaseModel):
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    region_code = Column(Integer, nullable=False)
    phone_number = Column(String(20), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(128), nullable=False)
    salt = Column(String(60))
    shop_status = Column(Integer, nullable=False)
    order = relationship('Order', backref='order')
    chat = relationship('Chat', backref='chat')

    def __init__(self, *args, **kwargs):
        """Initializes the Seller Object."""

        super().__init__(*args, **kwargs)
