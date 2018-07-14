import json
import urlparse

def loadParameters(environ):
	query = environ['QUERY_STRING']
	return urlparse.parse_qs(query)
	
def loadPostParameters(environ):
	if 'CONTENT_LENGTH' in environ:
		query = environ['wsgi.input'].read(int(environ['CONTENT_LENGTH']))
		return urlparse.parse_qs(query)
	else:
		return {}
		
def loadPostPayload(environ):
	if 'CONTENT_LENGTH' in environ:
		query = environ['wsgi.input'].read(int(environ['CONTENT_LENGTH']))
		return json.loads(query)
	else:
		return {}