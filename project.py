import mechanize
import sys
import getpass

browser = mechanize.Browser()

def login(username, password):
	url = "https://auth.vt.edu/login?service=https%3A%2F%2Fscholar.vt.edu%2Fsakai-login-tool%2Fcontainer"
	browser.open(url)
	browser.select_form(nr = 0)
	browser.form['username'] = username
	browser.form['password'] = password
	browser.submit()
	if browser.response().info().getheader('Set-Cookie'):
		#login is successful when cookie is set
		print("Login successful")
		return True
	else:
		#cookie will be empty when login fail 
		print("Invalid username or password")
		return False


def main():
	isLogged = False
	
	while not isLogged:
		#get username and password from user and attempt to login
		print("Enter username and password: ")
		print "Username: ",
		username = str.strip(sys.stdin.readline())
		password = getpass.getpass()
		isLogged = login(username, password)
	
	#if isLogged:
	#	print browser.response().read();
	

if __name__ ==  "__main__":
	main()
