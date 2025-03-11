from backend import DBModel

db = DBModel()

class User:
    def __init__(self, username, password, email, fullName, birthDate, age, gender, address):
        self.username = username
        self.password = password
        self.email = email
        self.fullName = fullName
        self.birthDate = birthDate
        self.age = age
        self.gender = gender
        self.address = address
        self.role = 'patient'

    def login(self):
        if db.get_user_data(self.username,"password") == self.password:
            return db.get_user_data(self.username,"role")
        return "User not found."

    def logout(self):
        print(f"{self.username} logged out.")

    def change_password(self, old_password, new_password):
        if self.password == old_password:
            db.update(self.username, "password",new_password)
            print("Password changed successfully.")
        else:
            print("Incorrect old password.")

#not existing user
test= User("john_doess", "pass123", "john@example.com", "John Doe", "1990-05-15", 35, "Male", "123 Street, NY") 
test.login()
#existing user
user = User("john_doe", "pass123", "john@example.com", "John Doe", "1990-05-15", 35, "Male", "123 Street, NY") 
print(user.login()) #role if the user exist
user.change_password("password", "newpass456") # wrong pass
user.change_password("pass123", "newpass456") #succesfull change