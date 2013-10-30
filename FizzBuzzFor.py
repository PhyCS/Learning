for i in range(101):
    if i % 3 == 0 and i % 5 == 5:
        print str(i) + " FizzBuzz"
    elif i % 3 == 0:
        print str(i) + " Fizz"
    elif i % 5 == 0:
        print str(i) + " Buzz"
    else:
        print str(i)
    i = i + 1