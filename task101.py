import datetime as dt

def daily_details():
	
	current = dt.datetime.now()
	s=current.strftime("%A %b %d %Y")
	print(s)
	
	income = float(input("Income : "))
	expense = float(input("Expense : "))
	
	fincome = open("Income.txt", 'a')
	fincome.write(str(income)+ "\n")
	fincome.close()
	
	fexpense = open("Expense.txt", 'a')
	fexpense.write(str(expense)+ "\n")
	fexpense.close()	
	
	
