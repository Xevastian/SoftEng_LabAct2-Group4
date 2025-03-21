from user import User
from backend import DBModel

db = DBModel("users.json")

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