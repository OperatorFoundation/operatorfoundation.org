#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

from google.appengine.ext.webapp import RequestHandler

class LetsEncryptHandler(RequestHandler):

    def get(self, challenge):
        self.response.headers['Content-Type'] = 'text/plain'
        responses = {
                    'bY-vrwn-BFJVba0lZBU-mHKzc6bqwDYYcKzrC5O-nEs': 'bY-vrwn-BFJVba0lZBU-mHKzc6bqwDYYcKzrC5O-nEs.KxZb0_QrlYj56nhfSzUQOGlYZYh2lwWnlERQAgXv-Pg',
                    '6H2A1G74PxPg5kWw9Nf9ftXu_pQyTNG3rAFiUGoY2wE': '6H2A1G74PxPg5kWw9Nf9ftXu_pQyTNG3rAFiUGoY2wE.KxZb0_QrlYj56nhfSzUQOGlYZYh2lwWnlERQAgXv-Pg',
                    'mZBJri6KmUMk5PhCNL6Q8LK6vO3VrKBfKjrBNmCS15g': 'mZBJri6KmUMk5PhCNL6Q8LK6vO3VrKBfKjrBNmCS15g.KxZb0_QrlYj56nhfSzUQOGlYZYh2lwWnlERQAgXv-Pg',
                    '3BWwqM8__8TShJHoBMZCDW54rFVbkl4abhwF3J7Qoi0': '3BWwqM8__8TShJHoBMZCDW54rFVbkl4abhwF3J7Qoi0.KxZb0_QrlYj56nhfSzUQOGlYZYh2lwWnlERQAgXv-Pg',
                    '3BWwqM8__8TShJHoBMZCDW54rFVbkl4abhwF3J7Qoi0': '3BWwqM8__8TShJHoBMZCDW54rFVbkl4abhwF3J7Qoi0.KxZb0_QrlYj56nhfSzUQOGlYZYh2lwWnlERQAgXv-Pg'
                }
        self.response.write(responses.get(challenge, ''))

app = webapp2.WSGIApplication([
    ('/.well-known/acme-challenge/([\w-]+)', LetsEncryptHandler),
], debug=True)
