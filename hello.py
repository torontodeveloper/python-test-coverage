import argparse

parser = argparse.ArgumentParser(description='Angelina')

parser.add_argument('name')
parser.add_argument('-r',type=int,default=1)
args = parser.parse_args()

for item in range(args):
    print('hello',args.name)
    
def say_hello(name:str)->None:
    """This is hello world function

    Args:
        name (str): name of the string u wanna repeat
    """    