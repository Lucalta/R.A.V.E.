import json

def getUsers():
	with (open('{sitepath}/html/data/userData', 'r')) as x:
		dict = json.loads(x.read())
	return dict
	
def getSessions():
	with (open('{sitepath}/html/data/sessionData', 'r')) as x:
		dict = json.loads(x.read())
	return dict

def setUsers(dict):
	json.dump(dict, open('{sitepath}/html/data/userData','w'))
	
def setSessions(dict):
	json.dump(dict, open('{sitepath}/html/data/sessionData','w'))