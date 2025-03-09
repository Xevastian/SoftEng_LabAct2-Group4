class User:
    def __init__(self, user_id, username, password, email, role):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.email = email
        self.role = role

    def login(self, username, password):
        return self.username == username and self.password == password

    def logout(self):
        print(f"{self.username} logged out.")

    def change_password(self, old_password, new_password):
        if self.password == old_password:
            self.password = new_password
            print("Password changed successfully.")
        else:
            print("Incorrect old password.")

class Admin(User):
    def __init__(self, user_id, username, password, email, admin_id):
        super().__init__(user_id, username, password, email, role="Admin")
        self.admin_id = admin_id

    def manage_users(self):
        print(f"Admin {self.username} is managing users.")

    def approve_appointment(self):
        print(f"Admin {self.username} is approving an appointment.")

    def view_reports(self):
        print(f"Admin {self.username} is viewing reports.")

class Patient(User):
    def __init__(self, user_id, username, password, email, patient_id):
        super().__init__(user_id, username, password, email, role="Patient")
        self.patient_id = patient_id

    def book_appointment(self):
        print(f"Patient {self.username} booked an appointment.")

    def cancel_appointment(self):
        print(f"Patient {self.username} canceled an appointment.")

    def view_appointment(self):
        print(f"Patient {self.username} is viewing appointments.")
