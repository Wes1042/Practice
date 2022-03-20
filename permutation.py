

def factorial(num):
    """own function for factoring"""

    factorial = 1
    if num < 0 :
        print("Factorials cant be negative numbers")
    else:    
        for i in range(1,num + 1):
            factorial = factorial * i
            
    return factorial



#combination is amount of numbers that do not combine more than once
def combination(n,r):
    """This will solve for a number in probability for """
    n_factorial = factorial(n)
    r_factorial = factorial(r)
    diff = n - r
    diff_factorial = factorial(diff)
    total = n_factorial / (diff_factorial * r_factorial)

    print(int(total))
    #    n! 
    # ------
    # (n - r)!* r!

# Permutation is amount of numbers that can be combined together including more than once
def permunation(n,r):
    """This will solve for a number in probability"""
    n_factorial = factorial(n)
    diff = n - r 
    r_factorial = factorial(diff)
    total = n_factorial / r_factorial
    print (int(total))

    #  n!
    #------
    # (n-r)!

combination(5,2)
#permunation(5,4)
