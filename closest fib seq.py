# formula for fibonacci
def fibs():
    a,b = 0,1
    yield a
    yield b
    while True:
        a,b = b,a+b
        yield b

def nearest_fib(n):

    for fib in fibs():
        if fib == n:
            return True, n
        elif fib < n:
            prev = fib
        else:
            # determines if n is closest to prev or to fib?
            if n - prev < fib - n:
                return False, prev
            else:
                return False, fib
        

n = int(input("enter a number: "))
for fib in fibs():
    # prints fib if it equals n
    if n == fib:
        print("your number is a Fibonacci number")
        break
    # if n does not equal fib the closest fibonacci number is displayed
    if fib > n:
        print("your number is not a Fibonacci number")
        print("the closest Fibonacci number is", fib)
        break

# contributed by Finley Jepson
