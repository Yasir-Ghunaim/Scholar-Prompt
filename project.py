import urllib
import urllib2
import cookielib
import sys

#Given a username and a password this function will attempt to login in to Scholar
def login(opener, jar, username, password):
	url = "https://auth.vt.edu/login?service=https%3A%2F%2Fscholar.vt.edu%2Fsakai-login-tool%2Fcontainer"

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
	if response.info().getheader('Set-Cookie'):
		#login is successful when cookie is set
		print("Login successful")
		return True
	else:
		#cookie will be empty when login fail 
		print("Invalid username or password\n")
		return False

def main():
	isLogged = False
	
	while not isLogged:
		#Enable cookies
		global jar, opener 
		jar = cookielib.FileCookieJar("cookies")
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(jar))
		
		#get username and password from user and attempt to login
		print("Enter username and password: ")
		loginInfo = sys.stdin.readline()
		username = loginInfo.split(" ")[0]
		password = loginInfo.split(" ")[1]
		isLogged = login(opener, jar, username, password)
	
	
	
	

#This is python style to call main function
#basically when program start the defined varible __name__
#will hold the value "__main__" in which case we call our function main
if __name__ ==  "__main__":
	main()
