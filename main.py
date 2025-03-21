from user import User
from admin import Admin
from patient import Patient
from appointments import Appointment
from vaccines import Vaccine
from backend import DBModel
import hashlib

# Initialize databases
users_db = DBModel("users.json")
appointments_db = DBModel("appointments.json")
vaccines_db = DBModel("vaccines.json")

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
        "role": "patient",  #
    }
    users_db.create(user_data)
    return

def login():
    # email = input("Email: ")
    # password = input("Password: ")
    # user = users_db.get(email,'email')
    # if user == {} or user['password'] != hashlib.sha256(password.encode()).hexdigest():
    #     print('Wrong email or password')
    #     return   
    # user = User(user)
    # if user.role == 'admin':
    #     adminTerminal(user)
    # else:
    #     patientTerminal(user)
    adminTerminal({
        "username": "VexIvan",
        "password": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",
        "email": "test@gmail.com",
        "fullName": "Vex Ivan Sumang",
        "birthDate": "2004-10-16",
        "age": 20,
        "gender": "Male",
        "address": "BSU",
        "role": "admin",
        "id": "c7aadb9c"
    })
    return

def patientTerminal(patient):
    patient = Patient(patient)
    while True:
        choice = input("\n[1]Book Appointment     [2]View Appointment     [3]Edit Appointment     [4]Log out\n\nInput: ").strip()

        if choice == "1":
            #patient.book_appointment()
            pass
        elif choice == "2":
            #patient.view_appointment()
            pass
        elif choice == '3':
            #patient.edit_appointment()
            pass
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