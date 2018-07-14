# -*- coding: utf-8 -*-
import urllib
import sys
import json
import uuid
import distutils.dir_util
import os

sys.path.append("{sitepath}/html/python")
from loadTemplates import *
from loadCookies import *
from loadParameters import *
from dictionaryManager import *

def loadAnnotatorData(page, id):
	with (open('{sitepath}/html/data/annotator/' + page + '/' + id, 'r')) as x:
		return json.loads(x.read())

def saveAnnotatorData(page, id, data):
	path = '{sitepath}/html/data/annotator/' + page
	distutils.dir_util.mkpath(path)		
	json.dump(data, open(path + '/' + id,'w'))

		
def application (environ, start_response):

	response_headers = []

	query = loadParameters(environ)
	postQuery = loadPostPayload(environ)
	cookies = loadCookies(environ)
	method = environ['REQUEST_METHOD']
	userData = getUsers()
	
	sessionID = '0'
	if 'sid' in cookies:
		sessionID = cookies['sid']
		
	page = "index.html"
	if "page" in query:
		page = urllib.quote(query ["page"][0])
		
	with (open('{sitepath}/html/data/sessionData', 'r')) as x:
		dict = json.loads(x.read())
	user = "anonymous"
	if sessionID != '0':
		user = dict["%s" % sessionID]
		
	
	status = '200 OK'
	
	response_body = query["page"][0]
	
	if method == "POST":
		id = uuid.uuid4()
		postQuery['id'] = str(id)
		saveAnnotatorData(page, str(id), postQuery)
		response_body = json.dumps(postQuery)
	elif method == "PUT":
		id = page.split('/')[1]
		page = page.split('/')[0]
		saveAnnotatorData(page, str(id), postQuery)
		response_body = json.dumps(postQuery)
	elif method == "GET":
		try:
			total = 0
			s = '{"rows":['
			for filename in os.listdir('{sitepath}/html/data/annotator/' + page):
				file = loadAnnotatorData(page, filename)
				if file['permissions']['read'] == [] or user in file['permissions']['read']:
					total += 1
					s += ','
					s += json.dumps(file)					
			s += "]"
			s = s.replace(',','',1)
			s += ',"total":' + str(total) + "}"
			response_body = s
		except:
			response_body = "[]"
	elif method == "DELETE":
		id = page.split('/')[1]
		page = page.split('/')[0]
		try:
			os.remove('{sitepath}/html/data/annotator/' + page + '/' + id)
		except OSError:
			pass
		status = '204 NO CONTENT'
			
	
			
		
	response_headers.append(('Content-Type', 'application/json'))
	response_headers.append(('Content-Length', str(len(response_body))))
	
	start_response(status, response_headers)
	return [response_body.encode()]
