# This is a prototype of the login unit for our Robo-Advisor.
# 

import hashlib
from passwords import USERS

MAX_ATTEMPTS = 3

# login function
def login():
	attempts = 0
	success = 0

	print()
	print("User Login Page:")
	print()

	while (attempts < MAX_ATTEMPTS):
		username = input("Enter username: ")
		password = input("Enter password: ")

		# validation
		if (username in USERS and USERS[username] == hashlib.md5(password.encode("utf-8")).hexdigest()):
			print("You have successfully signed in.")
			print()
			return True
		else:
			print("Sorry, that username and/or password is not correct.")
			print()
		
		attempts += 1

	print("Max number of attempts used.")
	print()
	return False