# used to generate a dictionary of usernames and hashed passwords for testing purposes

import hashlib

USERS = {
}

def create_user(n, p):
	USERS[n] = hashlib.md5(p.encode("utf-8")).hexdigest()

create_user("user1", "pass1")
create_user("user2", "pass2")
create_user("user3", "pass3")




