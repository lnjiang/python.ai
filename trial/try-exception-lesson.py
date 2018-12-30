import math
nterms = 2000

n1 = 0
n2 = 1
count = 0



if nterms <= 0:
    print("the number of terms has to be positive")
elif nterms == 1:
    print("%dth number in fibonacci sequence:" % (nterms))
    print(n1)
else:
    print("%dth number in fibonacci sequence:" % (nterms))
    while count < nterms:
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
    print(n1)
    try:
        print('aka %.6E' % n1)
    except OverflowError:
        print ("Thats a big number!")
    except:
        print ("something went wrong :(")
    print("%dth number in the fibonacci sequence:" % (nterms + 1))
    print(n2)
    try:
        print('aka %.6E' % n2)
    except OverflowError:
        print ("Thats an even BIGGER number!")
    except:
        print("something went wrong :(")