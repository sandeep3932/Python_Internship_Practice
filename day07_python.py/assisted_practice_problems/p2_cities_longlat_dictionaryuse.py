def valid_city(city, cities):
    if city in cities:
        lat, lon = cities[city]
        return f"{city}: latitute :{lat}, longitude:{lon}"

def main():
    cities = {
        "mumbai": (19.076, 72.8777),
        "bangalore": (12.9716, 77.5946),
        "chennai": (13.0827, 80.2707),
        "pune": (18.5204, 73.8567),
        "hyderabad": (17.385, 78.4867)
    }
  
  
    while True:
        user_input = input("Enter the name of the city:")
        if user_input.lower() == "exit":
            print(f"You have exitted the system")
            break
        else:
            print(f"{valid_city(user_input.lower(), cities)}")

main()