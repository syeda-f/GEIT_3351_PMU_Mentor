#dummy database for user emails and passwords for login
users = [
    {"email": "userA@pmu.edu.sa", "password": "Password@123"},
    {"email": "userB@pmu.edu.sa", "password": "Password@456"}
]

def verifyDomain(email):
    return email.endswith("@pmu.edu.sa")

def verifyPassword(email, password):
    for user in users:
        if user["email"] == email and user["password"] == password:
            return True
    return False

def getUser(email):
    for user in users:
        if user["email"] == email:
            return user
    return None

def sendCredentials(email, password):
    if not verifyDomain(email):
        return {"result": "failure", "message": "Invalid domain"}
    if not verifyPassword(email, password):
        return {"result": "failure", "message": "Invalid email or password"}
    user = getUser(email)
    return {"result": "success", "user": user}

def login(email, password):
    result = sendCredentials(email, password)
    
    if result["result"] == "success":
        user = result["user"]
        print(f"Login successful! Welcome ")
        return "Welcome"
    else:
        print(f"Error: {result['message']}")
        return "Invalid credentials"

if __name__ == "__main__":
    print("=== PMU Login System ===\n")
    email_input = input("Enter your email: ")
    password_input = input("Enter your password: ")
    
    result = login(email_input, password_input)
    print(f"\nResult: {result}")
