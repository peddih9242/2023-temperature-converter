# reverse a list and show the 5 most recent items

to_be_reversed = []

for item in range(5):
    response = input("Enter an item: ")
    to_be_reversed.append(response)

to_be_reversed.reverse()
recent_five = to_be_reversed[0:5]
print(recent_five)
