from user import User

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