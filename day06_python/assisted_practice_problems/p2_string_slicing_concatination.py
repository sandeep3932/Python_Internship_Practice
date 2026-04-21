def slice_string(input_string):
    return input_string[:1:-2]
    """
    in the brackets[start:stop:step]
    step is the direction , if its -2 its going to skip every other element and 
    go in reverse direction which - indictated, here the stop index is not included
    """
    
def concatinate_start_middle_endchar(input_string):
    return input_string[0] + input_string[len(input_string)//2] + input_string[-1]
def main():
    input_string = input(str("Enter the String you want to slice/concatinate: "))
    print(f"Reversed reverse is: {slice_string(input_string)}")
    print(f"concatinated string is: {concatinate_start_middle_endchar(input_string)}")

main()