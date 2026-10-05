print("Adding up whole numbers")
user_reply = "y"
total = 0
while user_reply == "y":
 nuevo_numero = int(input("Introduce the number to add"))
 total = total + nuevo_numero
 user_reply = input("Continue?")
print("The total result is: ", total)
print("Thank you for using this program!")
