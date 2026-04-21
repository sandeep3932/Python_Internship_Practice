import re
import sys

def stock_present_appleandorange(input, stock):
    if input in stock:
        print(f"{input} is in stock")
    else:
        print(f"{input} is not in stock")
   

def all_fruits_present(instock, outstock):
    all_fruits = set(instock) | set(outstock)
    print(f"{all_fruits}")
    for fruit in all_fruits:
        print(f"{fruit}")

def update_stock(instock, outstock, input):
    if input in outstock:
        outstock.remove(input)
    instock.add(input)
    print(f"Updated stock accordingly:\n"+
          f"in stock: {instock}\n"+
          f"out stock: {outstock}")
    



def main():
    in_stock = {'apple', 'watermelon', 'strawberry'}
    out_of_stock = {'banana', 'orange', 'guava'}
    for i in range(0,2):
        check_input = input("Enter the fruit you want to check is its in stock or not :")
        stock_present_appleandorange(check_input.lower(), in_stock)

    all_fruits_present(in_stock, out_of_stock)
    add_input = input("Enter the fruit you want to add in stock: ")
    update_stock(in_stock, out_of_stock, add_input)

main()