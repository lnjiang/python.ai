# I M DYING :(
# ANYWAY
# there is a bank giving you an APR 6% for your savings account. If you have $1 at the beginning,
# find how much you will have after 10 years
import math

apr = 0.06
init = 1.0
sum1 = 1.0
for y in range (1,13):
    sum1 *= (1.0 + apr)
print ("sum1 from for loop is %f" % sum1)

numyears=1000000
NUM = range (1 , numyears + 1)
SUM = 1.0
APR = 1.0/numyears
for y in NUM:
    SUM *= (1.0 + APR)
    print ("After year %d, the value is %f" %( y, SUM))

print (math.e)