o=1
while [ $o -eq 1 ]
do
	echo -e "Enter the option:: \n"
	echo -e "1.faculty \n2.student \n"
	read a
	if [ $a -eq 1 ]
	then
		echo -e "Enter the name of the faculty::"
		read b
		python search.py $b
	elif [ $a -eq 2 ]
	then
		echo -e "Enter the name of the student::"
		read b
		python searchstudent.py $b
	else 
		echo -e "Wrong input!!"
	fi
	echo ' 	      ******************DONE*******************'
done
