def calculate_sum(x: int, y: int):
    return x + y
try :
    initial_points = int(input("Enter value for initial points:"))
    bonus_points = int(input("Enter value for bonus points:"))
    print(f"Data type of initial points is: {type(initial_points)} and \n" +
        f"data type of bonus points is: {type(bonus_points)}")
    total_points = calculate_sum(initial_points, bonus_points)
    print(f"The total points are : {total_points}")
except ValueError as err:
    print(f"You have an error and the error is:{err}. Try again with correct value")
except:
    print(f"Try again and give proper input")



