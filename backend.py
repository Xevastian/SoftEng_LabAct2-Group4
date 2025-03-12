import json
import os

class DBModel:
    FILE_PATH = "users.json"
    
    def __init__(self):
        if not os.path.exists(self.FILE_PATH):
            self.save_users([])

    def load_users(self):
        if os.path.exists(self.FILE_PATH) and os.path.getsize(self.FILE_PATH) > 0:
            with open(self.FILE_PATH, "r") as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    return []  # Return an empty list if JSON is corrupted
        return []
  
    def save_users(self, users):
        with open(self.FILE_PATH, "w") as file:
            json.dump(users, file, indent=4)

    #adding
    def register(self, username, password, email, fullName, birthDate, age, gender, address):
        users = self.load_users()
        if any(user["username"] == username for user in users):
            print("Username already exists.")
            return
        new_user = {
            "username": username,
            "password": password,
            "email": email,
            "fullName": fullName,
            "birthDate": birthDate,
            "age": age,
            "gender": gender,
            "address": address,
            "role": "patient"
        }
        users.append(new_user)
        self.save_users(users)
        print("User registered successfully.")

    #updating
    def update(self, username, key, data):
        users = self.load_users()
        for user in users:
            if user["username"] == username:
                user[key] = data
                self.save_users(users)
                print("User updated successfully.")
                return
        print("User not found.")

    #loading mass data
    def readData(self, role):
        users = self.load_users()
        filtered_users = [user for user in users if user["role"] == role]
        return filtered_users
    
    # getting specific data
    def get_user_data(self, username, key):
        users = self.load_users()
        for user in users:
            if user["username"] == username:
                return user.get(key, "Key not found.")
        print("User not found.")
        return None
    
    def get_user(self, username):
        users = self.load_users()
        for user in users:
            if user["username"] == username:
                return user
        print("User not found.")
        return None