#using python dictionaries for making dummy databases

#dummy database of all active PMU students
students = [
  {"name": "Daman Arshad", "PMUID": "202300481", "email": "202300481@pmu.edu.sa", "PMUpassword": "wind#0Dam"},
  {"name": "Nuhaa Khan", "PMUID": "2023004308", "email": "202300308@pmu.edu.sa", "PMUpassword": "biryanI123$"},
  {"Name": "Syeda Fatima", "PMUID": "202300288", "email": "202300288@pmu.edu.sa", "PMUpassword": "aaloo1234!!"},
  {"Name": "Wasan Alsanouna", "PMUID": "202301446", "email": "202301466@pmu.edu.sa", "PMUpassword": "kirby67%db"},  
  {"Name": "Zainab Fatima", "PMUID": "202300316", "email": "202300316@pmu.edu.sa", "PMUpassword": "ZaZa67%67%"},
  {"Name": "Zunairah Khan", "PMUID": "202300994", "email": "202300994@pmu.edu.sa", "PMUpassword": "kakdiZun123#"}
]

#dummy database of all active users
users = [
  {"Name": "Zainab Fatima", "Email": "202300316@pmu.edu.sa", "Password": "baiganAchaar123$", "XP": 102},
  {"Name": "Daman Arshad", "Email": "202300481@pmu.edu.sa", "Password": "dadaArrr9/11", "XP": 172},
  {"Name": "Syeda Fatima", "Email": "202300288@pmu.edu.sa", "Password": "tamataR57$", "XP": 280},  
]

#dummy database of all active mentors
mentors = [
  {"Name": "Zainab Fatima", "Email": "202300316@pmu.edu.sa", "Password": "zain911F@!", "XP": 102, "MentorID": "MO10001"}
]

#dummy database of all active mentees
mentees = [
  {"Name": "Daman Arshad", "Email": "202300481@pmu.edu.sa", "Password": "dadaArrr9/11", "XP": 172, "MenteeID": "ME00001"},
  {"Name": "Syeda Fatima", "Email": "202300288@pmu.edu.sa", "Password": "tamataR57$", "XP": 280, "MenteeID": "ME00002"}
]

#methods to display a message when validation of credentials passes or fails
def displayAcceptedMessage(n):
    match n:
        case 0: print("PMU Email Account Verified! Enter your account details!")
        case 1: print("Strong Password successfully created!")
        case 2: print("Congratulations!!! Your Account has been created!")

def displayErrorMessage(n):
    match n:
        case 0: print("Please follow correct email format! (username@domain) ")
        case 1: print("Invalid Email Domain!")
        case 2: print("Invalid PMU ID!")
        case 3: print("Wrong Password!")
        case 4: print("Password should contain one lower case letter!")
        case 5: print("Password should contain one upper case letter!")
        case 6: print("Password should contain one number!")
        case 7: print("Password should contain one special character!")
        case 8: print("Password should have atleast 10 characters!")
        case 9: print("Your passwords don't match!")
    
#
def checkPass(password1, password2):
    if password1 == password2:
        displayAcceptedMessage(1)
    else:
        displayErrorMessage(9)
#
def createPass():
    while True:
        print("Password should have atleast 10 characters: 1 uppercase, 1 lowercase, 1 number, 1 special symbol")
        p1 = str(input("Create Password: "))
        if not any (char.islower() for char in p1): 
            displayErrorMessage(4)
            continue
        if not any (char.isupper() for char in p1): 
            displayErrorMessage(5)
            continue
        if not any (char.isdigit() for char in p1): 
            displayErrorMessage(6)
            continue
        if not any (not char.isalnum() for char in p1): 
            displayErrorMessage(7)
            continue
        if len(p1)<10: 
            displayErrorMessage(8)
            continue
        p2 = str(input("Confirm Password: "))
        checkPass(p1, p2)

#verifying if user trying to sign up is an active PMU student
def verifyActive(ID, domain, password):
    if domain == "pmu.edu.sa":
        found = False
        for student in students:
            if len(ID) == 9 and student["PMUID"] == ID:
                found = True
                if student["PMUpassword"] == password:
                    displayAcceptedMessage(1)
                    createPass()
                    #return True
                else: 
                    displayErrorMessage(3)
                    return False
        else:
            displayErrorMessage(2)
            return False
    else:
        displayErrorMessage(1)
        return False
  
#splitting email & passing on crednetials to another method so user knows exactly where she went wrong
def verifyAccount(studentEmail, password):
    if "@" in studentEmail and studentEmail.count("@") == 1:
        ID, domain = studentEmail.split("@")
        verifyActive(ID, domain, password)
    else:
        displayErrorMessage(0)
        return False
    
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

#Main Method
if __name__ == "__main__":
    print("=== Welcome to PMU Mentor ===")
    print("1. Create Account")
    print("2. Login to Account\n")
    num = int(input("Select 1 or 2: "))
    print()
    
    if num == 1:
        print("=== Account Creation ===\n")
        email = str(input("PMU Email: "))
        passw = str(input("PMU Password: "))
        verifyAccount(email, passw)
        
    if num == 2:
        print("=== Login System ===")
        email_input = input("Enter your email: ")
        password_input = input("Enter your password: ")
        result = login(email_input, password_input)
        print(f"\nResult: {result}")
        
    else:
        print("Invalid input, please enter 1 or 2 ONLY")







