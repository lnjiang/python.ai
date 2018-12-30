import sys
import math
nterms = 1476

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
       count +=1
print (n1)
print ('aka %.6E' % n1)
print ("%dth number in the fibonacci sequence:" %(nterms+1))
print (n2)
print ('aka %.6E' % n2)

#to find the golden ratio:

print ("Ratio of two numbers: %f" %(n1/n2))

print ("golden ratio: %f" % ((math.sqrt(5)-1)/2))



print(sys.float_info.max)