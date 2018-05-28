#!/usr/bin/python2

import  cgi
import  commands,time
print  "Content-type:text/html"
print   ""

web_data=cgi.FieldStorage()

out=web_data.getvalue('c')
#  running  os 



for  i in range(int(out)):
	print  "<pre>"
	print  "creating  "+str(i)+"  virtual servers in every second......!@!"
	print  commands.getoutput('sudo qemu-img create -f qcow2 -b /var/lib/libvirt/images/rhvmdnd.qcow2   /var/lib/libvirt/images/ashudn'+str(i)+'.qcow2')
	print time.sleep(1)
	print "</pre>"
	print  "<br/>"*5
	
	print  "<p>"
	print  "starting  created  vms plz wait......."
	
	print  commands.getoutput('sudo  virt-install --ram 512 --vcpu 1 --disk path=/var/lib/libvirt/images/ashudn'+str(i)+'.qcow2     --import  --name ashudn'+str(i)+'  &>/dev/null  &')
	time.sleep(1)
	print  "</p>"











