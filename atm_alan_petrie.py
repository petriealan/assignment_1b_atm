"""
Assignment # 4 - ATM
Alan Petrie
This program asks the user for their PIN number.
"""
import random

def main():
    """
    Main function:
    Evaluates if a user entered PIN is correct
    """
    pin = 1234
    counter = 0
    max_tries = 3
    #Get PIN from user
    while True:
        try:
            user_pin = input('\nEnter PIN number: ')
        except EOFError:
            continue
        try:
            user_pin = int(user_pin)
        except ValueError:
            print('Invalid entry.  You must enter only digits.')
            user_pin = 0
            continue

        if user_pin == pin:
            balance = random.random() * 1000
            print(f'Your account balance is: ${balance:,.2f}')
            break
        else:
            counter += 1
            if counter == max_tries:
                print('Account locked.  The police are on their way.')
                break
            attempts_remaining = max_tries - counter
            if attempts_remaining == 1:
                print(f'Invalid PIN.  You have {attempts_remaining} attempt remaining.')
            else:
                print(f'Invalid PIN.  You have {attempts_remaining} attempts remaining.')


if __name__ == '__main__':
    main()
