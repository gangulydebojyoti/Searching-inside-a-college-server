import time
import os 
import sys
import pickle
a=sys.argv[1]
q=open('facultysubject.txt','r')
w=open('facultydept.txt','r')
e=open('facultyprojects.txt','r')
dic1={}
dic2={}
dic3={}
dic1=pickle.load(q)
##print dic1.keys()
dic2=pickle.load(w)
##print dic2.keys()
dic3=pickle.load(e)
#3print dic3.keys()
print 'NAME OF FACULTY: '+a+'\n'
print 'DETAILS AVAILABLE:- '+'\n'
print '			**************SEARACHING***************'
time.sleep(2)
if dic1.has_key(a)==True :
	var1=dic1[a]
	##print var1 
	var ='SUBJECT OF FACULTY: '+var1
	print var+'\n' 
if dic2.has_key(a)==True :
	var2=dic2[a]
	var3='DEPT. OF FACULTY: '+var2
	print var3+'\n'
if dic3.has_key(a)==True :
	var4=dic3[a]
	var5='ONGOING PROJECTS: '+var4
	print var5+'\n'

if dic1.has_key(a)==False and dic2.has_key(a)==False and dic3.has_key(a)==False :
	print '			**************SEARACHING***************'
	time.sleep(2)
	print '			........Sorry!No Matches Found.........'
	


