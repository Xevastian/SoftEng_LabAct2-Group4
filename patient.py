from user import User
from backend import DBModel
from appointments import Appointment

db = DBModel("users.json")

class Patient(User):
    def __init__(self, user_data):
        super().__init__(user_data)
        if self.role != "patient":
            raise ValueError("User is not a patient.")

    def book_appointment(self, time, vaccination):
        Appointment.schedule_appointment(self.id, time, vaccination)
        print("\nAppointment successfully booked!")

    def view_appointment(self):
        appointments = Appointment.getAllAppointments(filter_key="userId", filter_value=self.id)
        
        if not appointments:
            print("\nNo appointments found.")
            return
        
        print("\nYour Appointments:")
        print("-" * 80)
        print(f"{'ID':<10}{'Time':<20}{'Vaccine':<20}{'Status':<15}")
        print("-" * 80)

        for appt in appointments:
            print(f"{appt['appointmentId']:<10}{appt['time']:<20}{appt['vaccination']:<20}{appt['status']:<15}")

        print("-" * 80)

    def cancel_appointment(self, appointment_id):
        appointments = Appointment.getAllAppointments(filter_key="userId", filter_value=self.id)
        for appointment in appointments:
            if appointment['appointmentId']:# == appointment_id and appointment['userId'] == self.id:
                Appointment.update_appointment(appointment_id, "status", 'Cancel')
                print("\nAppointment successfully canceled!")
                return
        print("\nAppointment not found or does not belong to you.")
            
        