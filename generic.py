import logging

from google.appengine.api import users
from google.appengine.ext import webapp
from json import loads, dumps

from jsonrpc.handler import JSONRPC

class GenericPage(webapp.RequestHandler):
  def options(self, *args):
    self.response.headers['Access-Control-Allow-Origin']='*'
    self.response.headers['Access-Control-Allow-Headers']='Content-Type'

  def get(self, *args):
    self.response.headers['Access-Control-Allow-Origin']='*'
    user = users.get_current_user()
    logging.info('Generic user: '+str(user))

    if self.requireLogin() and not user:
      self.redirect(users.create_login_url(self.request.uri))
    else:
      self.execute('get', user, self.request, self.response, args)

  def post(self, *args):
    self.response.headers['Access-Control-Allow-Origin']='*'
    logging.debug('post! '+str(self.request.path)+' '+str(self.__class__))
    user = users.get_current_user()
    self.execute('post', user, self.request, self.response, args)

  def put(self, *args):
    logging.debug('put! '+str(self.request.path)+' '+str(self.__class__))
    user = users.get_current_user()
    self.execute('put', user, self.request, self.response, args)

  def delete(self, *args):
    logging.debug('delete! '+str(self.request.path)+' '+str(self.__class__))
    user = users.get_current_user()
    self.execute('delete', user, self.request, self.response, args)

  def requireLogin(self):
    return False

  def execute(self, method, user, req, resp, args):
    pass
