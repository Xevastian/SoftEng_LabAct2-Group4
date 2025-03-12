from auth import Auth

def main():
    auth = Auth()
    
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            username = input("Username: ")
            password = input("Password: ")
            email = input("Email: ")
            fullName = input("Full Name: ")
            birthDate = input("Birth Date (YYYY-MM-DD): ")
            age = input("Age: ")
            gender = input("Gender: ")
            address = input("Address: ")
            
            auth.register(username, password, email, fullName, birthDate, age, gender, address)
        
        elif choice == "2":
            username = input("Username: ")
            password = input("Password: ")
            
            user = auth.login(username, password)
            if user:
                user.terminal()
        
        elif choice == "3":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()