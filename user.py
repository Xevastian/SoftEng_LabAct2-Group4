from backend import DBModel,hash_password

db = DBModel("users.json")

class User:
    def __init__(self, user_data):
        if user_data is None:
            raise ValueError("User data cannot be None")
        self.id = user_data['id']
        self.username = user_data["username"]
        self.password = user_data["password"]
        self.email = user_data["email"]
        self.fullName = user_data["fullName"]
        self.birthDate = user_data["birthDate"]
        self.age = user_data["age"]
        self.gender = user_data["gender"]
        self.address = user_data["address"]
        self.role = user_data["role"]

    def login(self):
        print(f"\n\n\n{self.username} logged in.\n\n\n")

    def logout(self):
        print(f"\n\n\n{self.username} logged out.\n\n\n")

    def change_detail(self, old_password, new_password, key, value):
        allowed_keys = ["age", "address", "username", "password"]
        
        if key not in allowed_keys:
            raise ValueError("Invalid key. You can only update age, address, username, or password.")
        
        if key == "password":
            if self.password != hash_password(old_password):
                raise ValueError("Incorrect old password.")
            value = new_password  # Assign new password if verification passes
            self.password = new_password

        db.update(self.id, key, value)
        print(f"{key} updated successfully.")
