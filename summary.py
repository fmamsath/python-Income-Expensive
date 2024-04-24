def summary():
	total_income_records = 0
	total_income = 0
	with open("income.txt",'r') as income_file:
		for a in income_file:
			total_income_records = total_income_records+1
			
	f = open("income.txt",'r')
	read = f.readlines()
	line_number =[]
	
	for line in read:
		if line[-1] == '\n':
			line_number.append(line[:-1])
			
		else:
			line_number.append(line)
			
	for a in range(0, total_income_records,1):
		total_income = total_income+float(line_number[a])
		
	print("Total number of records in income_file : "+ str(total_income_records) +"\n")
	print("Total_income : " + str(total_income) +"\n")
	avg = total_income/total_income_records;
	print("Average income : " + str(avg) +"\n\n")
	
	total_expense_records = 0
	total_expense = 0
	lines_expense = []
	with open("expense.txt",'r') as expense_file:
		for c in expense_file:
			total_expense_records = total_expense_records+1
			
	f1 = open("expense.txt",'r')
	read1 = f1.readlines()
	line_number1 = []
	
	for line1 in read1:
		if line1[-1] == '\n':
			line_number1.append(line1[:-1])
			
		else:
			line_number1.append(line1)
			
	for c in range(0, total_expense_records, 1):
		total_expense = total_expense+float(line_number1[c])
		
	print("Total number of recorts in expense_file : " + str(total_expense_records) +"\n")
	print("Total_expense : " + str(total_income) +"\n")
	avg_expense = total_expense/total_expense_records;
	print("Average Expense : " + str(avg_expense) +"\n\n")
	
	profit = total_income-total_expense;
	
	if profit > 0 :
		print("There is a profit : "+ str(profit))
	elif profit < 0 :
		print("There is a loss : "+ str(profit))
	else:
		print("There is no profit or loss")
	
	