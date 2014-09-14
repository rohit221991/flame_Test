import webapp2
import os
import jinja2
import logging
import json

from constants import cities, categories
# from models import Image, image_key
from model import *
from utilities import *

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                               autoescape=True)


# Shorthand functions to make life easier
class BaseHandler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))
        
        
class MainPage(BaseHandler):
    def get(self):
#        self.write("We are building something.... Wait For it.... Lengendary")
        self.render('index.html')
    
app = webapp2.WSGIApplication([
    ('/', MainPage),
   
], debug=True)
