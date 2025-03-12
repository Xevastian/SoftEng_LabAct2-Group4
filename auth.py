from backend import DBModel

class User:
    def __init__(self, user_data):
        self.username = user_data["username"]
        self.role = user_data["role"]

    def terminal(self):
        print(f"Welcome, {self.username}! You are logged in as {self.role}.")


class Patient(User):
    def __init__(self, user_data):
        super().__init__(user_data)
    
    def terminal(self):
        print(f"Patient Portal - Welcome, {self.username}!")


class Admin(User):
    def __init__(self, user_data):
        super().__init__(user_data)
    
    def terminal(self):
        print(f"Admin Dashboard - Welcome, {self.username}!")


class Auth(DBModel):
    def register(self, username, password, email, fullName, birthDate, age, gender, address):
        super().register(username, password, email, fullName, birthDate, age, gender, address)

    def login(self, username, password):
        users = self.load_users()
        for user in users:
            if user["username"] == username and user["password"] == password:
                return self._get_access(user)
        print("Invalid credentials.")
        return None

    def _get_access(self, user):
        if user["role"] == "patient":
            access = Patient(user)
        elif user["role"] == "admin":
            access = Admin(user)
        else:
            print("Invalid role.")
            return None
        access.terminal()
        return access
