total_units = int(input("Enter the total bill in units:"))
SUBCHARGE = 0.1

def subcharge(price_without_tax):
    return SUBCHARGE*price_without_tax + price_without_tax

def bill_calculation():
    if(total_units <= 300):
        if(total_units // 100 == 3):
            return (3*100) + (5*100) + (total_units - 200)*8
        if(total_units // 100 == 2):
            return (3*100) + (5*100) + (total_units%100)*8
        elif(total_units // 100 == 1):
            return (3*100) + (total_units%100)*5
        else:
            return (total_units%100)*3
    else:
        price_without_tax = (3*100) + (5*100) + (total_units - 200)*8
        return subcharge(price_without_tax)
def main():
    print(f"The total bill is: \u20B9{bill_calculation()}")

main()
