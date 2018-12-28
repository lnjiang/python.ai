# calculate factorial using recursive function
n = 100
fact = 1
def factorial (num):
    product = 1
    for x in range(1, num + 1):
        product *= x
    return product
num = 100

print ("{}! = {}".format(num, factorial(num)))

"""Using a recursive function:"""

def recursive_factorial(n):

    if n == 1:
        return 1
    else:
        return n * recursive_factorial(n-1)

print ("{}! = {}".format(num, recursive_factorial(num)))

print ("done")
