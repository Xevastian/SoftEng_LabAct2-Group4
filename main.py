from admin import Admin
from patient import Patient
from appointments import Appointment
from vaccines import Vaccine
from backend import DBModel
import backend
import hashlib
from datetime import datetime, timedelta


# Initialize databases
users_db = DBModel("users.json")
appointments_db = DBModel("appointments.json")
vaccines_db = DBModel("vaccines.json")
    
def get_available_times():
    appointments = Appointment.getAllAppointments()  # Fetch all appointments from the database
    booked_times = [appointment['time'] for appointment in appointments]

    start_time = datetime.strptime('07:00', '%H:%M')
    end_time = datetime.strptime('17:00', '%H:%M')

    available_times = []
    current_time = start_time

    while current_time <= end_time:
        time_str = current_time.strftime('%H:%M')
        if time_str not in booked_times:
            available_times.append(time_str)
        current_time += timedelta(minutes=30)

    return available_times

def print_available_times(times):
    morning_times = [time for time in times if time < '12:00']
    afternoon_times = [time for time in times if time >= '12:30']

    print("Available Hours:")
    print("---------------------------------")
    print("       Morning | Afternoon ")
    print("---------------------------------")

    max_length = max(len(morning_times), len(afternoon_times))
    for i in range(max_length):
        left = morning_times[i] if i < len(morning_times) else ""
        right = afternoon_times[i] if i < len(afternoon_times) else ""
        print(f"{left:<14} | {right}")
    print("---------------------------------")

def main():
    print("Welcome to the Vaccination Appointment System")
    
    while True:
        choice = input("\n[1]Register     [2]Log in     [3]Exit\n\nInput: ").strip()

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

def register():
    username = input("Username: ")
    email = input("Email: ")
    password = backend.input_password()
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
    users_db.create(user_data)
    return

def login():
    email = input("Email: ")
    password = backend.input_password()
    user = users_db.get(email,'email')
    if user == {} or user['password'] != hashlib.sha256(password.encode()).hexdigest():
        print('Wrong email or password')
        return   
    if user['role'] == 'admin':
        adminTerminal(user)
    else:
        patientTerminal(user)
    return

def patientTerminal(patient):
    patient = Patient(patient)
    patient.login()
    while True:
        choice = input("\n[1]Book Appointment     [2]View Appointment     [3]Cancel Appointment     [4]Change User Details     [5]Log out\n\nInput: ").strip()

        if choice == "1":
            available_times =  get_available_times()
            print_available_times(available_times)

            time = input("Enter time(HH:MM): ")
            Vaccine.get_available_vaccines()
            vaccination = input("Enter Vaccine: ")
            patient.book_appointment(time, vaccination)
        elif choice == "2":
            patient.view_appointment()
        elif choice == '3':
            patient.view_appointment()
            appointmentId = input("Enter appointment ID: ")
            patient.cancel_appointment(appointmentId)
        elif choice == '4':
            key = input("Enter detail to change (age, address, username, password): ").strip()
            if key not in ["age", "address", "username", "password"]:
                print("Invalid option. You can only update age, address, username, or password.")
                continue
            
            if key == "password":
                old_password = input("Enter old password: ").strip()
                new_password = input("Enter new password: ").strip()
                try:
                    patient.change_detail(old_password, new_password, key, new_password)
                except ValueError as e:
                    print(e)
            else:
                value = input(f"Enter new {key}: ").strip()
                patient.change_detail(None, None, key, value)
        elif choice == '5':
            patient.logout()
            break
        else:
            print("Invalid choice. Please try again.")


def adminTerminal(admin):
    admin = Admin(admin)
    admin.login()
    while True:
        choice = input("\n[1]Manage Users     [2]Manage Appointment     [3]Manage Vaccinations     [4]Change User Details     [5]Log out\n\nInput: ").strip()

        if choice == "1":
            admin.manage_users()
        elif choice == "2":
            admin.manage_appointment()
        elif choice == '3':
            admin.manage_vaccincation()
        elif choice == '4':
            key = input("Enter detail to change (age, address, username, password): ").strip()
            if key not in ["age", "address", "username", "password"]:
                print("Invalid option. You can only update age, address, username, or password.")
                continue
            
            if key == "password":
                old_password = input("Enter old password: ").strip()
                new_password = input("Enter new password: ").strip()
                try:
                    admin.change_detail(old_password, new_password, key, new_password)
                except ValueError as e:
                    print(e)
            else:
                value = input(f"Enter new {key}: ").strip()
                admin.change_detail(None, None, key, value)
        elif choice == '5':
            admin.logout()
            break
        else:
            print("Invalid choice. Please try again.")
    
main()
