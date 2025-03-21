import json
import os
import hashlib

# hashing
def generate_id(username):
    return hashlib.sha256(username.encode()).hexdigest()[:8]

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(password, hashed_password):
    return hash_password(password) == hashed_password

class DBModel:
    def __init__(self, file_path):
        self.file_path = file_path
        
        if not os.path.exists(self.file_path):
            self.save_data([])

    def load_data(self):
        if os.path.exists(self.file_path) and os.path.getsize(self.file_path) > 0:
            with open(self.file_path, "r") as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    return []  # Return an empty list if JSON is corrupted
        return []
  
    def save_data(self, data):
        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=4)

    # Adding data
    def create(self, new_data):
        data = self.load_data()
        new_data["id"] = generate_id(new_data["username"])
        new_data["password"] = hash_password(new_data["password"])  # Hash password before saving
        if any(item["id"] == new_data["id"] for item in data):
            print("ID already exists.")
            return
        data.append(new_data)
        self.save_data(data)
        print("Data saved successfully.")

    # Updating data
    def update(self, id, key, new_value):
        data = self.load_data()
        for item in data:
            if item.get("id") == id:
                if key == "password":
                    new_value = hash_password(new_value)  # Hash new password before updating
                item[key] = new_value
                self.save_data(data)
                print("Data updated successfully.")
                return
        print("User not found.")


    # Reading data by role/type
    def read_all(self, filter_key=None, filter_value=None):
        data = self.load_data()
        if filter_key and filter_value:
            data = [item for item in data if item.get(filter_key) == filter_value]
        return data

    # Getting specific data
    def get(self, value, key):
        
        data = self.load_data()
        for item in data:
            if item[key] == value:
                return item
        return {}