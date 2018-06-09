#!/usr/bin/python2

import  cgi,cgitb
import  commands,time
cgitb.enable()

print "Content-type:text/html"
print ""
#  taking date from apache and storing into web variable 
web=cgi.FieldStorage()

# taking user name
user=web.getvalue('u')
# taking password 
password=web.getvalue('p')

if  user  ==   'root' and password ==  '123' :
	print "<a href='http://192.168.10.216/service.html'>"
	print   "Click here to GO Hadoop SErvices"
	print  "</a>"
else :
	print  "wrong values redirecting to login page"
	time.sleep(2)
	print "<a href='http://192.168.10.216/login.html'>"
	print   "Click here to try again"
	print  "</a>"
	
