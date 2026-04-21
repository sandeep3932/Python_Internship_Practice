import re
def digits_in_string(s):
    digit_string = re.findall(r'\d', s)
    return digit_string

def main():
    input_string = input("Enter the string: ")
    if(len(digits_in_string(input_string)) > 0):
        print(f"The digits in the string is/are: {digits_in_string(input_string)}")
    else:
        print(f"There are no digits in the string")

main()
