# temperature checking function, takes a minimum value and makes sure
# number input is larger than min value
def temp_check(min_value):

    error = "Please enter a number larger than {}.".format(min_value)
    valid = False
    while not valid:
        try:
            response = float(input("Choose a number: "))

            if response < min_value:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

# main routine

for item in range(5):
    temp_check(-273)
    print()

for item in range(5):
    temp_check(-459)
