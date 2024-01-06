
# try:
#     age = int(input('plz enter user'))
# except ValueError as error:
#      raise ValueError('plz enter proper string value that can be typecast to int')
# print(f'user is {age}')
import math
def calc_area(radius:float)->float:
    """calculate area of circle or shape

    Args:
        radius (float): radius

    Returns:
        float: area of circle or shape
    """    
    if radius<0:
        # raise ValueError("Radius can't be negative")
        pass
    area = math.pi*2**radius
    return area

area = calc_area(-9)
assert area > 1, print('sorry, area is not positive')

print(f'area is {area}')
