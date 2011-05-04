import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template

from databases import *

class PublicPage(webapp.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'templates/public.html')
        matches = Match.gql("ORDER BY regdate DESC").get()
        if matches != None:
            test_context = {
                    "competition_active": True,
                    "red_team": {"name": matches.red.name,
                                 "match_score": {
                                        "total": matches.rednormal+matches.redbonus,
                                        "normal": matches.rednormal,
                                        "bonus": matches.redbonus,
                                     }
                                 },
                    "blue_team": {"name": matches.blue.name,
                                 "match_score": {
                                        "total": matches.bluenormal+matches.bluebonus,
                                        "normal": matches.bluenormal,
                                        "bonus": matches.bluebonus,
                                     }
                                 },
            
                    }
        else:
#            new1 = Team(name = "ICRobot")
#            new1.put()
#            new2 = Team(name = "MDX")
#            new2.put()
#            newm = Match()
#            newm.red = new1
#            newm.rednormal = 40
#            newm.redbonus = 20
#            newm.blue = new2
#            newm.bluenormal = 15
#            newm.bluebonus = 5
#            newm.put()
            test_context = {
                    "competition_active": False
                }


        self.response.out.write(template.render(path, test_context))

application = webapp.WSGIApplication(
                                    [('/', PublicPage)],
                                    debug=True)

def main():
    run_wsgi_app(application)

if __name__=="__main__":
    main()
