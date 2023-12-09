import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    userName = Column(String(255))
    firstName =  Column(String(255))
    lastName = Column(String(255))
    profile_pic = Column(String(255))
class Post(Base):
    __tablename__ = 'Post'
    id = Column(Integer, primary_key=True)
    media = Column(String(255))
    caption = Column(String(255))
    user_poster_id = Column(Integer, ForeignKey('User.id'))

    def to_dict(self):
        return {}
class Followers(Base):
    __tablename__ = 'Followers'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.id'))
    following_user_id = Column(Integer, ForeignKey('User.id'))
class Comments(Base):
    __tablename__ = 'Comments'
    id = Column(Integer, primary_key=True)
    commenter_id = Column(Integer, ForeignKey(User.id))
    content = Column(String(255))
    liked = Column(Boolean)



## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
