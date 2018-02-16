import jinja2
import logging
import lords_support
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


class TroopData(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('troop_data.html')
        self.response.out.write(
            template.render(
                troopdata=lords_support.troops_as_json(
                    lords_support.init_data())))


class LordsCombat(webapp2.RequestHandler):
    def get(self):
        if self.request.get('initial', 'true') == 'true':
            logging.info("true")
            template = jinja_environment.get_template('lords_combat.html')
            self.response.out.write(template.render(
                level_names=lords_support.display_levels(),
                unit_names=lords_support.unit_names(),
                troop_size=lords_support.init_data(),
                input_tags=lords_support.tag_names(),
                size=len(lords_support.unit_names()[lords_support.LEVEL1])))
        else:
            logging.info("false")
            lords_support.process_input(self.request)
            template = jinja_environment.get_template('lords_results.html')
            self.response.out.write(template.render(
                level_names=lords_support.display_levels(),
                unit_names=lords_support.unit_names(),
                troop_size=lords_support.init_data(),
                size=len(lords_support.unit_names()[lords_support.LEVEL1])))


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
        ('/troop_data', TroopData)
    ], debug=True)
