# reverse a list and show the 5 most recent items

to_be_reversed = []
MAX_CALCS = 5
response = ""

while response != "xxx":

    response = input("Enter an item: ")

    if response == "xxx":
        break

    to_be_reversed.append(response)

# print reversed order of lists
if len(to_be_reversed) >= MAX_CALCS:
    print("\nMost Recent")
    for item in range(0, MAX_CALCS):
        print(to_be_reversed[len(to_be_reversed) - item - 1])
else:
    print("\nItems from Newest to Oldest")
    for item in range(len(to_be_reversed)):
        print(to_be_reversed[len(to_be_reversed) - item - 1])
