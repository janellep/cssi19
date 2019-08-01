def countToN(num):

    #num will be asigned 
    #the absolute value of 
    #itself 

    num = abs(num)
    for i in range(1,num+1):
        print i 

    




n = raw_input("Enter an integer:\n")
n = int(n)

countToN(n)

def Factors(num):
    num = abs(num)
    l = [] #list()
    for i in range(1,num+1):

        if num % i == 0: 
            l.append(i)

    return l

print Factors(n)