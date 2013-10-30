n = 0
while n < 101:
    if n % 3 == 0 and n % 5 == 0:
        print str(n) + " FizzBuzz"
    elif n % 3 == 0:
        print str(n) + " Fizz"
    elif n % 5 == 0:
        print str(n) +" Buzz"
    else:
        print str(n)
    n = n+1