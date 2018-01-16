import jinja2
import logging
import os
import webapp2

from google.appengine.api import users

# We set a parent key on the 'Greetings' to ensure that they are all in the
# same entity group. Queries across the single entity group will be consistent.
# However, the write rate should be limited to ~1/second.


jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


def process_input(request):
    # process the input
    input = {}
    input[1] = []
    input[2] = []
    input[3] = []
    input[4] = []

    input[1].append(request.get('inf1', 0))
    input[1].append(request.get('arch1', 0))
    input[1].append(request.get('cav1', 0))
    input[1].append(request.get('seige1', 0))
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
    ], debug=True)
