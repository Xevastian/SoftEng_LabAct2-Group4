from user import User
from backend import DBModel
from vaccines import Vaccine
from appointments import Appointment
import backend
import hashlib
import json

db = DBModel("users.json")

class Admin(User):
    def __init__(self, user_data):
        super().__init__(user_data)
        if self.role != "admin":
            raise ValueError("User is not an admin.")

    def manage_users(self):
        def display_users(search_term=None):
            users = db.read_all()

            # Apply search filter if search_term is provided
            if search_term:
                users = [user for user in users if search_term.lower() in json.dumps(user).lower()]

            # Sort users by role
            users = sorted(users, key=lambda x: x["role"])

            if not users:
                print("\n\n" + "-" * 50)
                print("No users found.")
                print("-" * 50 + "\n")
            else:
                print("\n" + "-" * 80)
                print(f"{'ID':<10}{'Username':<15}{'Email':<25}{'Full Name':<20}{'Role':<10}")
                print("-" * 80)

                for user in users:
                    print(f"{user['id']:<10}{user['username']:<15}{user['email']:<25}{user['fullName']:<20}{user['role']:<10}")
                
                print("-" * 80 + "\n")

        
        while True:
            choice = input("\n[1]View All Users     [2]Search Users     [3]Add Users     [4]Edit Users     [5]Back\n\nInput: ").strip()

            if choice == "1":
                #display users
                print('\n\n'+"-" * 15,"All Data","-" * 15)
                display_users()
            elif choice == "2":
                #search users
                search_input = input("Enter search term: ") 
                print('\n\n'+"-" * 15,"Contains",search_input,"-" * 15)
                display_users(search_input)
            elif choice == '3':
                #Add users
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
                db.create(user_data)
                
            elif choice == '4':
                #edit users
                user_id = input("Enter the ID of the user you want to update: ")
                key = input("Enter the field to update [email, fullName, age, address, gender, birthDate, role, password]: ")
                new_value = input("Enter the new value: ")
                if key.lower() in ["password", "pw"]:  
                    new_value = hashlib.sha256(new_value.encode()).hexdigest()
                db.update(user_id, key, new_value)
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")

    def manage_appointment(self):
        def view_appointments():
            appointments = Appointment.getAllAppointments()

            if not appointments:
                print("\nNo appointments found.")
            else:
                print("\n" + "-" * 80)
                print(f"{'ID':<10}{'User ID':<15}{'Time':<20}{'Vaccine':<20}{'Status':<15}")
                print("-" * 80)

                for appt in appointments:
                    print(f"{appt['appointmentId']:<10}{appt['userId']:<15}{appt['time']:<20}{appt['vaccination']:<20}{appt['status']:<15}")

                print("-" * 80)

        def modify_appointment():
            try:
                appointmentId = int(input("Enter appointment ID to update: ").strip())
                key = input("Enter the field to update (time, vaccination, status): ").strip()
                new_value = input("Enter new value: ").strip()
                
                if key not in ["time", "vaccination", "status"]:
                    print("Invalid field. Allowed fields: time, vaccination, status.")
                    return

                Appointment.update_appointment(appointmentId, key, new_value)
                print("Appointment updated successfully.")
            except ValueError:
                print("Invalid appointment ID. Please enter a valid number.")

        def remove_appointment():
            try:
                appointmentId = int(input("Enter appointment ID to delete: ").strip())
                Appointment.delete_appointment(appointmentId)
                print("Appointment deleted successfully.")
            except ValueError:
                print("Invalid appointment ID. Please enter a valid number.")
        while True:
            choice = input("\n[1]View Appointment     [2]Update Appointment     [3]Clear Appointment     [4]Back\n\nInput: ").strip()
            
            if choice == '1':
                view_appointments()
            elif choice == '2':
                modify_appointment()
            elif choice == '3':
                remove_appointment()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")

    def manage_vaccincation(self):
        def display():
            all_vaccines = Vaccine.get_all_vaccines()
            print(f"\n{'-' * 50}")
            print(f"{'ID':<5} {'Name':<20} {'Manufacturer':<20} {'Stock':<10}")
            print(f"{'-' * 50}")
            
            for vaccine in all_vaccines:
                print(f"{vaccine['vaccineId']:<5} {vaccine['name']:<20} {vaccine['manufacturer']:<20} {vaccine['stock']:<10}")
            
            print(f"{'-' * 50}\n")
        while True:
            choice = input("\n[1]Add Stock     [2]Remove Stock     [3]Check Stock     [4]Back\n\nInput: ").strip()
            
            if choice == '1':
                name = input("Enter vaccine name: ").strip()
                manufacturer = input("Enter manufacturer: ").strip()
                try:
                    count = int(input("Enter stock amount to add: ").strip())
                    if count > 0:
                        Vaccine.add_vaccine(name, manufacturer, count)
                        display()
                    else:
                        print("Stock count must be positive.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            elif choice == '2':
                try:
                    vaccine_id = int(input("Enter vaccine ID to reduce stock: ").strip())
                    amount = int(input("Enter amount to reduce: ").strip())

                    if amount > 0:
                        Vaccine.reduce_stock(vaccine_id, amount)
                        display()
                    else:
                        print("Reduction amount must be positive.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            elif choice == '3':
                display()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")
