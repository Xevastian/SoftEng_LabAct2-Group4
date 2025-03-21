from user import User
from admin import Admin
from patient import Patient
from appointments import Appointment
from vaccines import Vaccine
from backend import DBModel
import hashlib
import sys
import msvcrt  # Windows-only

# Initialize databases
users_db = DBModel("users.json")
appointments_db = DBModel("appointments.json")
vaccines_db = DBModel("vaccines.json")

def input_password(prompt="Password: "):
    print(prompt, end="", flush=True)
    password = ""
    
    while True:
        ch = msvcrt.getch()  # Read a single character
        if ch in {b'\r', b'\n'}:  # Enter key is pressed
            print()  # Move to the next line
            break
        elif ch == b'\x08':  # Backspace key is pressed
            if len(password) > 0:
                password = password[:-1]
                sys.stdout.write('\b \b')  # Remove the last `*`
                sys.stdout.flush()
        else:
            password += ch.decode('utf-8')
            print("*", end="", flush=True)
    
    return password
    
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
    password = input_password()
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
        "role": "patient",  #
    }
    users_db.create(user_data)
    return

def login():
    email = input("Email: ")
    password = input_password()
    user = users_db.get(email,'email')
    if user == {} or user['password'] != hashlib.sha256(password.encode()).hexdigest():
        print('Wrong email or password')
        return   
    print(user)
    if user['role'] == 'admin':
        adminTerminal(user)
    else:
        patientTerminal(user)
    return

def patientTerminal(patient):
    patient = Patient(patient)
    while True:
        choice = input("\n[1]Book Appointment     [2]View Appointment     [3]Cancel Appointment     [4]Log out\n\nInput: ").strip()

        if choice == "1":
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
            break
        else:
            print("Invalid choice. Please try again.")


def adminTerminal(admin):
    admin = Admin(admin)
    while True:
        choice = input("\n[1]Manage Users     [2]Manage Appointment     [3]Manage Vaccinations     [4]Log out\n\nInput: ").strip()

        if choice == "1":
            admin.manage_users()
            pass
        elif choice == "2":
            admin.manage_appointment()
            pass
        elif choice == '3':
            admin.manage_vaccincation()
            pass
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")
    
main()