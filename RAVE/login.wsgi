# -*- coding: utf-8 -*-
import urllib
import sys
import json
import uuid

sys.path.append("{sitepath}/html/python")
from loadTemplates import *
from loadCookies import *
from loadParameters import *
from dictionaryManager import *

def application (environ, start_response):

	response_headers = []

	query = loadParameters(environ)
	postQuery = loadPostParameters(environ)
	cookies = loadCookies(environ)
	method = environ['REQUEST_METHOD']
	userData = getUsers()
	
	sessionID = '0'
	if 'sid' in cookies:
		sessionID = cookies['sid']
	
	
	message = ""
	
	
	if "action" in query and method == "POST":
		if (query["action"][0]) == "register":
			if postQuery['username'][0] in userData or postQuery['username'][0] == 'anonymous':
				message = "<h4>Registration unsuccessful</h4>"
			else:
				userData[postQuery['username'][0]] = postQuery['password'][0]
				setUsers(userData)
				message = "<h4>Registration successful</h4>"		
	
		elif (query["action"][0]) == "login":
			message = "<h4>Login unsuccessful</h4>"
			if postQuery['username'][0] in userData:
				if userData[postQuery['username'][0]] == postQuery['password'][0]:
					message = "<h4>Login successful</h4>"
					sessionData = getSessions()
					while True:
						sid = uuid.uuid4()
						if sid != 0 and not sid in sessionData:
							break
					sessionData["%s" % sid] = postQuery['username'][0]	
					setSessions(sessionData)
					response_headers.append(("Set-Cookie","sid=%s" % sid))
					sessionID = sid
						
		elif (query["action"][0]) == "logout":
			response_headers.append(("Set-Cookie","sid=0"))
			sessionID = '0'
			
		
	response_body = "<!DOCTYPE html>\n<html>" + getHead("index.html", sessionID) + getHeader() + get404() + message + getLogin() + getFooter() + "</html>"
	response_headers.append(('Content-Type', 'text/html'))
	response_headers.append(('Content-Length', str(len(response_body))))
	status = '200 OK'
	start_response(status, response_headers)
	return [response_body.encode()]
