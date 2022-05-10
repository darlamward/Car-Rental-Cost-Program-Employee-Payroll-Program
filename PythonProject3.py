# A program to help calculate Widgets Inc. employee payroll.
# Author: Darla Ward
# Date Completed : 05-10-2022

hourlyWage = 17.50
widgetCommission = .35
incomeTax = .21
CPP = 0.0495
EI = 0.016
unionDues = 15.00

employeeName = input("Enter employee name: ")
hoursWorked = float(input("Enter the amount of hours worked: "))
widgetsProducedMonday = int(input("Enter the number of widgets produced on Monday: "))
widgetsProducedTuesday = int(input("Enter the number of widgets produced on Tuesday: "))
widgetsProducedWednesday = int(input("Enter the number of widgets produced on Wednesday: "))
widgetsProducedThursday = int(input("Enter the number of widgets produced on Thursday: "))
widgetsProducedFriday = int(input("Enter the number of widgets produced on Friday: "))

totalWidgetsProduced = (widgetsProducedMonday + widgetsProducedTuesday + widgetsProducedWednesday
                        + widgetsProducedThursday + widgetsProducedFriday)
commission = totalWidgetsProduced * widgetCommission
regularPay = hoursWorked * hourlyWage
grossPay = regularPay + commission

incomeTaxOnPay = grossPay * incomeTax
CPPOnPay = grossPay * CPP
EIOnPay = grossPay * EI

totalDeductions = incomeTaxOnPay + CPPOnPay + EIOnPay + unionDues
netPay = grossPay - totalDeductions

print()
print()
print("Employee Name:          ", employeeName)
print("Number of Hours worked: ", hoursWorked)
print()
print("Number of widgets produced on Monday:    ", widgetsProducedMonday)
print("Number of widgets produced on Tuesday:   ", widgetsProducedTuesday)
print("Number of widgets produced on Wednesday: ", widgetsProducedWednesday)
print("Number of widgets produced on Thursday:  ", widgetsProducedThursday)
print("Number of widgets produced on Friday:    ", widgetsProducedFriday)
print("Total number of widgets produced:        ", totalWidgetsProduced)
print()
print("Regular Pay:       ${:,.2f}".format(regularPay))
print("Commission Earned: ${:,.2f}".format(commission))
print("Gross Pay:         ${:,.2f}".format(grossPay))
print()
print("Income Tax Deducted: ${:,.2f}".format(incomeTaxOnPay))
print("CPP Deducted:        ${:,.2f}".format(CPPOnPay))
print("EI Deducted:         ${:,.2f}".format(EIOnPay))
print("Union Dues Deducted: ${:,.2f}".format(unionDues))
print("Total Deductions:    ${:,.2f}".format(totalDeductions))
print()
print("Net Pay:             ${:,.2f}".format(netPay))
