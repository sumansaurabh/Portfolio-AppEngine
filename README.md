The aim of this project is to allow user to host a personal 
portfolio in Google App Engine Server in Python just with 
basic knowledge of app engine and python.
Copyright (C) 2014  Suman Saurabh
                    info@suman-saurabh.appspot.com

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software


My Portfolio
=============

## Introduction
The aim of this project is to allow user to host a personal portfolio in Google App Engine Server in Python just without any knowledge of app engine and python. 

## Features
1. Allows you to host any type of static website content on app engine server. For dynamic website, good knowledge of app engine and python is required. It's not even better to host a paid website in Google app engine when other better services are available.

2. App-engine has mail forwarding facility so a custom email address can be set up to send and recieve emails. Form submisson page in the /templates/index.html submits the query using the 'Google email address' signed in by visitor. On submitting the query, a computerised notification email sent will be sent to the visitor and query details will be sent to owner.

3. It doesn't ask for credit card while all the major hosting asks for credit card info, even though they will charge from it.

## Customization
Customize your app engine to suit your profile. Nothing more is required, just change the mailing details from the files shown:
```

	app.yaml -> this file is required for running app engine
		'application: games-2024' change it to your website name.
		'url: /_ah/mail/info@.*games-2024\.appspotmail\.com' replace 'games-2024' to your website name.

	config.py -> Update your details
    
 ```


## Workflow
1. Get the basic Google app engine setup - Python 2.7 framework on the system.
2. Create a server in http://appengine.google.com/ and provide the website name, this name should be same as in app.yaml file 
	eg. server name is saucy-salamander
	write the same in app.yaml file
	application: saucy-salamander

3. Run the command: ' appcfg.py --oauth2 update <folder_location> ' to deploy on google app engine server
4. To deploy on localhost: 'dev_appserver.py <folder_location>'

