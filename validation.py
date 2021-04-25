def account_number_validation(account_number):
    
    if account_number:
        
        if len(str(account_number)) == 10:
            
            try:
                int(account_number)
                return True
            except ValueError:
                print("Invalid Account number")
                return False
            except TypeError:
                print("Invalid account type")
                return False
         
        else:
            print("Account number cannot be more or less than 10 digits!")
            return False
            
    else:
        print("Account number required")
        return False
     