

import webapp2
import controllerhandle

application = webapp2.WSGIApplication([
    ('/', controllerhandle.MainHandler),
    ('/sendMail', controllerhandle.MainHandler)
    
], debug=True)
