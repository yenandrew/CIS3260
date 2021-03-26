#Write a program that reads the following information and prints a payroll statement:
#Employee’s name (e.g., Smith)
#Number of hours worked in a week (e.g., 10)
#Hourly pay rate (e.g., 9.75)
#Federal tax withholding rate (e.g., 20%)
#State tax withholding rate (e.g., 9%)

name=input("Enter employee's name: ")

hour=int(input("Enter number of hours worked in a week: "))

rate=float(input("Enter hourly pay rate (onit dollar sign): "))

Ftax=float(input("Enter federal tax withholding rate (omit percent sign): "))

Stax=float(input("Enter state tax withholding rate (omit percent sign): "))

pay=(hour*rate)

Fholding=pay*Ftax/100

Sholding=pay*Stax/100

TotalD=Fholding+Sholding

NetP=pay-TotalD

print("Employee Name: "+str(name))

print("Hour Worked: "+str(hour))

print("Pay Rate: $"+str(rate))

print("Gross Pay: $"+str(pay))

print("Deductions:")

print("\tFederal Withholding("+str(Ftax)+"%): $"+str(Fholding))

print("\tState Withholding("+str(Stax)+"%): $"+str(Sholding))

print("\tTotal Deduction: $"+str(TotalD))

print("Net Pay: $"+str(NetP))