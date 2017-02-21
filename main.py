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

class MainHandler(webapp2.RequestHandler):

    formstring = """<form method=post action="/">
   <p>Enter Your Id: <input type="text" name="id"/></p>
   <p>Password: <input type="password" name="pwd"/></p>
   <p><input type="submit"></p>
   </form>"""

    def get(self):
        self.response.write(self.formstring)

    def post(self):
        savedid='admin@naver.com'
        savedpwd='keroro2424'
        stringid=self.request.get('id')
        stringpwd=self.request.get('pwd')
        
        if savedid == stringid and savedpwd == stringpwd:
            self.response.write('hello admin')
        else:
            self.response.write('It is wrong')
            self.response.write(self.formstring)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
], debug=True)
