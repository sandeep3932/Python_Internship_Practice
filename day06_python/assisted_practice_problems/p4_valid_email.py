import re

def is_valid_email(email):
    # Regex pattern for email validation
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Using fullmatch (cleaner than match + ^ $)
    if re.fullmatch(pattern, email):
        return True
    else:
        return False


def main():
    email = input("Enter an email address: ")
    
    if is_valid_email(email):
        print("Valid email")
    else:
        print("Invalid email")

main()