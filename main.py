

import webapp2
import controllerhandle


application = webapp2.WSGIApplication([
    ('/', controllerhandle.MainHandler),
    ('/post', controllerhandle.MainHandler)
    
], debug=True)
