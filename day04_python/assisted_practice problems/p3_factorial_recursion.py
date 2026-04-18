def factorial(n: int):
    product = 1
    if n == 0:
        return 1
    else:
        for i in range(1, n+1):
            product = product * i

        return product

number = int(input("Enter the number you want factorial of:"))

def main():
    print(f"Factorial of {number} is {factorial(number)}")

main()