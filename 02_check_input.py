def temp_check(temp_type):
    valid = False
    while not valid:
        try:
            if temp_type == "celsius":
                response = int(input("Celsius: "))
                lower_limit = -273
                if response > lower_limit:
                    valid = True
                else:
                    print("Please enter a number above {}.".format(lower_limit))
            else:
                response = int(input("Fahrenheit: "))
                lower_limit = -459
                if response > lower_limit:
                    valid = True
                else:
                    print("Please enter a number above {}.".format(lower_limit))

        except ValueError:
            print("Please enter a number above {}.".format(lower_limit))

    return response

# main routine

for item in range:
    type_temp = input("What type of temperature? ")
    temp_check(type_temp)