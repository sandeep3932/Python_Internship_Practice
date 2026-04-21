import sys
import timeit

# Create list and tuple
list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tuple_numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Measure memory size
tuple_size = sys.getsizeof(tuple_numbers)
list_size = sys.getsizeof(list_numbers)

print(f"Size of tuple: {tuple_size} bytes")
print(f"Size of list: {list_size} bytes")

# Measure creation time
tuple_time = timeit.timeit(lambda: (1,2,3,4,5,6,7,8,9,10), number=1000000)
list_time = timeit.timeit(lambda: [1,2,3,4,5,6,7,8,9,10], number=10000000)

print(f"Tuple creation time: {tuple_time} seconds")
print(f"List creation time: {list_time} seconds")