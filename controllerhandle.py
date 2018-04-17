#!/usr/bin/env python

import webapp2
import urllib2,json
import jinja2
import os
import yaml
from google.appengine.api import mail
from google.appengine.api import users
import config

JINJA_ENVIRONMENT = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
	extensions=['jinja2.ext.autoescape'],
	autoescape=True)




class MainHandler(webapp2.RequestHandler):

	def post(self):
		##Gets the subject and msg contents
		_response={}
		

		_subject=self.request.get('subject')
		_message = self.request.get('message')
		_sender_mail_id = self.request.get('email')
		
		self.send_mail(_subject, _message, _sender_mail_id)
		self.response.set_status(201,"sucess")
		self.response.headers.add_header('Content-Type', 'application/json')
		self.response.write(json.dumps({"status": True, "message": "Sent Mail"}))
		
		
		
		



	def send_mail(self, subject, messagebody, user):
		""" Sends mail to both the parties """
		
		sender = "\""+config.OWNER_NAME+"\" <"+config.WEBSITE_MAIL_SERVER+">"
		message = mail.EmailMessage()

		############################ Copy of contnet to personal mail id ###################
		message.sender = sender
		
		message.to = config.OWNER_MAIL_ID
		message.subject = subject
		message.body = """Sender: """+str(user)+"""
		Content:->
		"""+messagebody;
		message.send()
		###################################################################################

		
		########################## Notification Mail to Sender ############################
		_user_name = user.split("@")[0]

		message.sender = sender
		message.to = user
		message.subject = config.MAIL_SIGNATURE['SUBJECT'].format(config.OWNER_NAME)
		message.body = config.MAIL_SIGNATURE['BODY'].format(_user_name, config.OWNER_NAME)
		message.send()
		###################################################################################
		


	##Loads the template		
	def get(self):
		
		template_values = {}
		self.display(template_values);

		
	def display(self,template_values):

		template = JINJA_ENVIRONMENT.get_template('static/index.html')
		self.response.write(template.render(template_values))
