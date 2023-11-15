from sqlalchemy import DateTime, Integer, String, ForeignKey
from sqlalchemy_utils import EmailType

from sqlalchemy.orm import mapped_column


from ..utils.db import db


class User(db.Model):
    """User Model"""

    id = mapped_column(Integer, primary_key=True)
    first_name = db.Column(String(length=50), nullable=False)
    last_name = db.Column(String(length=50), nullable=True)
    email = db.Column(String, unique=True, nullable=False)
    password = db.Column(String, nullable=False)
    # Getting contacts
    contacts = db.relationship("Contact", back_populates="users")


class Contact(db.Model):
    """Contact Model"""

    id = db.Column(Integer, primary_key=True)
    first_name = db.Column(String(length=50))
    last_name = db.Column(String(length=50))
    local_phone = db.Column(String(length=25))
    mobile_phone = db.Column(String(length=25))
    email = db.Column(EmailType)
    user_id = mapped_column(Integer, ForeignKey("user.id"))
    # Getting user
    user = db.relationship("User", back_populates="contacts")
