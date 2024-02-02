import hashlib

user_datebase = {}

def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def register(username, password):
    if username in user_datebase:
        print("User already exists.")
        return
    user_datebase[username] = hash_password(password)
    print(f"User {username} registered successfully.")

def login(username, password):
    if username in user_datebase and user_datebase[username] == hash_password(password):
        print(f"User {username} logged in successfully.")
        return True
    else:
        print("Invalid username or password.")
        return False

def reset_password(username):
    if username not in user_datebase:
        print("User does not exist.")
        return
    new_password = input(f"Enter new password for {username}: ")
    user_datebase[username] = hash_password(new_password)
    print(f"Password for {username} reset successfully.")


register('john', 'pppp@ssw0rd')
login('john', 'ppppP@ssw0rd')
reset_password('john')
login('john', 'newP@ssw0rd')
