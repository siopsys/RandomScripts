#!/usr/bin/env python3

#cost calculator for wedding venues

venuename = input("Please enter the venue name: ")

def food(guests,pph):
    global fprice 
    fprice = int(pph) * int(guests)
    return fprice

'''cost for food, takes the number of guests and multiples by the price per head. The two totals are then added together to give
the total and a breakdown saved to a file
'''
try:
    guests = input("Please enter the number of guests: ")
    pph = input("Please enter the price per head: ")
    rental = int(input("please enter the price of the venue hire: "))
    print("food is " + str(food(guests,pph)))
    print("venue hire is " + str(rental))
except ValueError: 
    print("One of the values was not a number, please try again")

total = rental + fprice
print("The total is " + str(total))


