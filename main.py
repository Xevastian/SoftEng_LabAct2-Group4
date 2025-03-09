#Di pa to finals hehe
from user import Admin, Patient

# Store registered users
users = {}

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
    
    if username in users:
        print("Username already exists. Try a different one.")
        return

    password = input("Enter password: ").strip()
    email = input("Enter email: ").strip()
    role = input("Enter role (Admin/Patient): ").strip().capitalize()

    if role == "Admin":
        admin_id = input("Enter Admin ID: ").strip()
        users[username] = Admin(len(users) + 1, username, password, email, admin_id)
        print(f"Admin {username} registered successfully.")

    elif role == "Patient":
        patient_id = input("Enter Patient ID: ").strip()
        users[username] = Patient(len(users) + 1, username, password, email, patient_id)
        print(f"Patient {username} registered successfully.")

    else:
        print("Invalid role. Please enter 'Admin' or 'Patient'.")

def login():
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    user = users.get(username)

    if user and user.login(username, password):
        print(f"Welcome, {user.username}! You are logged in as {user.role}.")
        
        if isinstance(user, Admin):
            admin_menu(user)
        elif isinstance(user, Patient):
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
            admin.manage_users()
        elif choice == "2":
            admin.approve_appointment()
        elif choice == "3":
            admin.view_reports()
        elif choice == "4":
            admin.logout()
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
            patient.book_appointment()
        elif choice == "2":
            patient.cancel_appointment()
        elif choice == "3":
            patient.view_appointment()
        elif choice == "4":
            patient.logout()
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
