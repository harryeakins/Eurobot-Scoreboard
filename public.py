import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template

class Team:
    def __init__(self, name, score):
        self.name = name
        self.match_score = score

from datetime import datetime

test_context = {
        "competition_active": True,
        "red_team": Team("ICRobot", 120),
        "blue_team": Team("MDX", 20),
        }

class PublicPage(webapp.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'templates/public.html')
        self.response.out.write(template.render(path, test_context))

application = webapp.WSGIApplication(
                                    [('/', PublicPage)],
                                    debug=True)

def main():
    run_wsgi_app(application)

if __name__=="__main__":
    main()
