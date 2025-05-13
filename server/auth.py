import bcrypt
def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password, salt.decode('utf-8')

def verify_password(password, hashed_password):
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

# Example usage
password = "mysecretpassword"
hashed_password, salt = hash_password(password)
print(f"Hashed password: {hashed_password.decode('utf-8')}")

is_correct = verify_password(password, hashed_password.decode('utf-8'))
print(f"Password correct: {is_correct}")