import random
import string
print("Welcome to the password generator!")
length = int(input("How long do you want your password to be? "))
password = ""
for i in range(length):
    password += random.choice(string.ascii_letters + string.digits)
print("Your password is: " + password)
print("Thank you for using the password generator! Have a nice day!")
input("Press Enter to exit.")
exit()
# End of file
