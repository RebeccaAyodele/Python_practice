phone = input ("Phone: ")

digits = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
}

output = ""
for i in phone:
    output += digits.get(i, "!") + " "
print(output)