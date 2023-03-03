# Write a small program to ask for a name and an age.
name = input("What is your name? ")
age = int(input("Please enter your age: "))
# When both values have been entered, check if the person is the right age to go
# on an 18-30 holiday(they must be over 18 and under 31).
if 18 <= age < 31:
    # If they are, welcome them to the holiday, otherwise print a polite message
    # refusing them entry.
    print("Hello {}, welcome to the holiday".format(name))
else:
    print("Sorry {}, you are {} years old and not meet the criteria for the holiday".format(name, age))

# Our programs expect valid input.