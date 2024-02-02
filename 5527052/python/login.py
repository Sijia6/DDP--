import hashlib
user_datebase = {}

def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def register(username, password):
    if username in user_datebase:
        print("User already exists.")
    else:
        user_datebase[username] = hash_password(password)
        print(f"User {username} registered successfully.")

def login(username, password):
    if username in user_datebase and user_datebase[username] == hash_password(password):
        print(f"User {username} logged in successfully.")
        return True
    else:
        print("Invalid username or password.")
        return False

register('john', 's3cureP@ssw0rd')
login('john', 's3cureP@ssw0rd')
login('john', 'wrongpassword')


