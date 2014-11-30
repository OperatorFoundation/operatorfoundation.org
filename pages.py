from datetime import datetime

import logging

from google.appengine.api import users
from google.appengine.api import memcache
from google.appengine.ext import db

from generic import GenericPage
from models import *

class Index(GenericPage):
  def execute(self, method, user, req, resp, args):
    logging.debug("index")
    logging.debug(user)
    if not user:
      self.redirect('/welcome')
    else:
      self.redirect('/salons')

  def requireLogin(self):
    return False

class Login(GenericPage):
  def processContext(self, method, user, req, resp, args, context):
    self.redirect('/')

  def requireLogin(self):
    return True

class Logout(GenericPage):
  def processContext(self, method, user, req, resp, args, context):
    if user:
      self.redirect(users.create_logout_url('/'))
    else:
      self.redirect('/')

  def requireLogin(self):
    return False
