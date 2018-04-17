import logging, email, cgi
from google.appengine.ext import webapp
from google.appengine.ext.webapp.mail_handlers import InboundMailHandler
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import mail
import config


# This class is a mail redirector application that forwards the mail sent to the website to its owner.
class MailRedirector(InboundMailHandler):

    """Mail Sent to the mail server is to be redirected """
    
    sender = "\""+config.OWNER_NAME+"\" <"+config.WEBSITE_MAIL_SERVER+">"

    

    # Called by GAE when an email is received.
    def receive(self, inmsg):
        # log this msg for kicks
        # download the logs to dev machine using:
        # appcfg.py --severity=0 request_logs <appname> <file_to_dump>        if not hasattr(inmsg, 'subject'):
        nmsg.subject = "####No subject####"

        logging.info("Received a message from: " + inmsg.sender +
                    ", to " + inmsg.to + ", subject: " + inmsg.subject)
        # now make a message object that can be submitted to GAE
        oumsg = mail.EmailMessage()


        
        oumsg.sender = MailRedirector.sender
        # TODO distinguish between error messages and potential loop/spoof.
        inmsg_email_address = email.utils.parseaddr(inmsg.sender)[1]
        my_email_address = email.utils.parseaddr(MailRedirector.sender)[1]
        if inmsg_email_address == my_email_address:
            logging.error("Oops. loop/err/spoof? sender: " + inmsg.sender +
                "subject: " + inmsg.subject + " at date: " + inmsg.date)
            return


        # compute the address to forward to    

        oumsg.to = config.OWNER_MAIL_ID
        # at least we are allowed to set an arbitrary subject :)
        oumsg.subject = inmsg.subject

        # gather up the plain text parts of the incoming email
        # and cat them together. 
        body = None

        for plaintext in inmsg.bodies(content_type='text/plain'):
            if body == None:
                body = "####Original sender: " + inmsg.sender + " and recipient: " + inmsg.to + " #####\n\n"
            body = body + plaintext[1].decode()

        if body == None:
            oumsg.body = "####Original email had no body text.####"
        else:
            oumsg.body = body

        # do similar things as plaintext for the html parts.
        html = None
        for htmlpart in inmsg.bodies(content_type='text/html'):
            if html == None:
                html = "<P style=\"color: red\">Original sender: " + cgi.escape(inmsg.sender) + " and recipient: " + cgi.escape(inmsg.to) + "<br></br><br></br></p>"
            html = html + htmlpart[1].decode()


        # corner case: if no html in original, dont put one in new
        if html != None:
            oumsg.html = html
        # TODO: attach the attachments.
        logging.info("Sending message to: " + oumsg.to)
        # queue it for sending
        oumsg.send()

        return
application = webapp.WSGIApplication([MailRedirector.mapping()], debug=True )