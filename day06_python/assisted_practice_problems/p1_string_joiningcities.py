def join_with_uppercase():
    places_list = []
    for i in range(1, 6):
        places = str(input(f"Enter the name of the place {i}: "))
        places_list.append(places)
        
    print(f"Places stored in list: {places_list}")
    print(f"All places saperated by comma and space and in uppercase: {', '.join(places_list).upper()}")

def main():
    join_with_uppercase()

main()