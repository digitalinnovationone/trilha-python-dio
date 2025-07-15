
#=== Banking System Challenge ===

user_name = ''
password = ''
name = ''
cpf = 0
birthday = ''
address = ''
new_user = {}
all_users = []
balance = 0
withdraw_times = 0
extract = []
accounts = []
WITHDRAW_LIMIT = 500
WITHDRAW_TIMES_LIMIT = 3

def logout(): #=== Function to logout user ===
        print('''
                Logging out!''')
        global account_menu, menu_loop
        menu_loop = False
        account_menu = False

def ask_menu(): #=== Function to ask if the user wants to continue or end system ===
    toDo = int(input('''      
            What do you want to do?
                    
                1. for menu
                2. for end
                    
            '''))
    if (toDo == 1):
        global menu_loop
        menu_loop = True
    elif (toDo == 2):
        print('''
            Thanks for using FuBank system! See you later!''')
        exit()    

def withdraw(balance: int, extract: list, withdraw_limit: int, withdraw_times: int, withdraw_times_limit: int, withdraw_value: int) -> tuple:
    if withdraw_value <= 0: #=== Function to withdraw money ===
        print('''
            Please enter a positive value.              
            ''')
        return
    elif (withdraw_value > balance or withdraw_value > withdraw_limit or withdraw_times >= withdraw_times_limit):
        print('''
            Unauthorized transaction              
            ''')
        return
    else:
        balance -= withdraw_value
        withdraw_times += 1
        extract.append(f'''
            Withdraw: R$ -{withdraw_value}
            Balance: R$ {balance}''')
        print(f'''
            Successful withdraw! Your balance: R$ {balance}
            ''')
        return balance, extract, withdraw_times

def deposit(deposit_value, balance, extract): #=== Function to deposit money ===  
    if deposit_value <= 0:
        print('Please enter a positive value.')
        return
    else:
        balance += deposit_value
        extract.append(f'''
            Deposit: R$ +{deposit_value}
            Balance: R$ {balance}''')
        print(f'''                      
            Successful deposit! Your balance: R$ {balance}''')    
        return balance, extract

while True: #=== Main system loop ===
    current_user = {}
    account_menu = True
    login = True
    menu_loop = True

    #=== Login page Loop ===

    while(login):
        welcome = int(input('''
                Hello, welcome to the FuBank!
                1. for login
                2. for register
                        
                '''))

        if (welcome == 1):
            user_name = input('''
                Username: ''')
            password = input('''
                Password: ''')
            if (user_name == "" or password == ''):
                print('''
                Please enter a valid username and password.''')
            elif (user_name and password):
                found = False
                for user in all_users:
                    if user_name == user['user_name'] and password == user['password']:
                        print('''
                Login successful!''')
                        found = True
                        login = False
                        current_user = user
                        break

                if not found:
                    print('''
                Invalid username or password.''')
                    continue
            
        elif (welcome == 2):
            user_name = input('''
                Choose a username: ''')
            password = input('''
                Choose a password: ''')
            name = input('''
                Complete name: ''')
            cpf = input('''
                CPF: ''')
            birthday = input('''
                Birthday(dd/mm/yy): ''')
            address = input('''
                Address(st - num - district - city / state): ''')
            if (user_name and password and name and cpf and birthday and address):
                new_user = {
                    'user_name': user_name,
                    'password': password,
                    'name': name,
                    'cpf': cpf,
                    'birthday': birthday,
                    'address': address,
                }
                print('''
                User registered successfuly!''')
                all_users.append(new_user)            
                continue
            else:
                print('''
                Please fill in all fields.''')
                continue
        
        else:
            print('''
                Please enter a valid option.''')
            continue

    #=== Login page Loop End ===

    #=== Account Menu Loop ===

    while(account_menu): 
        current_account = {}
        if (current_user):
            try:
                menu = int(input(f'''     
                Hello {current_user['name'].split()[0]}! Chose one number:

                    1. for Enter an existent account
                    2. for Create a new account
                    3. for Logout
                    4. for End
                    
                ''')
            )
            except ValueError:
                print('''
                Please enter a valid number.''')    
                continue 

            if (menu == 1): #=== Enter an existent account option ===
                if not accounts:
                    print('''
                You have no accounts yet! Please create one.''')
                    continue
                current_account = int(input('''
                Agency: 0001
                Choose an account number: '''))
                if current_account < 0:
                    print('''
                Invalid account number.''')
                    continue
                else:
                    current_user.update(accounts[current_account - 1])
                    break

            elif (menu == 2): #=== Create a new account option ===
                account_number = len(accounts) + 1
                accounts.append({
                    'agency': '0001',
                    'account_number': account_number,
                    'user_name': current_user['user_name'],
                    'balance': 0,
                    'withdraw_times': 0,
                    'extract': []
                })
                print(f'''
                Account created successfuly!
                Your agency is: 0001
                Your account number is: {account_number}''')
                continue
            
            elif (menu == 3): #=== Logout option ===
                logout()
                                        
            elif (menu == 4): #=== End option ===
                print('''
                Thanks for using FuBank system! See you later!''')
                exit()

            else:    
                print('''
                Please chose one valid option''')
                continue

    #=== Account Menu Loop End ===            

    #=== Main account Menu Loop ===

    while (menu_loop):
        if (current_user):
            try:
                menu = int(input(f'''     
                Welcome to account number {current_user['account_number']}! Choose one number:

                    1. for Extract
                    2. for Withdraw
                    3. for Deposit
                    4. for Logout
                    5. for End

                ''')
            )
            except ValueError:
                print('''
                Please enter a valid number.''')    
                continue 
            if (menu == 1): #=== Extract option ===
                print(f'''  
                {''.join(current_user['extract'])}     
                                ''')
                ask_menu() 
            
            elif (menu == 2): #=== Withdraw option ===
                try:
                    withdraw_value = int(input('''
                Value: R$ '''))
                except ValueError:
                    print('''
                Please enter a valid number.''')
                    continue
                result = withdraw(current_user['balance'], current_user['extract'], WITHDRAW_LIMIT, current_user['withdraw_times'], WITHDRAW_TIMES_LIMIT, withdraw_value)
                if result:
                    current_user['balance'], current_user['extract'], current_user['withdraw_times'] = result
                    ask_menu()

            elif (menu == 3): #=== Deposit option ===
                try:
                    deposit_value = int(input('''
                Value: R$ '''))
                except ValueError:
                    print('''
                Please enter a valid number.''')                       
                    continue

                result = deposit(deposit_value, current_user['balance'], current_user['extract'])
                if result:
                    current_user['balance'], current_user['extract'] = result
                    ask_menu()

            elif (menu == 4): #=== Logout option ===
                logout()
                        
            elif (menu == 5): #=== End option ===
                print('''
                Thanks for using FuBank system! See you later!''')
                exit()

            else:    
                print('''
                Please chose one valid option''')
                continue