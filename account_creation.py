#using python dictionaries for making dummy databases

#dummy database of all active PMU student emails and their passwords
students = [
  {"Name": "Daman Arshad", "ID": "202300481", "email": "202300481@pmu.edu.sa", "password": "damDam##000"},
  {"Name": "Syeda Fatima", "ID": "202300228", "email": "202300228@pmu.edu.sa", "password": "syedI2004!!"},
  {"Name": "Zainab Fatima", "ID": "202300316", "email": "202300316@pmu.edu.sa", "password": "ZaZa67%67%"},
  {"Name": "Zunairah Khan", "ID": "202300481", "email": "202300994@pmu.edu.sa", "password": "zunZun123#"}
]

#dummy database of all active mentors
mentors = [
  {"Name": "Zainab Fatima",  },
]

#dummy database of all active mentees
mentees = [
  
]

#methods to display a message when validation of credentials passes or fails
def displayAcceptedMessage(n):
  if n == 1:
    print("PMU Email Account Verified! Enter your account details!")
  if n == 2:
    print("Strong Password successfully created!")
def displayErrorMessage(n):
  if n == 0:
    print("Please follow correct email format! (username@domain) ")
  if n == 1:
    print("Invalid Email Domain!")
  if n == 2:
    print("Invalid PMU ID!")
  if n == 3:
    print("Wrong Password!")
  if n == 4:
    print("Your passwords don't match!")

#verifying if user trying to sign up is an active PMU student
def verifyActive(ID, domain, password):
  if domain == "pmu.edu.sa":
    for student in students:
      if len(ID) == 8 and ID == students["ID"]:
        if password == students["password"]: 
          displayAcceptedMessage(1)
          
        else: displayErrorMessage(3)
      else: displayErrorMessage(2)
  else: displayErrorMessage(1)
          
#splitting email & passing on crednetials to another method
def verifyAccount(studentEmail, password):
  if "@" in studentEmail and studentEmail.count("@") == 1:
    ID, domain = studentEmail.split("@")
    verifyActive(ID, domain, password)
  else:
    displayErrorMessage(0)
    
    







#Main Method
print("--- Create Account ---")
email = str(input("PMU Email: "))
passw = str(input("PMU Password: "))
verifyAccount(email, passw)






