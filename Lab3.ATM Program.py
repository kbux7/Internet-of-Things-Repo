#Question 4: Create a simple ATM program.
#Start with:
#Balance = 50000
#Display:
#1. Check Balance
#2. Deposit
#3. Withdraw
#4. Exit
#Use a loop so the user can continue using the ATM until they select Exit.

balance = 50000
choice = 0

while (choice != 4):
    print('\nWelcome to our ATM Service!')
    print('Please select an option:')
    print('1. Check Balance')
    print('2. Deposit')
    print('3. Withdraw')
    print('4. Exit')

    choice = int(input('Enter your choice: '))
    if choice == 1:
        print(f'\nYour current balance is: {balance}\n')
    elif choice == 2:
        deposit_amount = float(input('\nEnter the amount to deposit: '))
        balance += deposit_amount
        print(f'\nYou have deposited {deposit_amount}\nNew balance is: {balance}\n')
    elif choice == 3:
        withdraw_amount = float(input('\nEnter the amount to withdraw: '))
        if withdraw_amount > balance:
            print('\nInsufficient funds.\n')
        else:
            balance -= withdraw_amount
            print(f'\nYou have withdrawn {withdraw_amount}\nNew balance is: {balance}\n')
    elif choice == 4:
        print('\nThank you for using our ATM. Goodbye!')
        break
    else:
        print('\nInvalid option. Please try again.\n')