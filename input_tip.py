print("What is your total bill at the restaurant?")
bill = int(input())

tip = 0.15 * bill
two = 0.20 * bill
three = 0.00 * bill
total = bill + tip
twotwo = bill + two
threethree = bill + three

print(total)

print("What is your level of satisfaction with the service at the restaurant, return good, great or terrible ?")
satisfaction = input()

if satisfaction == "good" :
    print(total)
elif satisfaction == "great" :
    print(twotwo)

else:
    print(threethree)
