overdue_days = int(input("How many days is the book overdue: "))
fine = 0 

if overdue_days <= 5:
    fine =  overdue_days * 1
elif overdue_days <=10:
    fine = overdue_days * 2
else:
    fine = overdue_days * 5

print(fine)