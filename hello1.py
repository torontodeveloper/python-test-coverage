import argparse

def say_hello(name:str,repeat:int=1,goodbye:bool=False) -> optional[str]:
    '''
    This function return given string repeated by repeat number if Goodbye set to False 
    and says Goodbye if Goodbye set to True
    Parameters
    ----------
    name:str
    repeat:int
    goodbye:bool
    
    Returns:
    --------
    None
    
    Example
    --------
    >>> say_hello('Angelina',repeat=2,goodbye=True)
    Example
    --------
    >>> say_hello('Salma',goodbye=True)
    Example
    --------
    >>> say_hello('Salma')
    '''
    if goodbye==True:
        message='Goodbye'
    else:
        message = 'Hello'
    for item in range(repeat):
        print(f'{message},{name}')
        
say_hello('Angelina',repeat=3,goodbye=True)
say_hello('Angelina',repeat=3,goodbye=False)