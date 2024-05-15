from pymongo import MongoClient
import hashlib, binascii, os

# Connect to MongoDB
# Replace 'mongodb+srv://<username>:<password>@<cluster-url>/test?retryWrites=true&w=majority' with your actual MongoDB connection string
client = MongoClient('mongodb+srv://apucic:BmCU0EAZBUAcvNbb@cluster0.zoehvde.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['user_management']
users = db.users

def hash_password(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')

def verify_password(stored_password, provided_password):
    """Verify a stored password against one provided by user."""
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512', 
                                  provided_password.encode('utf-8'), 
                                  salt.encode('ascii'), 
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password

def register(name, surname, email, password):
    """Register a new user."""
    if users.find_one({"email": email}):
        return False, "Email already registered."
    hashed_pwd = hash_password(password)
    users.insert_one({"name": name, "surname": surname, "email": email, "password": hashed_pwd})
    return True, "User registered successfully."

def login(email, password):
    """Login a user."""
    user = users.find_one({"email": email})
    if user and verify_password(user['password'], password):
        return True, "Login successful."
    return False, "Invalid email or password."

def forgot_password(email):
    """Reset password process simulation."""
    user = users.find_one({"email": email})
    if user:
        new_password = "newpassword123"  # For demonstration purposes
        new_hashed_pwd = hash_password(new_password)
        users.update_one({"email": email}, {"$set": {"password": new_hashed_pwd}})
        return True, f"Your new password is: {new_password}"
    return False, "Email not found."

# Example usage
print(register("John", "Doe", "john.doe@example.com", "password123"))
print(login("john.doe@example.com", "password123"))
print(forgot_password("john.doe@example.com"))
print(login("john.doe@example.com", "newpassword123"))
