""" The models module provides App Engine db.Model classes for storing freefall models in the App Engine database. """

from google.appengine.ext import db
from google.appengine.ext import blobstore

class Salon(db.Model):
  name=db.StringProperty(required=True)
  displayName=db.StringProperty(required=True)

class Member(db.Model):
  user=db.UserProperty(required=True)
  name=db.StringProperty(required=True)

class Application(db.Model):
  user=db.UserProperty(required=True)
  essay=db.TextProperty(required=True)
  status=db.StringProperty(required=True)
  username=db.StringProperty(required=True)

class Post(db.Model):
  salon=db.ReferenceProperty(Salon, required=True)
  draft=db.BooleanProperty(required=True)
  author=db.ReferenceProperty(Member, required=True)
  date=db.DateTimeProperty(required=True)
  subject=db.StringProperty(required=True)
  body=db.TextProperty(required=True)
  replyto=db.SelfReferenceProperty(required=False)

class TODO(db.Model):
  category=db.StringProperty(required=False)
  author=db.ReferenceProperty(Member, required=True)
  date=db.DateTimeProperty(required=True)
  text=db.StringProperty(required=True)
  
