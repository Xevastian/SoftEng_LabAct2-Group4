import json
import os

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
    def create(self, new_data, unique_key):
        data = self.load_data()
        if any(item[unique_key] == new_data[unique_key] for item in data):
            print(f"{unique_key} already exists.")
            return
        data.append(new_data)
        self.save_data(data)
        print("Data saved successfully.")

    # Updating data
    def update(self, identifier_value, key, new_value, identifier_key="id"):
        data = self.load_data()
        for item in data:
            if item.get(identifier_key) == identifier_value:
                item[key] = new_value
                self.save_data(data)
                print("Data updated successfully.")
                return
        print("Item not found.")

    # Reading data by role/type
    def read_all(self, filter_key=None, filter_value=None):
        data = self.load_data()
        if filter_key and filter_value:
            data = [item for item in data if item.get(filter_key) == filter_value]
        return data

    # Getting specific data
    def get(self, identifier_value, identifier_key="id"):
        data = self.load_data()
        for item in data:
            if item.get(identifier_key) == identifier_value:
                return item
        print("Item not found.")
        return None
