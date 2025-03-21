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
        if self.password == old_password:
            db.update(self.username, "password", new_password)
            print("Password changed successfully.")
        else:
            print("Incorrect old password.")


class Admin(User):
    def __init__(self, user_data):
        super().__init__(user_data)
        if self.role != "admin":
            raise ValueError("User is not an admin.")

    def manage_users(self):
        users = db.readData("admin") + db.readData("patient")
        for user in users:
            print(user)


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
