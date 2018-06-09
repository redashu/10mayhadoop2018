#!/usr/bin/python2

import  cgi,cgitb
import  commands,time
cgitb.enable()

print "Content-type:text/html"
print ""
#  taking date from apache and storing into web variable 
web=cgi.FieldStorage()
#  getting hadoop version
h_version=web.getvalue('h1')

# getting  cluster size 
size=web.getvalue('nm')
#  getting  start service type
s_type=web.getvalue('ss')

if  h_version ==  'hv2'  and size  ==  '2' and  s_type ==  'od' :

	print  "only starting  two vms only"
	print  commands.getoutput('sudo  virsh  start  h2dn1')
	time.sleep(1)
	print  commands.getoutput('sudo  virsh  start  h2dn2')
	print   "plz wait for  30 seconds"
	time.sleep(30)
	print  commands.getoutput('sudo ansible-playbook  /etc/ansible/playbooks/n2dno.yml')
	

else :
	print   "sorry  put only correct values"











	
