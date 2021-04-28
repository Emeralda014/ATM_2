#To Register
#first name, last name, password, email address are required

#For Login
#email address and password are required

#Bank operations
#Bank operations like withdraw, deposit, transfer and complaints

#Initializing the system

import random
import validation

database = {
    1371451047: ['Onyii', 'Peace', 'peace@gmail.com', 'Peace', 500]
}

def init():
    
    print("Welcome to Copec Bank")
    
    have_account = int(input("Do you have an account with us: 1 (YES) 2 (NO) \n"))
        
    if have_account == 1:
        login()
            
    elif have_account == 2:
        register()
        
    else:
        print("You have selected an invalid option")
        init()
            

def login():
    
    print("******* Login ********")
    
    account_number_from_user = input("What is your account number? \n")
    
    is_valid_account_number = validation.account_number_validation(account_number_from_user)

    if is_valid_account_number:
    
        password = input("What is your password? \n")
        
        for account_number, user_details in database.items():
            if account_number == int(account_number_from_user):            
                if user_details[3] == password:
                    bank_operations(user_details)
                                    
            else:
                print("Invalid account or password hhhh")
                login()
                     
    else:
        init()
                
 
        
def register():
    print("****** Register ******")
    
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    email = input("What is your email address? \n")
    password = input("Create your password \n")
    
    try:
        account_number = generate_account_number()
        
    except ValueError:
        
        print("Account generation failed due to internet connection. Try again!")
        init()
        
    account_number = [first_name, last_name, email, password, 0]
         
    print("Your account has been created")
    print("== ==== ====== ===== ==")
    print("Your account number is: %d" % account_number)
    print("== ==== ====== ==== ==")
    
    login()

def bank_operations(user):
    
    print("Welcome %s %s " % (user[0], user[1]))
    
    selectedOption = int(input("What would you like to do? (1) Deposit (2) Withdrawal (3) Transfer (4) Complaints (5)current_balance (6) Logout \n"))
          
    if selectedOption == 1:
        deposit_operation(user)
            
    elif selectedOption == 2:
        withdrawal_operation(user)
            
    elif selectedOption == 3:
        transfer_operation(user)
           
    elif selectedOption == 4:
        complaints_operation(user)
        
    elif selectedOption == 5:
        current_balance(user)
           
    elif selectedOption == 6:
        logout()
            
    else:
        print("Invalid Option!")
        bank_operations(user)
        
            
def generate_account_number():
    return random.randrange(00000000000,9999999999) 

#['Onyii', 'Peace', 'peace@gmail.com', 'Peace', 500]
   
def deposit_operation(user):
    deposit = int(input("How much would you like to deposit? \n"))
    user[4] += deposit
    print(f"you have deposited {deposit} into your account")
    print(f"your current balance is {user[4]} ")
    
def current_balance(user):
        print(f"your current balance is {user[4]} ")
    

def withdrawal_operation(user):
    withdrawal = int(input("How much would you like to withdraw? \n"))
    user[4] -= withdrawal
    print("Take your cash.")
    print(f"your current balance is {user[4]} ")

    
    
def transfer_operation():
    transfer = int(input("How much would you like to transfer? \n"))
    user[4] -= transfer
    destination = int(input("account number you want to transfer to \n"))
    print(f"you transferred {user[4]} to  {destination}")

    
def complaints_operation():
    input("What issue will you like to report? \n")
    print("Thank you for contacting us.")
    
    
#clears all the session
def logout():
    login()
    
   
init()