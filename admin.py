from user import User

class Admin(User):
    def __init__(self, username, password, email, fullName, birthDate, age, gender, address, admin_id):
        super().__init__(username, password, email, fullName, birthDate, age, gender, address)
        self.admin_id = admin_id

    def manage_users(self):
        print(f"Admin {self.username} is managing users.")

    def approve_appointment(self):
        print(f"Admin {self.username} is approving an appointment.")

    def view_reports(self):
        print(f"Admin {self.username} is viewing reports.")