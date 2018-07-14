import json

def getHead(page, sessionID):
	with (open('{sitepath}/html/data/sessionData', 'r')) as x:
		dict = json.loads(x.read())
	user = "anonymous"
	if sessionID != '0':
		user = dict["%s" % sessionID]
	with open('{sitepath}/html/html/head.template', 'r') as content_file:
		return content_file.read().replace("$pageparameter", page).replace("$userparameter", user);
		
def getHeader():
	with open('{sitepath}/html/html/header.template', 'r') as content_file:
		return content_file.read()
		
def getFooter():
	with open('{sitepath}/html/html/footer.template', 'r') as content_file:
		return content_file.read()
		
def get404():
	with open('{sitepath}/html/html/404.template', 'r') as content_file:
		return content_file.read()
		
def getHome():
	with open('{sitepath}/html/html/home.template', 'r') as content_file:
		return content_file.read()
		
def getLogin():
	with open('{sitepath}/html/html/login.template', 'r') as content_file:
		return content_file.read()