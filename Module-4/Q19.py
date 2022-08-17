
# How Do You Handle Exceptions With Try/Except/Finally In Python?Explain with coding snippets
"""
# Except() 
def divide(x, y):
    try:
        # Floor Division : Gives only Fractional
        # Part as Answer
        result = x // y
        print("Yeah ! Your answer is :", result)
    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero ")
   
# Look at parameters and note the working of Program
divide(3, 2)
divide(3, 0)


Output:
Yeah ! Your answer is : 1
Sorry ! You are dividing by zero 

"""

"""

#Finally

def divide(x, y):
    try:
        # Floor Division : Gives only Fractional
        # Part as Answer
        result = x // y
    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero ")
    else:
        print("Yeah ! Your answer is :", result)
    finally: 
        # this block is always executed  
        # regardless of exception generation. 
        print('This is always executed')  
 
# Look at parameters and note the working of Program
divide(3, 2)
divide(3, 0)



Output:
Yeah ! Your answer is : 1
This is always executed
Sorry ! You are dividing by zero 
This is always executed

"""