import random
from time import ctime
import os


#record staff login in time
login_time = ctime()    


#generate 10 digit long account number
def gen_accNumber(N):   
	min = pow(10, N-1)
	max = pow(10, N) - 1
	return random.randint(min, max)


#collects customer info and stores in customer.txt file
def collect_info():   
    accName=input("Please Provide Client's Full Name: ")
    openingBal=input("Enter Opening Balance: ")
    accType=input("Account Type: ")
    accEmail=input("Provide Account Email: ")
    accNumber=gen_accNumber(10)
    clientInfo = (f"Account Name: {accName}\nOpening Balance: NGN{openingBal}\nAccount Type: {accType}\nEmail: {accEmail}\nAccount Number: {accNumber}\n \n")
    client_file = open("customer.txt", "a+")
    client_file.write(clientInfo)
    client_file.close()
    print(f"System Generated Account Number: {accNumber}")
    
    add_new=input("Do You Want To Add Another Customer?\n1. Yes\n2. No\n> ")
    if add_new=="1":
        collect_info()
    else:
        dashboard()
    return clientInfo
    
    
    
#landing page on launching app    
def landing_page():
    option=input("Choose Between 1 and 2\n1. Staff Login\n2. Close App\n> ")
    app_running=True
    if option=="1":
        while app_running:
            staffLoginCheck()
        else:
            app_running=False
        
    

#collect staff login and validates
def staffLoginCheck():
    print("Welcome to Staff Login Page")
    staffUsername=input("Please Enter Your Username: ")
    staffPwd=input("Please Enter Your Password: ")
    
    with open('staff.txt') as staff_file:
        if staffUsername and staffPwd in staff_file.read():
            print("Login Successful!")
            dashboard()
            userSession(staffUsername, login_time)
        else:
            print("Incorrect Details, Try Again")
            
            

#stores username and login time
def userSession(staffUsername, login_time):
    session_file= open("userSession.txt","w+")
    session_file.write(f"{staffUsername} logged in on {login_time}")
    session_file.close()
    
    

#staff dashboard after login
def dashboard():
    print("Staff Dashboard")
    choice=input("1. Create New Bank Account\n2. Check Account Details\n3. Logout\n> ")
    if choice=="1":
        collect_info()
    elif choice=="2":
        accNumber_check=input("Please Enter Customer's Account Number: ")
        with open("customer.txt") as customer_file:
            if accNumber_check in customer_file.read():
                print(collect_info())
            else:
                print("Account Not Found")
                dashboard()
    elif choice=="3":
        os.remove("usersession.txt")
        landing_page()
    else:
        print("Choice Not Recognized, Try Again!")
        
        
landing_page()


    