# A NON-tail-recursive function.
# The function is not tail
# recursive because the value
# returned by fact(n-1) is used
# in fact(n) and call to fact(n-1)
# is not the last thing done by
# fact(n)
def fact(n):
    if (n == 0):
        return 1
    return n * fact(n-1)


# Driver program to test
# above function
if __name__ == '__main__':
    print(fact(5))

# A tail recursive function
# to calculate factorial

def fact(n, a=1):

    if (n <= 1):
        return a

    return fact(n - 1, n * a)

# Driver program to test
# above function
print(fact(5))

