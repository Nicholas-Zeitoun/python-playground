print('spam eggs')
print('doesn\'t') # use \' to escape the single quote...
print("doesn't") # use doublequotes instead
print('"Yes," they said.')
print("\"Yes,\" they said.")
print('"Isn\'t," they said.')
s = 'First line.\nSecond line.' # \n means newline
print(s)  # with print(), \n produces a new line
print('\C:\some\name') # here \n means newline!
print(r'C:\some\name') # r before the quote
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
print(3 * 'un' + 'ium')
print('Py' 'thon') # String literals automatically concatenated
text = ('Put several strings within parentheses '
        'to have them joined together.')
print(text)
prefix = 'Py'
# prefix 'thon' # can;t concatenate a variable and a string
print(prefix + 'thon')
word = 'Python'
print(word[0])
print(word[5])