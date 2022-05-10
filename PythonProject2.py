# A program to calculate the cost of a rental with Edsel Car Rental Company
# Author : Darla Ward
# Date Completed : 05-10-2022

rentalPricePerDay = 35.00
pricePerKM = .10
HST = 0.15

customerName = input("Enter Customer Name: ")
phoneNumber = input("Enter Phone Number: ")
daysRented = int(input("Enter the amount of days the car was rented: "))
beforeMileage = int(input("Enter the mileage before renting: "))
afterMileage = int(input("Enter the mileage upon return: "))

travelledKM = afterMileage - beforeMileage
rentalCost = daysRented * rentalPricePerDay
mileageCost = travelledKM * pricePerKM
rentalMileageCost = rentalCost + mileageCost
HSTOnRentalCost = rentalCost * HST
totalCost = rentalMileageCost + HSTOnRentalCost

print()
print("Customer Name:   ", customerName)
print("Phone Number:    ", phoneNumber)
print()
print("Days Rented:             ", daysRented)
print("Mileage before renting:  ", beforeMileage)
print("Mileage after renting:   ", afterMileage)
print("Mileage Travelled:       ", travelledKM)
print()
print("Price of car rental: $ {:.2f}".format(rentalCost))
print("Mileage Fee:         $ {:.2f}".format(mileageCost))
print("Rental Subtotal:     $ {:.2f}".format(rentalMileageCost))
print("HST on Rental:       $ {:.2f}".format(HSTOnRentalCost))
print()
print("Total Cost:          $ {:.2f}".format(totalCost))
