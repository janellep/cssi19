der Greetings(name):
    print "Hello,",name

    def echo():
        response = raw_input('Enter a string?'):
        print response + '/n' + response

echo()

#fizzbuzz translation
def FizzBuzz(num):
    if num % 3 is 0 and num % 5 is 0:
        print 'FizzBuzz'
    elif num % 3 is 0:
            print 'Fizz'
    elif num % 5 is 0:
            print 'Buzz'
    else:
            print num
            
        fizzbuzz(9)
        fizzbuzz(10)
        fizzbuzz(30)
        fizzbuzz(7)
