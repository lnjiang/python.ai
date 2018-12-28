def fibonacci (n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci (n-1) + fibonacci (n-2)

x = 15

print("the %dth fibonacci number is %d" %(x, fibonacci(x)))