def temp_check(temp_type):
    valid = False
    while not valid:
        try:
            if temp_type == "celsius":
                lower_limit = -273
                response = int(input("Celsius: "))
                if response > lower_limit:
                    valid = True
                else:
                    print("Please enter a number above {}.".format(lower_limit))
            elif temp_type == "fahrenheit":
                lower_limit = -459
                response = int(input("Fahrenheit: "))
                if response > lower_limit:
                    valid = True
                else:
                    print("Please enter a number above {}.".format(lower_limit))
            else:
                print("Error: valid temperature unit not received")
                return 0

        except ValueError:
            print("Please enter a number above {}.".format(lower_limit))

    return response

# main routine

for item in range(5):
    type_temp = input("What type of temperature? ")
    temp_check(type_temp)
    print()