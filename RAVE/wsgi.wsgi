# -*- coding: utf-8 -*-
import urllib
import sys

sys.path.append("{sitepath}/html/python")
from loadTemplates import *
from loadParameters import *
from loadCookies import *

def application (environ, start_response):
	
	dict = loadParameters(environ)
	cookies = loadCookies(environ)	
	sessionID = '0'
	if 'sid' in cookies:
		sessionID = cookies['sid']
	
	page = "index.html"
	if "page" in dict:
		page = urllib.quote(dict ["page"][0])
		
	
	home = ""
	if page == "index.html":
		home = getHome()
			
	response_body = "<!DOCTYPE html>\n<html>" + getHead(page, sessionID) + getHeader() + get404() + home + getFooter() + "</html>"
		
	status = '200 OK'
	response_headers = [
	('Content-Type', 'text/html'),
	('Content-Length', str(len(response_body)))
	]
	start_response(status, response_headers)
	return [response_body.encode()]
