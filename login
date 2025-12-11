# Dummy user database
users = [
    {"email": "userA@pmu.edu.sa", "password": "Password@123"},
    {"email": "userB@pmu.edu.sa", "password": "Password@456"}
]

def login():
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    
    if not email.endswith("@pmu.edu.sa"):
        print("Error: Invalid domain. Must be @pmu.edu.sa")
    
    for user in users:
        if user["email"] == email and user["password"] == password:
            print(f"\nLogin successful! Welcome {email}")
            return ("Welcome")
    
    print("Error: Invalid email or password")
    return ("Invalid credentials")

# Main program
if __name__ == "__main__":
    print("=== PMU Login System ===\n")
    result = login()
    print(f"\nResult: {result}")


