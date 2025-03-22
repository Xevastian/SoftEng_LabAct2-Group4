import json
import os
import hashlib
import sys
import msvcrt  # Windows-only

# hashing
def generate_id(username):
    return hashlib.sha256(username.encode()).hexdigest()[:8]

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(password, hashed_password):
    return hash_password(password) == hashed_password

def input_password(prompt="Password: "):
    print(prompt, end="", flush=True)
    password = ""
    
    while True:
        ch = msvcrt.getch()  # Read a single character
        if ch in {b'\r', b'\n'}:  # Enter key is pressed
            print()  # Move to the next line
            break
        elif ch == b'\x08':  # Backspace key is pressed
            if len(password) > 0:
                password = password[:-1]
                sys.stdout.write('\b \b')  # Remove the last `*`
                sys.stdout.flush()
        else:
            password += ch.decode('utf-8')
            print("*", end="", flush=True)
    
    return password

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
    def create(self, new_data): # for users
        data = self.load_data()
        new_data["id"] = generate_id(new_data["username"])
        new_data["password"] = hash_password(new_data["password"])  # Hash password before saving
        if any(item["id"] == new_data["id"] for item in data):
            print("ID already exists.")
            return
        data.append(new_data)
        self.save_data(data)
        print("Data saved successfully.")

    def create_data(self, new_data):
        data = self.load_data()
        data.append(new_data)
        self.save_data(data)
        print("Data saved successfully.")

    # Updating data
    def update(self, id, key, new_value, identifier_key="id"):
        data = self.load_data()
        found = False
        for item in data:
            if item.get(identifier_key) == (int(id) if identifier_key == "appointmentId" else id):  # Convert id to int if needed
                found = True
                if key == "password":
                    new_value = hash_password(new_value)
                item[key] = new_value
                self.save_data(data)
                print(f"Data updated successfully: {item}")
                return
        if not found:
            print(f"No item found with {identifier_key} = {id}")



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
    
    def get_last_id(self,id_name): # for increments of id in json
        data = self.load_data()
        if data:
            return data[-1][id_name]
        return None  
    
    def delete(self, id, identifier_key="id"):
        data = self.load_data()
        updated_data = [item for item in data if item[identifier_key] != id]
        if len(updated_data) == len(data):  # No changes means ID was not found
            print("ID not found.")
            return

        self.save_data(updated_data)
        print("Data deleted successfully.")
