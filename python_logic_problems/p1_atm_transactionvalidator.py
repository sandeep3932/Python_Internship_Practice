initial_balance = float(input("Enter the Initial Balance:"))
withdrawl_requests = int(input("Enter the number of withdrawls you want to make:"))

def validate_withdrawal(withdrawl_amount, initial_balance):
    if(initial_balance - withdrawl_amount > 0 and withdrawl_amount % 100 == 0):
        print(f"SUCCESS")
        return process_transaction(initial_balance, withdrawl_amount)
    else:
        print(f"FAILED")
        return initial_balance
def process_transaction(initial_balance, withdrawl_amount):
    return initial_balance - withdrawl_amount

def run_all_requests(initial_balance, withdrawl_requests):
    for i in range(withdrawl_requests):
        withdrawl_amount = int(input("Enter the amount you want to withdraw:"))
        initial_balance = validate_withdrawal(withdrawl_amount, initial_balance)
    return initial_balance



def main():
    print({run_all_requests(initial_balance, withdrawl_requests)})
    

main()



