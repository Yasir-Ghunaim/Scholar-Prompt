import urllib
import urllib2
import cookielib
import sys

def login(username, password):
	url = "https://auth.vt.edu/login?service=https%3A%2F%2Fscholar.vt.edu%2Fsakai-login-tool%2Fcontainer"

	#Enable cookies 
	jar = cookielib.FileCookieJar("cookies")
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(jar))

	#HTTP GET to grab lt parameter that is used in logging in
	response = opener.open(url).read()
	#extract lt
	lt = response.split("\"lt\" value=\"")[1].split("\"")[0]
	#grab cookie from response

	data = urllib.urlencode({'username' : str(username).strip(),
							 'password' : str(password).strip(),
							 'lt' : lt,
							 'execution' : 'e1s1',
							 '_eventId' : 'submit',
							 'submit' : '_submit'})
	response = opener.open(url,data)
	if not response.info().getheader('Set-Cookie'):
		print("Invalid username or password")
	else:
		print("Login successful")


loginInfo = sys.stdin.readline()
username = loginInfo.split(" ")[0]
password = loginInfo.split(" ")[1]
login(username, password)
