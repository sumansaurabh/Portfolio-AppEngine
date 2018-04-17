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


def jsonify_response(func):
	""" Make the response REST compatible """

	def response_decorator(*args, **kw):

		_post_fn=func(*args, **kw)
		try:
			_origin = args[0].request.headers['Origin']
		except:
			_origin = settings.ORIGIN_SITE_NAME

		args[0].response.headers.add_header('Content-Type', 'application/json')

		if _post_fn:
			args[0].response.write(json.dumps(_post_fn))
		else:
			args[0].response.write({"status": 400, "message": "Invalid request"})

	return response_decorator

class MainHandler(webapp2.RequestHandler):

	@jsonify_response	
	def post(self):
		##Gets the subject and msg contents
		_response={}
		

		# _body = self.request.body.encode("utf-8")

		# try:
		# 	_json = json.loads(_body,encoding="utf-8")
		# except:
		# 	_json = None
		# 	self.abort(400)

		# if _json:
		# 	self.response.set_status(201,"sucess")
		# 	_response["status"]=True
		# 	_response["message"]="Mail Sent"

		_subject=self.request.get('subject')
		_message = self.request.get('message')
		_sender_mail_id = self.request.get('email')

		print(" ------------------------- ")
		print(_subject)
		print(_message)
		print(_sender_mail_id)

		# _message = _json['message']
		# _subject = _json['subject']
		# _sender_mail_id = _json['email']
		
		self.send_mail(_subject, _message, _sender_mail_id);
		
		return _response
		
		
		



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

		template = JINJA_ENVIRONMENT.get_template('templates/index.html')
		self.response.write(template.render(template_values))
