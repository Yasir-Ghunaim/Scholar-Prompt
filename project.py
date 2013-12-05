import urllib
import urllib2
import cookielib
url = "https://auth.vt.edu/login?service=https%3A%2F%2Fwebapps.banner.vt.edu%2Fbanner-cas-prod%2Fauthorized%2Fbanner%2FSelfService%3Bjsessionid%3D21709F288B978AFC233DEA9658850C04.mt-prod-1"

#Enable cookies 
jar = cookielib.FileCookieJar("cookies")
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(jar))

#HTTP GET to grab lt parameter that is used in logging in
response = opener.open(url).read()
#extract lt
lt = response.split("\"lt\" value=\"")[1].split("\"")[0]


#data = urllib.urlencode({'username' : 'joe',
#                         'password' : 'joe',
#                         'lt' : lt,
#                         'execution' : 'e1s1',
#                         '_eventId' : 'submit',
#                         'submit' : '_submit'})
print(lt)
print(response)
