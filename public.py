import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template

class PublicPage(webapp.RequestHandler):
    def get(self):
        template_values = {
                "notices": ["This is a test", "Test number 2"],
        }

        path = os.path.join(os.path.dirname(__file__), 'templates/public.html')
        self.response.out.write(template.render(path, template_values))

application = webapp.WSGIApplication(
                                    [('/', PublicPage)],
                                    debug=True)

def main():
    run_wsgi_app(application)

if __name__=="__main__":
    main()
