from datetime import datetime

import logging

from google.appengine.api import users
from google.appengine.api import memcache
from google.appengine.ext import db

from rpc import JsonRpcService
from models import *

class UserService(JsonRpcService):
  def json_isLoggedIn(self):
    user = users.get_current_user()
    logging.info('isLoggedIn '+str(user));
    return user!=None

  def json_isAdmin(self):
    return users.is_current_user_admin()

  def json_login(self):
    return users.create_login_url('/admin')

  def json_logout(self):
    return users.create_logout_url('/')
