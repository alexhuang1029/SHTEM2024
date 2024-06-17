print('helloworld')
a = 0
i, j = 0,1

# Set starting value for Fibonaci Sequence
if a == 0:
    print(0)
    a = 1

# Set recursive pattern starting from the 2nd term
if a >= 1 and a < 50:
    while a < 50:
        # Allows i to take the value of j
        # At the same time, j becomes the sum of the previous i and itself
        i, j = j, i+j
        print(i)
        a = a+1