def is_baby_boomer(x: int):
    """
    returns baby boomer or not
    """
    if x >= 1946 and x < 1964:
        return True
    else:
        return False
def is_gen_x(x: int):
    """
    returns gen x or not
    """
    if x >= 1965 and x < 1980:
        return True
    else:
        return False
def is_millenial(x: int):
    """
    returns millenial or not
    """
    if x >= 1981 and x < 1996:
        return True
    else:
        return False
def is_generation_z(x: int):
    """
    returns generation z or not
    """
    if x>= 1997 and x < 2012:
        return True
    else:
        return False
def is_generation_alpha(x: int):
    """
    returns generation alpha or not
    """
    if x >= 2013 and x < 2025:
        return True
    else:
        return False

try:  
    birth_year = int(input("Type the birth year of the person:"))

    print(f"Birth Year is {birth_year}")
    print(f"Is Baby Boomer: {is_baby_boomer(birth_year)}\n" +
        f"Is Gen X: {is_gen_x(birth_year)}\n" +
        f"Is Millennial: {is_millenial(birth_year)}\n" +
        f"Is Gen Z: {is_generation_z(birth_year)}\n" +
        f"Is Gen Alpha: {is_generation_alpha(birth_year)}\n")
except ValueError as err:
    print(f"Please re enter the value, the value is incorrect: {err}")
except:
    print(f"Please give the correct input")
"""
without writing functions directly with print statements, shorter code
"""
print(f'\nBirth Year is {birth_year}',
f'Is Baby Boomer: {birth_year > 1946 or birth_year == 1946 and birth_year < 1964}',
f'Is Gen X: {birth_year >= 1965 and birth_year < 1980}',
f'Is Millennial: {birth_year >= 1981 and birth_year < 1996}',
f'Is Gen Z: {birth_year >= 1997 and birth_year < 2012}',
f'Is Gen Alpha: {birth_year >= 2013 and birth_year < 2025}', sep = '\n')

    





        
    
