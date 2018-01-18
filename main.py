from atm_machine import ATMMachine
import sys


def main():
    options = ['Show current balance status', 'Withdraw amount', 'Exit']
    atm = None
    currency, notes_dict, sum_notes = initialise_atm_attributes()

    while True:
        print('\nPlease pick one of the below choices:')
        for idx, option_text in enumerate(options):
            print(str(idx+1) + ": " + option_text)

        choice = input()

        if choice == '3':
            sys.exit()

        if not atm:
            atm = ATMMachine(notes_dict, sum_notes, currency)

        if choice == '1':
            print(atm)
        elif choice == '2':
            amount = input('Please enter the amount you want to withdraw: ')
            while not amount.isdigit():
                print('Please provide a valid number')
            atm.withdraw(int(amount))
        else:
            print('Please use one of the available options:')


def initialise_atm_attributes():
    notes_dict = {20: 100, 50: 75}
    sum_notes = 5750
    currency = '$'
    return currency, notes_dict, sum_notes


main()
