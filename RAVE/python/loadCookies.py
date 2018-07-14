def loadCookies(environ):
	res = {}
	if 'HTTP_COOKIE' in environ:
		cookies = environ['HTTP_COOKIE']
		cookies = cookies.split('; ')

		for value in cookies:
			value = value.split('=')
			res[value[0]] = value[1]
	return res