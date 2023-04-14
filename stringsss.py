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
print(word[-1]) # last character
print(word[-2]) # second last character
print(word[0:2]) # slicing: characters from position 0 (included) to 2 (excluded)
print(word[2:5]) # characters from position 2 (included to 5 (excluded)
print(word[4:42]) # out of range slice
print(word[42:])
newWord = 'J' + word[1:]
print(newWord)
print(word[:2] + 'py')
s = 'supercalifragilisticexpialidocious'
print(len(s)) # built in function len() returns length of a string