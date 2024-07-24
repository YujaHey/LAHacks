import random

MAX_LINES = 3 #global constant in all caps
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

#function asks user for how much they want to deposit
def deposit():
    #continuously ask for their input until valid input is given
    while True:
        amount = input("Enter your desposit amount: $")

        #check if amount is actually a number
        if amount.isdigit():
            amount = int(amount)
            #when amount is greater than 0, the while loop will return "amount"
            if amount > 0:
                break
            else: 
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number")
    
    return amount

#ask user the lines they want to bet on
def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines you want to bet on (1 to "+str(MAX_LINES)+") ")
        if lines.isdigit():
            lines = int(lines)
            if MAX_LINES >= lines >= 1:
                break
            else: 
                print("Amount must be between 1 and "+str(MAX_LINES))
        else:
            print("Please enter a number")
    return lines

def get_bet():
    while True:
        bet = input("Enter your bet amount: $")
        if bet.isdigit():
            bet = int(bet)
            if MAX_BET >= bet >= MIN_BET:
                break
            else: 
                print(f"Amount must be between ${MIN_BET} to ${MAX_BET}")
        else:
            print("Please enter a number")
    return bet

def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet*lines

        if total_bet > balance:
            print(
                f"\nYou do not have enough to bet ${total_bet}, your balance is ${balance}")
        else:
            break
    print(f"You are betting {bet} on {lines} lines. Total bet is equal to ${total_bet}")

if __name__ == "__main__":
    main()