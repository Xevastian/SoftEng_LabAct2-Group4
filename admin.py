from user import User
from backend import DBModel

class Admin(User):
    def __init__(self, user: User):
        super().__init__({
            "username": user.username,
            "password": user.password,
            "email": user.email,
            "fullName": user.fullName,
            "birthDate": user.birthDate,
            "age": user.age,
            "gender": user.gender,
            "address": user.address,
            "role": "admin"  # Ensure role is set to admin
        })

    def manage_users(self):
        print(f"Admin {self.username} is managing users.")

    def approve_appointment(self):
        print(f"Admin {self.username} is approving an appointment.")

    def view_reports(self):
        print(f"Admin {self.username} is viewing reports.")

db = DBModel()

username = input("Enter username: ")
password = input("Enter password: ")

stored_password = db.get_user_data(username, "password")
if stored_password and stored_password == password:
    user_data = db.get_user(username)  # Fetch full user details
    if user_data:
        user = User(user_data)  # Create User object
        
        if user.role == "admin":
            admin = Admin(user)  # Convert User to Admin
            print(f"Logged in as: {admin.role}")
            admin.manage_users()  # Test admin methods
            admin.approve_appointment()
            admin.view_reports()
        else:
            print(f"Logged in as: {user.role}")
else:
    print("Invalid credentials.")