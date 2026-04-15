def calculate_sum(x: int, y: int):
    """
    returns sum of two numbers
    """
    return x + y

initial_points = 10
bonus_points = 50

print(f"Data type of initial points{type(initial_points)} and \n" + 
      f"Data type of bonus points{type(bonus_points)}")
total_points = calculate_sum(initial_points, bonus_points)
print(f"total points are : {total_points}")