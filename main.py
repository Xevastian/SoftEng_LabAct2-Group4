from user import *
from appointments import Appointment
from vaccines import Vaccine
from backend import DBModel

# Initialize databases
users_db = DBModel("users.json")
appointments_db = DBModel("appointments.json")
vaccines_db = DBModel("vaccines.json")

def main():
    print("Welcome to the Vaccination Appointment System")
    
    while True:
        choice = input("\nDo you want to (1) Register or (2) Log in? Enter 1 or 2: ").strip()

        if choice == "1":
            register()
        elif choice == "2":
            login()
        else:
            print("Invalid choice. Please enter 1 or 2.")

def register():
    username = input("Enter username: ").strip()
    
    if users_db.get(username, "username"):
        print("Username already exists. Try a different one.")
        return

    password = input("Enter password: ").strip()
    email = input("Enter email: ").strip()
    role = input("Enter role (Admin/Patient): ").strip().capitalize()

    if role == "Admin":
        admin_id = input("Enter Admin ID: ").strip()
        new_user = {
            "username": username,
            "password": password,
            "email": email,
            "role": "admin",
            "admin_id": admin_id
        }
        users_db.create(new_user, "username")
        print(f"Admin {username} registered successfully.")

    elif role == "Patient":
        patient_id = input("Enter Patient ID: ").strip()
        new_user = {
            "username": username,
            "password": password,
            "email": email,
            "role": "patient",
            "patient_id": patient_id
        }
        users_db.create(new_user, "username")
        print(f"Patient {username} registered successfully.")

    else:
        print("Invalid role. Please enter 'Admin' or 'Patient'.")

def login():
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    user = users_db.get(username, "username")
    
    if user and user["password"] == password:
        print(f"Welcome, {user['username']}! You are logged in as {user['role'].capitalize()}.")
        
        if user["role"] == "admin":
            admin_menu(user)
        elif user["role"] == "patient":
            patient_menu(user)
    
    else:
        print("Invalid username or password.")

def admin_menu(admin):
    while True:
        print("\nAdmin Menu:")
        print("1. Manage Users")
        print("2. Approve Appointment")
        print("3. View Reports")
        print("4. Logout")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            manage_users()
        elif choice == "2":
            approve_appointment()
        elif choice == "3":
            view_reports()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")

def patient_menu(patient):
    while True:
        print("\nPatient Menu:")
        print("1. Book Appointment")
        print("2. Cancel Appointment")
        print("3. View Appointments")
        print("4. Logout")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            book_appointment(patient)
        elif choice == "2":
            cancel_appointment(patient)
        elif choice == "3":
            view_appointments(patient)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")

def manage_users():
    users = users_db.read_all()
    for user in users:
        print(user)

def approve_appointment():
    appointments = appointments_db.read_all(filter_key="status", filter_value="Pending")
    for appointment in appointments:
        print(appointment)
    
    appointment_id = input("Enter the appointment ID to approve: ").strip()
    appointments_db.update(int(appointment_id), "status", "Approved")
    print("Appointment approved successfully.")

def view_reports():
    appointments = appointments_db.read_all()
    print("All Appointments:")
    for appointment in appointments:
        print(appointment)

def book_appointment(patient):
    user_id = patient["username"]
    time = input("Enter appointment time (YYYY-MM-DD HH:MM:SS): ").strip()
    location = input("Enter location: ").strip()

    new_appointment = {
        "appointmentId": len(appointments_db.read_all()) + 1,
        "userId": user_id,
        "time": time,
        "location": location,
        "status": "Pending"
    }
    appointments_db.create(new_appointment, "appointmentId")
    print("Appointment booked successfully.")

def cancel_appointment(patient):
    user_id = patient["username"]
    appointments = appointments_db.read_all(filter_key="userId", filter_value=user_id)
    if not appointments:
        print("No appointments found.")
        return
    
    for appointment in appointments:
        print(appointment)

    appointment_id = input("Enter the appointment ID to cancel: ").strip()
    appointments_db.update(int(appointment_id), "status", "Canceled")
    print("Appointment canceled successfully.")

def view_appointments(patient):
    user_id = patient["username"]
    appointments = appointments_db.read_all(filter_key="userId", filter_value=user_id)
    if not appointments:
        print("No appointments found.")
    else:
        for appointment in appointments:
            print(appointment)

if __name__ == "__main__":
    main()
