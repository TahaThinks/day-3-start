print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    person_age = int(input("How old are you? "))
    if person_age < 12:
        print("$5")
    elif person_age > 12 and person_age <= 18:
        print("$7")
    else:
        print("$12")
else:
    print("Sorry, You have to grow taller before you can ride.")
