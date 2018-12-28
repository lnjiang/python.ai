def testargument(a):
    print ("before increment id(a) = %d" %id(a))
    a +=1
    print ("after increment id(a) = %d" %id(a))
num = 9
print ("id(num) = %d" % id(num))
print ("before call f(x), num = %d" % num)
testargument(num)
print("id(num) = %d" % id(num))
print ("after call f(x), num = %d" % num)

def testargument_list(b):
    print ("before increment id(b) = %d" %id(b))
    b.append("turtle")
    print ("after increment id(b) = %d" %id(b))

mylist = ["dog", "cat"]
print("id(mylist) = %d" % id(mylist))
print("before call, my list = ", mylist)
testargument_list(mylist)
print("id(mylist)= %d" % id(mylist))
print("after call, mylist = ", mylist)