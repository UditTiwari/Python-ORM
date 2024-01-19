from models.base import TimeStampeModel
from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import Relationship
from models.users import Model

class User(TimeStampeModel):
    __tablename__ = "users"

    id =Column(Integer,primay_key=True,autoincrement=True)
    first_name = Column(String(80),nullable=False)#Shift + Alt + Up/Down
    last_name = Column(String(80),nullable=False)
    email = Column(String(90),nullable=False,unique=True)

    preference =  Relationship("Preference",back_populates="user",uselist=False,passive_deletes=True)
    addresses = Relationship("Address",back_populates="user",passive_deletes=True)
    roles = Relationship("Role",secondary="user_roles",back_populates="users",passive_deletes=True)

    def __repr__(self):
        return f"{self.__class__.__name__},name:{self.first_name}{self.last_name}"
    

class Preference(TimeStampeModel):
    __tablename__="preferences"

    id = Column(Integer,primar_key=True,autoicrement=True)
    language =Column(String(80),nullable=False)
    currency =Column(String(3),nullable=False)
    user_id =Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),nullable=False,unique=True)

    user = Relationship("User",back_populates="preference")


class Address(TimeStampeModel):
    __tablename__="addresses"

    id = Column(Integer,primar_key=True,autoicrement=True)
    road_name =Column(String(80),nullable=False)
    postcode =Column(String(80),nullable=False)
    city =Column(String(80),nullable=False)
    user_id =Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),nullable=False,index=True)

    user = Relationship("User",back_populates="addresses")

    def __repr__(self):
        return f"{self.__class__.__name__},name:{self.city}"


class Role(Model):
    __tablename__="roles"

    id = Column(Integer,primar_key=True,autoicrement=True)
    name =Column(String(80),nullable=False)
    slug =Column(String(80),nullable=False,unique=True)

    users = Relationship("User",secondary="user_roles",back_populates="roles",passive_deletes=True)

    def __repr__(self):
        return f"{self.__class__.__name__},name:{self.name}"
    

class UserRole(TimeStampeModel):
    __tablename__="user_roles"

    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    role_id = Column(Integer, ForeignKey("roles.id", ondelete="CASCADE"), primary_key=True)
