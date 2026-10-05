first_name = input("What is your first name? ").strip()
last_name = input("What is your last name? ").strip()
print("Hello,", first_name, last_name + "!")
no_spaces_first = first_name.replace(" ", "")
no_spaces_last = last_name.replace(" ", "")
print("Your first name has", len(no_spaces_first), "letters")
print("Your last name has", len(no_spaces_last), "letters")
if " " in first_name:
    print("Your first name is a compound name")
else:
    print("Your first name is a simple name")
if " " in last_name:
    print("Your last name is a compound name")
else:
    print("Your last name is a simple name")
