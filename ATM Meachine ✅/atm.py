# Creating empty lists for users, their PINs, and bank statements
users = []
pins = []
amounts = []
withdrawals = []
lodgements = []

# Function to add a new user
def add_user():
    user_name = input("Enter the user name: ")
    pin = input("Enter the pin: ")
    amount = float(input("Enter the amount: "))
    users.append(user_name)
    pins.append(pin)
    amounts.append(amount)
    withdrawals.append(0)  # Initialize withdrawals to zero
    lodgements.append(0)   # Initialize lodgements to zero

# Adding an initial user for demonstration
add_user()

count = 0

# While loop checks existence of the entered username
while True:
    user = input('\nENTER USER NAME: ').lower()
    if user in users:
        n = users.index(user)
        break
    else:
        print('----------------')
        print('INVALID USERNAME')
        print('----------------')

# Comparing pin
while count < 3:
    print('------------------')
    pin = input('PLEASE ENTER PIN: ')  # Replaced getpass.getpass with input
    print('------------------')
    if pin.isdigit() and len(pin) == 4:
        if user == users[n]:
            if pin == pins[n]:
                break
            else:
                count += 1
                print('-----------')
                print('INVALID PIN')
                print('-----------')
                print()
        else:
            count += 1
            print('-----------')
            print('INVALID PIN')
            print('-----------')
            print()
    else:
        print('------------------------')
        print('PIN CONSISTS OF 4 DIGITS')
        print('------------------------')
        count += 1

# In case of a valid pin- continuing, or exiting
if count == 3:
    print('-----------------------------------')
    print('3 UNSUCCESSFUL PIN ATTEMPTS, EXITING')
    print('!!!!!YOUR CARD HAS BEEN LOCKED!!!!!')
    print('-----------------------------------')
    exit()

print('-------------------------')
print('LOGIN SUCCESSFUL, CONTINUE')
print('-------------------------')
print()
print('--------------------------')
print(str.capitalize(users[n]), 'welcome to ATM')
print('----------ATM SYSTEM-----------')

# Main menu
while True:
    print('-------------------------------')
    response = input('SELECT FROM FOLLOWING OPTIONS: \nStatement__(S) \nWithdraw___(W) \nLodgement__(L)  \nChange PIN_(P)  \nQuit_______(Q) \n: ').lower()
    print('-------------------------------')
    valid_responses = ['s', 'w', 'l', 'p', 'q']
    if response == 's':
        print('---------------------------------------------')
        print('ACCOUNT STATEMENT')
        print('---------------------------------------------')
        print(f"User Name: {str.capitalize(users[n])}")
        print(f"Account Balance: {amounts[n]} RUPEES")
        print(f"Total Withdrawals: {withdrawals[n]} RUPEES")
        print(f"Total Lodgements: {lodgements[n]} RUPEES")
        print('---------------------------------------------')
    elif response == 'w':
        print('---------------------------------------------')
        cash_out = int(input('ENTER AMOUNT YOU WOULD LIKE TO WITHDRAW: '))
        print('---------------------------------------------')
        if cash_out % 10 != 0:
            print('------------------------------------------------------')
            print('AMOUNT YOU WANT TO WITHDRAW MUST BE IN MULTIPLES OF 10 RUPEES')
            print('------------------------------------------------------')
        elif cash_out > amounts[n]:
            print('-----------------------------')
            print('YOU HAVE INSUFFICIENT BALANCE')
            print('-----------------------------')
        else:
            amounts[n] -= cash_out
            withdrawals[n] += cash_out  # Record the withdrawal amount
            print('-----------------------------------')
            print('YOUR NEW BALANCE IS: ', amounts[n], 'RUPEES')
            print('-----------------------------------')
    elif response == 'l':
        print()
        print('---------------------------------------------')
        cash_in = int(input('ENTER AMOUNT YOU WANT TO LODGE: '))
        print('---------------------------------------------')
        print()
        if cash_in % 10 != 0:
            print('----------------------------------------------------')
            print('AMOUNT YOU WANT TO LODGE MUST BE IN MULTIPLES OF 10 RUPEES')
            print('----------------------------------------------------')
        else:
            amounts[n] += cash_in
            lodgements[n] += cash_in  # Record the lodgement amount
            print('----------------------------------------')
            print('YOUR NEW BALANCE IS: ', amounts[n], 'RUPEES')
            print('----------------------------------------')
    elif response == 'p':
        print('-----------------------------')
        new_pin = input('ENTER A NEW PIN: ')
        print('-----------------------------')
        if new_pin.isdigit() and new_pin != pins[n] and len(new_pin) == 4:
            print('------------------')
            new_ppin = input('CONFIRM NEW PIN: ')
            print('-------------------')
            if new_ppin != new_pin:
                print('------------')
                print('PIN MISMATCH')
                print('------------')
            else:
                pins[n] = new_pin
                print('NEW PIN SAVED')
        else:
            print('-------------------------------------')
            print('   NEW PIN MUST CONSIST OF 4 DIGITS \nAND MUST BE DIFFERENT TO PREVIOUS PIN')
            print('-------------------------------------')
    elif response == 'q':
        exit()
    else:
        print('------------------')
        print('RESPONSE NOT VALID')
        print('------------------')
