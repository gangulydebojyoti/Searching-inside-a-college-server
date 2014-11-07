import pickle
import os
tdic={}
while True:
	ch=input( 'enter the optiton: 1.Faculty 2.Student \n')
	if(ch==1):
		print '1.Enter new faculty name with subjects'
		print '2.Enter new faculty name with department'
		print '3.Enter new faculty name with their projects'
		##print '4.Update faculty name with subjects'
		##print '5.Update faculty name with department'
		##print '6.Update faculty name with their projects'
		ch1=input('Enter a option : \n')
		if(ch1==1):
			f=open('facultysubject.txt','a')
			f.close()
			f=open('facultysubject.txt','r')
			if (f.read()==''):
				f.close()
				f=open('facultysubject.txt','a')
				pickle.dump(tdic,f)
				f.close()
			f=open('facultysubject.txt','r')
			new=raw_input("Enter the name of faculty:: \n")
			new1=raw_input("Enter subject:: \n")
			new_dict={}
			new_dict=pickle.load(f)
			f.close()
			os.remove('facultysubject.txt')
			f=open('facultysubject.txt','a')
			##new_dict={}
			new_dict[new]=new1
			pickle.dump(new_dict,f)
			f.close()
		elif(ch1==2):
			f=open('facultydept.txt','a')
			f.close()
			f=open('facultydept.txt','r')
			if (f.read()==''):
				f.close()
				f=open('facultydept.txt','a')
				pickle.dump(tdic,f)
				f.close()
			f=open('facultydept.txt','r')
			new=raw_input("Enter the name of faculty:: \n")
			new1=raw_input("Enter the department:: \n")
			new_dict={}
			new_dict=pickle.load(f)
			os.remove('facultydept.txt')
			f.close()
			f=open('facultydept.txt','a')
			##new_dict={}
			new_dict[new]=new1
			pickle.dump(new_dict,f)
			f.close()
		elif(ch1==3):
			f=open('facultyprojects.txt','a')
			f.close()
			f=open('facultyprojects.txt','r')
			if (f.read()==''):
				f.close()
				f=open('facultyprojects.txt','a')
				pickle.dump(tdic,f)
				f.close()
			f=open('facultyprojects.txt','r')
			new=raw_input("Enter the name of faculty:: \n")
			new1=raw_input("Enter list of projects:: \n")
			new_dict={}
			new_dict=pickle.load(f)
			f.close()
			os.remove('facultyprojects.txt')
			f=open('facultyprojects.txt','a')
			##new_dict={}
			new_dict[new]=new1
			pickle.dump(new_dict,f)
			f.close()
		print 'Succesfully saved!!!'
	elif(ch==2):
		print '1.Enter new student name with marks'
		print '2.Enter new student name with department'
		print '3.Enter new student name with their projects'
		ch2=input("Enter a option :: \n")
		if(ch2==1):
			f=open('studentmarks.txt','a')
			f.close()
			f=open('studentmarks.txt','r')
			if (f.read()==''):
				f.close()
				f=open('studentmarks.txt','a')
				pickle.dump(tdic,f)
				f.close()
			f=open('studentmarks.txt','r')
			new=raw_input("Enter the name of the student:: \n")
			new1=raw_input("Enter marks:: \n")
			new_dict={}
			new_dict=pickle.load(f)
			f.close()
			os.remove('studentmarks.txt')
			f=open('studentmarks.txt','a')
			##new_dict={}
			new_dict[new]=new1
			pickle.dump(new_dict,f)
			f.close()
		if(ch2==2):
			f=open('studentdept.txt','a')
			f.close()
			f=open('studentdept.txt','r')			
			if (f.read()==''):
				f.close()
				f=open('studentdept.txt','a')
				pickle.dump(tdic,f)
				f.close()
			f=open('studentdept.txt','r')
			new=raw_input("Enter the name of the student:: \n")
			new1=raw_input("Enter department:: \n")
			new_dict={}
			new_dict=pickle.load(f)
			f.close()
			os.remove('studentdept.txt')
			f=open('studentdept.txt','a')
			##new_dict={}
			new_dict[new]=new1
			pickle.dump(new_dict,f)
			f.close()
		if(ch2==3):
			f=open('studentproject.txt','a')
			f.close()
			f=open('studentproject.txt','r')
			if (f.read()==''):
				f.close()
				f=open('studentproject.txt','a')
				pickle.dump(tdic,f)
				f.close()
			f=open('studentproject.txt','r')
			new=raw_input("Enter the name of the student:: \n")
			new1=raw_input("Enter project:: \n")
			new_dict={}
			new_dict=pickle.load(f)
			f.close()
			os.remove('studentproject.txt')
			f=open('studentproject.txt','a')
			##new_dict={}
			new_dict[new]=new1
			pickle.dump(new_dict,f)
			f.close()
		print 'Successfully saved'
