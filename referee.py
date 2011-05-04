import os
import logging
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template

class RefereePage(webapp.RequestHandler):
    def post(self):
        logging.debug("Name: " + self.request.get("name"))
        self.get()

    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'templates/referee.html')
        self.response.out.write(template.render(path, {}))


def main():
    logging.getLogger().setLevel(logging.DEBUG)
    application = webapp.WSGIApplication(
            [('/referee', RefereePage)],
            debug=True)

    run_wsgi_app(application)

if __name__=="__main__":
    main()
