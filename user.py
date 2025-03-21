from backend import DBModel
import json
import hashlib

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

class Admin(User):
    def __init__(self, user_data):
        super().__init__(user_data)
        if self.role != "admin":
            raise ValueError("User is not an admin.")

    def manage_users(self):
        def display_users(search_term=None):
            users = db.read_all()
            if search_term:
                users = [user for user in users if search_term.lower() in json.dumps(user).lower()]

            users = sorted(users, key=lambda x: x["role"])
            if len(users) == 0:
                print('\n\n'+"-" * 50)
            for user in users:
                print("ID:", user["id"])
                print("Username:", user["username"])
                print("Email:", user["email"])
                print("Full Name:", user["fullName"])
                print("Age:", user["age"])
                print("Address:", user["address"])
                print("Gender:", user["gender"])
                print("Birth Date:", user["birthDate"])
                print("Role:", user["role"])
                print("-" * 40)  
        
        while True:
            choice = input("\n[1]View All Users     [2]Search Users     [3]Add Users     [4]Edit Users     [5]Back\n\nInput: ").strip()

            if choice == "1":
                #display users
                print('\n\n'+"-" * 15,"All Data","-" * 15)
                display_users()
            elif choice == "2":
                #search users
                search_input = input("Enter search term: ") 
                print('\n\n'+"-" * 15,"Contains",search_input,"-" * 15)
                display_users(search_input)
            elif choice == '3':
                #Add users
                username = input("Username: ")
                email = input("Email: ")
                password = input("Password: ")
                fullname = input("Full name: ")
                birthDate = input("Birth date (yyyy-mm-dd): ")
                age = int(input("Age: "))
                gender = input("Gender: ")
                address = input("Address: ")

                user_data = {
                    "username": username,
                    "password": password,
                    "email": email,
                    "fullName": fullname,
                    "birthDate": birthDate,
                    "age": age,
                    "gender": gender,
                    "address": address,
                    "role": "patient",  
                }
                db.create(user_data)
                
            elif choice == '4':
                #edit users
                user_id = input("Enter the ID of the user you want to update: ")
                key = input("Enter the field to update [email, fullName, age, address, gender, birthDate, role, password]: ")
                new_value = input("Enter the new value: ")
                if key.lower() in ["password", "pw"]:  
                    new_value = hashlib.sha256(new_value.encode()).hexdigest()
                db.update(user_id, key, new_value)
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")

    def manage_appointment(self):
        pass

    def manage_vaccincation(self):
        pass

class Patient(User):
    def __init__(self, user_data):
        super().__init__(user_data)
        if self.role != "patient":
            raise ValueError("User is not a patient.")

    def book_appointment(self, appointment_data):
        db_appointments = DBModel("appointments.json")
        db_appointments.register(**appointment_data)
        print("Appointment booked successfully.")

    def view_appointment(self):
        db_appointments = DBModel("appointments.json")
        appointments = db_appointments.readData("patient")
        if appointments:
            for appointment in appointments:
                print(appointment)
        else:
            print("No appointments found.")

    def cancel_appointment(self, appointment_id):
        db_appointments = DBModel("appointments.json")
        db_appointments.update(appointment_id, "status", "Canceled")
        print("Appointment canceled successfully.")