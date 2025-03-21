from backend import DBModel

db = DBModel("users.json")

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
        user_data = db.get_user(username)
        if user_data and user_data["password"] == password:
            return user_data["role"]
        return None

    def logout(self):
        print(f"{self.username} logged out.")

    def change_password(self, old_password, new_password):
        pass
