def f(n):
    '''this is a recursive function to find the factorisl of an integer'''
    if n==0 or n==1:
        return 1
    else:
        return n*f(n-1)
    print(f.__doc__)
print("the factorial of 5:", f(5))
print("the factorial of 11:", f(11))
print("the factorial of 8:", f(8))
print("the factorial of 24:", f(24))