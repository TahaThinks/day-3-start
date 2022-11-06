print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    #Cost per Age
    person_age = int(input("How old are you? "))
    cost_per_age = 0
    if person_age < 12:
        print("Child Tickets are $5.")
        cost_per_age = 5
    elif person_age <= 18:
        print("Youth Tickets are $7.")
        cost_per_age = 7
    else:
        print("Adult Tickets are $12.")
        cost_per_age = 12
    
    #Cost with Picture
    picture = input("Do you want a picture taken? Y/N ")
    total_cost = cost_per_age
    if picture == "Y":
        print("Extra +$3")
        total_cost += 3
    else:
        print("No picture then")
   
    #Total Ticket Charge
    print(f"Total Cost of Ticket is ${total_cost}")
    
else:
    print("Sorry, You have to grow taller before you can ride.")
