from backend import DBModel

db = DBModel()

class User:
    def __init__(self, user_data):
        if user_data is None:
            raise ValueError("User data cannot be None")
        
        self.username = user_data["username"]
        self.password = user_data["password"]
        self.email = user_data["email"]
        self.fullName = user_data["fullName"]
        self.birthDate = user_data["birthDate"]
        self.age = user_data["age"]
        self.gender = user_data["gender"]
        self.address = user_data["address"]
        self.role = user_data["role"]

    def login(self, username, password):
        if db.get_user_data(username, "password") == password:
            return db.get_user_data(username, "role")
        return "User not found."

    def logout(self):
        print(f"{self.username} logged out.")

    def change_password(self, old_password, new_password):
        if self.password == old_password:
            db.update(self.username, "password", new_password)
            print("Password changed successfully.")
        else:
            print("Incorrect old password.")