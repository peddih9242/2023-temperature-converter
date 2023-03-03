from datetime import date
import re


# if filename is blank, returns default name
# otherwise checks filename and either returns
# an error or returns the filename (with .txt extension)
def filename_maker(filename):

    # creates default filename
    # (YYYY_MM_DD_temperature_calculations)
    if filename == "":

        # set filename_ok to "" so we can see
        # default name for testing purposes
        filename_ok = ""
        date_part = get_date()
        filename = "{}_temperature_calculations".format(date_part)

    # checks filename has only a-z / A-Z / underscores
    else:
        filename_ok = check_filename(filename)

    if filename_ok == "":
        filename += ".txt"

    else:
        filename = filename_ok

    return filename


# retrieves date and creates DD_MM_YYYY string
def get_date():
    today = date.today()
    day = today.strftime("%d")
    month = today.strftime("%m")
    year = today.strftime("%Y")

    return "{}_{}_{}".format(day, month, year)


# checks that filename only contains letters,
# numbers and underscores. returns either "" if
# filename is ok or the problem if an error is found
def check_filename(filename):
    problem = ""

    # regular expression to check filename is valid
    valid_char = "[A-za-z0-9_]"

    # iterates through filename and checks each character
    for character in filename:
        if re.match(valid_char, character):
            continue

        elif character == " ":
            problem = "Sorry, no spaces allowed"

        else:
            problem = "Sorry, no {}'s allowed".format(character)
        break

    if problem != "":
        problem = "{}. Use letters / numbers / " \
                  "underscores only".format(problem)

    return problem


# main routine
test_list = ["", "file_name", "file-name", "my file"]

for item in test_list:
    the_filename = filename_maker(item)
    print(the_filename)
