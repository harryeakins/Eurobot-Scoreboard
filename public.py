import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template

test_context = {
        "competition_active": True,
        "red_team": {"name": "ICRobot",
                     "match_score": {
                            "total": 60,
                            "normal": 40,
                            "bonus": 20,
                         }
                     },
        "blue_team": {"name": "MDX",
                     "match_score": {
                            "total": 20,
                            "normal": 15,
                            "bonus": 5,
                         }
                     },

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
