APPLE_GST = 0.12
ORANGE_GST = 0.05
APPLE_ITEMCODE = "apple"
ORANGE_ITEMCODE = "orange"

def total_apple_price(apple_price_perkg: float, apple_quantity_kg: float):
    return apple_price_perkg * apple_quantity_kg

def total_orange_price(orange_price_perkg: float, orange_quantity_kg: float):
    return orange_price_perkg * orange_quantity_kg

def total_apple_pricegst(apple_price_perkg: float, apple_quantity_kg: float):
    return total_apple_price(apple_price_perkg, apple_quantity_kg) * (1 + APPLE_GST)

def total_orange_pricegst(orange_price_perkg: float, orange_quantity_kg: float):
    return total_orange_price(orange_price_perkg, orange_quantity_kg) * (1 + ORANGE_GST)

def total_amount():
    return total_apple_pricegst(apple_price_perkg, apple_quantity_kg) + total_orange_pricegst(orange_price_perkg, orange_quantity_kg)

buyer_name = str(input("Enter the name of the buyer: "))
apple_price_perkg = float(input("Enter price of an apple per kg: "))
orange_price_perkg = float(input("Enter price of an orange per kg: "))
apple_quantity_kg = int(input("Enter quantity of apples in kg: "))
orange_quantity_kg = float(input("Enter quantity of orange in kg: "))

def display_bill():
    print(f"Buyer Name: {buyer_name}")
    print(f"{'-'*74}")
    print(f"|{'Item Code':^10}|{'Price/Unit':^10}|{'unit':^10}|{'price':^10}|{'GST':^10}|{'Total w/ GST':^10}|")
    print(f"{'-'*74}")
    print(f"|{APPLE_ITEMCODE:^10}|{'Rs '+ str(apple_price_perkg):^10}|{apple_quantity_kg:^10}|{'Rs ' + str(total_apple_price(apple_price_perkg, apple_quantity_kg)):^10}|{'Rs ' + str(APPLE_GST):^10}|{'Rs ' + str(float(total_apple_pricegst(apple_price_perkg, apple_quantity_kg))):^10}|")
    print(f"|{ORANGE_ITEMCODE:^10}|{'Rs ' + str(orange_price_perkg):^10}|{orange_quantity_kg:^10}|{'Rs ' + str(total_orange_price(orange_price_perkg, orange_quantity_kg)):^10}|{'Rs ' + str(ORANGE_GST):^10}|{'Rs '+ str(float(total_orange_pricegst(orange_price_perkg, orange_quantity_kg))):^10}|")
    print(f"{'-'*74}")
    print(f"Total Round{' ' * 54} \u20B9 {total_amount()}")
    print(f"Total Round{' '*54} \u20B9 {total_amount():.2f}")

display_bill()