from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# from fastapi import APIRouter


# engine = create_engine('sqlite:///travelers.sqlite3', echo=True)
# #manage tables
# base = declarative_base()


# class Travelers (base):
#     __travelers__= 'Travelers'
#     id = Column(Integer, primary_key = True)
#     name = Column(String)
#     email = Column(String)
#     address = Column(String)
#     creation_date = Column(Integer)

#     def __init__(self, id, name, email, address, creation_date):
#         self.id = id
#         self.name = name
#         self.email = email
#         self.address = address
#         self.creation_date = creation_date


# router = APIRouter()
# router.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///traverlers.sqlite3'

# @router.route("/carebear", methods=["GET","POST"])
# def traveler():
#     if carebear_output.method == "GET":
        
#     else
#     return

# id, name, email, address, creation date