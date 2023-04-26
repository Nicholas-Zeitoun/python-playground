# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b

i = 256*256
print('The value of i is', i)

# keyword argument end can be used to avoid the newline after the output. Or end input with a different string
a, b = 0, 1
while a < 1000:
    print(a, end=',')
    a, b = b, a+b