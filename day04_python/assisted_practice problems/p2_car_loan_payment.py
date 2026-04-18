MONTHS_IN_YEAR = 12
def rate_per_month(R):
    r = R/(12*100)
    return r

def monthly_car_loan_payment(P, Y, R):
    n = Y*12
    r = rate_per_month(R)
    payment = (P * r)/(1 - (1 + r) ** (-n))
    return payment


principal_amount = float(input("Enter the principal amount:"))
duration = float(input("Enter the number of years:"))
rate_of_interest = float(input("Enter the rate of interest annually:"))
total_months = duration*MONTHS_IN_YEAR

def main():
    print(f"Payment per month is:" + f"{str(monthly_car_loan_payment(principal_amount, duration, rate_of_interest))}")

main()


