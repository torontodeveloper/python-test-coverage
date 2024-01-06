import math

def calculate_square(side:int) -> float:
    '''calcualte the square of shape 
    '''
    return side**2

def calcualte_area_circle(radius:int)->float:
    # if radius<0:
    #     raise ValueError(f'side should be >0, got negative')
    area = math.pi * radius **2
    return area
    