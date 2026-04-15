PI = 22/7
def caluculate_area(x: int):
    """
    returns the area of a circle with a given radius
    """
    return PI * x ** 2


radius = int(input("Enter the radius of the circle:"))
circle_area = caluculate_area(radius)
print(f"the data type of radius is : {type(radius)}")
print(f"the area of the circle with the given radius is: {circle_area}")

