#how to define a function 
'''you start by typing the keyboard def followed by the name of the function and then parentheses with a list of parameters separated by commas. last you add a colon after the close parenthesis and indent the next line for the body of the function '''
def f(x):
    return 2 * x + 3

     ''' The above Function is name f. It takes one parameter which should be a number. The function returns twice the parameters plus 3'''

    '''once a function is defined, you can use it by calling it. To call a function, you must use the function's name followed by parenthesis with the argument
    of the function enclosed in them. arguments are literals, object, expressions or return-values 
    function calls that takes the place of the parameters in the function definition. The arguments are associated with the parameter in the same position as them in.Hence, the first argument is associated
    with the first parameters'''

#function call with a literal 
print f(2) #return 7

#function call with an expression 
print f(3+ 4 * 6) #return 57

#funuction call with a function call 
print f(f(6)) #returns 33

v= 89
#function call with a variable 
print f(v) #return 181


'''Task 1:  Define a Function that takes two parameters. It returns the greater of the two parameters. Assume that the parameters are numbers '''

def greater(x,y):
    if x >= y: 
        return x
else:
    return y 

x= float(raw_input("Enter first number: "))
y= float(raw_input("Enter second number:")) 


'''Task 2: Define a function that takes no parameters. it prompts the user to enter a string. Afterwards , it  returns the string concatenated with itself'''


''' task 3 '''

def Display3(x,y,z);
    v = x*y*z+3
    print values

Display3(2,3,4)


#list
''' what is a list '''
''' a list is an ordeed collections of objects'''
'''you access the elemnts of a list with an index which is a interger'''

#creating a list 
l = []

k = list()

j = [1,2,3,4,5,6,7,8,9,10]

#list methods
print "l =",l
print "k =",k
print "j =",j


l.insert(0,'h')
k.insert(0,'a')
j.insert(5,12)



print "l =",l
print "k =",k
print "j =",j


l.remove('a')
k.remove('a')
j.remove(5)



l = (2,3,6,7)
k =(4,1,5,12,13)




l.insert(0,'h')
k.insert(0,'a')
j.insert(5,12)

#loop
l = l 
while i <= 10:
    print i
    i+=i 

i = 1 
while i <= 20:
    print i
    i+=i
    

for i in
    print i

h[i] = 
fir i in range(2,20):

# dictionary
d =
b = 
a =
c =


# object 


class person:
    def __init__(self,name):
        self.name = name
        self.age = 0

def birthday(self):
    self.age = +=1

t =  person("jane doe")

print t.name , t.age 


s = person("roger sam")
print s.name,s.age

t.birthday()

print t.name,t.age 