from task101 import daily_details
from summary import summary

def auth():
	try:
		file = open('text.txt','r')
		read = file.readlines()
		line_number =[]
	except FileNotFoundErrer:
		print("Error : File Not Found")
	else:
		file.close()

		for line in read:
			if line[-1] == '\n':
				line_number.append(line[:-1])

			else:
				line_number.append(line)

		username = str(line_number[0])
		password = str(line_number[1])

		uname = input("Enter username: ")
		pwd = input("Enter password: ")

		if uname == username and pwd == password:
			option=0
			while True:
				print(msg)
				option = int(input(" Select an Option : "))
				if option == 1:
					summary()
				elif option == 2:
					daily_details()
					print("Data Added Successfully!!!")
				elif option == 3:
					print("Program Finished!!!")
				else:
					print("Invalid Option")

		else:
			print("Invalid Username or Password")
       
msg="""
		01. Show Previous Data Summary.
		02. Add New Income Expense.
		03. Finished the program.
		"""

auth();
