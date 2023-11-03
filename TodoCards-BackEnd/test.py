import os, hashlib, hmac

# global variable for consistant salt size
SALT_SIZE = 16

# Authentication function to generate password hash
# Note that the salt is simply concatenated to the hash
def hash_password(password):
    salt = os.urandom(SALT_SIZE)
    pw_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return pw_hash + salt

# Authentication function to generate password hash
# using indexing to retrieve the salt
def is_password_correct(pw_salt_hash, password):
    salt = pw_salt_hash[-SALT_SIZE:]
    pw_hash = pw_salt_hash[:-SALT_SIZE]
    return hmac.compare_digest(
        pw_hash,
        hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    )



