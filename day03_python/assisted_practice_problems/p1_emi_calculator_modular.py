MONTHS_IN_YEAR = 12


def calculate_interest(principle: float, roi: float, frequency: int = 12) -> float:
    return round(principle * roi / (frequency * 100), 2)


def calculate_monthly_emi(principle: float, roi: float, time: int) -> float:
    interest_per_month = calculate_interest(1, roi)
    months = time * MONTHS_IN_YEAR

    emi = (
        principle
        * interest_per_month
        * (1 + interest_per_month) ** months
        / ((1 + interest_per_month) ** months - 1)
    )
    return emi


def generate_emi_schedule(principle: float, roi: float, time: int):
    emi = calculate_monthly_emi(principle, roi, time)
    balance = principle
    emi_details = []

    for month in range(1, time * MONTHS_IN_YEAR + 1):
        interest = calculate_interest(balance, roi, 12)
        principal = emi - interest
        balance = balance - principal

        if balance < 0:
            principal = round(principal + balance, 2)
            emi = round(principal + interest, 2)
            balance = 0

        emi_dict = {
            "Month": month,
            "EMI": round(emi, 2),
            "Interest": round(interest, 2),
            "Principal": round(principal, 2),
            "Balance": round(balance, 2),
        }

        emi_details.append(emi_dict)

    return emi_details


def display_emi_schedule(emi_details):
    print(f"{'-'*70}")
    print(f"| {'Month':^6} | {'EMI':^10} | {'Interest':^10} | {'Principal':^10} | {'Balance':^10} |")
    print(f"{'-'*70}")

    total_emi = total_interest = total_principal = 0

    for emi_dict in emi_details:
        print(
            f"| {emi_dict['Month']:^6} | {emi_dict['EMI']:^10} | {emi_dict['Interest']:^10} | {emi_dict['Principal']:^10} | {emi_dict['Balance']:^10} |"
        )

        total_emi += emi_dict["EMI"]
        total_interest += emi_dict["Interest"]
        total_principal += emi_dict["Principal"]

    print(f"{'-'*70}")
    print(
        f"| {'TOTAL':^6} | {total_emi:^10.2f} | {total_interest:^10.2f} | {total_principal:^10.2f} | {'-':^10} |"
    )
    print(f"{'-'*70}")


def main():
    principle = float(input("Enter Principle Amount: "))
    roi = float(input("Enter Rate of Interest (%): "))
    time = int(input("Enter Time (in years): "))

    emi_details = generate_emi_schedule(principle, roi, time)
    display_emi_schedule(emi_details)


main()