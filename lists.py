squares = [1,4,9,16,25]
print(squares)
print(squares[0]) # indexing returns the item
print(squares[-1])
print(squares[-3:]) # slicing returns a new list
print(squares[:]) # All slice. returns shallow copy of the list
squares += [36, 49, 64, 81, 100] # list concatenation
print(squares)