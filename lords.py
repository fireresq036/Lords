import collections
import jinja2
import logging
import os
import webapp2

from google.appengine.api import users

# We set a parent key on the 'Greetings' to ensure that they are all in the
# same entity group. Queries across the single entity group will be consistent.
# However, the write rate should be limited to ~1/second.

Troops = collections.namedtuple('Troops', 'inf, arch calv siege')

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


def process_input(request):
    # process the input
    inputs = collections.defaultdict(Troops)
    inputs[1].inf = request.get('inf1', 0)
    inputs[1].arch = request.get('arch1', 0)
    inputs[1].cav = request.get('cav1', 0)
    inputs[1].seige = request.get('seige1', 0)
    inputs[2].inf = request.get('inf2', 0)
    inputs[2].arch = request.get('arch2', 0)
    inputs[2].cav = request.get('cav2', 0)
    inputs[2].seige = request.get('seige2', 0)
    inputs[3].inf = request.get('inf3', 0)
    inputs[3].arch = request.get('arch3', 0)
    inputs[3].cav = request.get('cav3', 0)
    inputs[3].seige = request.get('seige3', 0)
    inputs[4].inf = request.get('inf4', 0)
    inputs[4].arch = request.get('arch4', 0)
    inputs[4].cav = request.get('cav4', 0)
    inputs[4].seige = request.get('seige4', 0)
    logging.info(input[1])


class LordsCombat(webapp2.RequestHandler):
    def get(self):
        if self.request.get('initial', True):
            template = jinja_environment.get_template('lords_combat.html')
            self.response.out.write(template.render())
        else:
            process_input(self.request)
            template = jinja_environment.get_template('lords_combat.html')
            self.response.out.write(template.render())


class AngularTest(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('lords_angular.html')
        self.response.out.write(template.render())


class MainPage(webapp2.RequestHandler):
    def get(self):
        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'
        template = jinja_environment.get_template('index.html')
        self.response.out.write(
            template.render(url=url, url_linktext=url_linktext))


application = webapp2.WSGIApplication(
    [
        ('/', MainPage),
        ('/lords_combat', LordsCombat),
        ('/lords_angular', AngularTest),
    ], debug=True)
