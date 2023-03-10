#factorial

def factorial(n):
    if n > 0:
        return n * factorial(n -1)
    else:
        return 1

#test
print (factorial(5))