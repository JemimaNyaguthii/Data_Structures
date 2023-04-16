# Dictionaries are made up of key-value pairs.Key is used to identify the item and
#  the value holds as the name suggests, the value of the item.
# del is used to remove an item  from the array.
diction={'Elvis':1, 'John':2, 'Peter':3, 'James':4}
del diction ['James']
# dict.keys() 

# Getting  a minimum value from the dictionary
minimum ={'flour':100,'sugar':80,'milk':60 }
print(min(minimum,key=minimum.get))

# changing the value of a key in a nested dictionary 
details={'jem':20,'mary':23,'jane':17}
details['jem']=23
print(details)

# # Tuples
#  Lists are mutable while tuples are immutable
# Accessing a value from a tuple
# we use indexing
fruits=('orange','banana','mango','apple')
print(fruits[1])

# Copy specific elements from one tuple to a new
games=('football','netball','basketball','rugby')
fav=games[-2]
print(fav)

# Counting the number of occurrences  
rivers=('Volta','Orange','Nile','Zambezi','Volta')
print(rivers.count('Volta'))

# lists
# reversing a list
numbs=[50,60,70,80,90]
numbs.reverse()
print(numbs)
# alternative is using negative slicing
# -1 indicates to start from the last item.

# Given list x = [1, 2, 3, 4, 5, 6, 7, 8, 9].
# Print the last element in the list

numx=[1,2,3,4,5,6,7,8,9]
numx.append(10)
print(numx)


numb=[90,80,70,60,50]
numb=numb[::-1]
print(numb)
#  Remove empty strings from the list of strings
# Use a filter() function to remove None type from the list
# remove None from list1 and convert result into list
names=('Dama','Mona','Dolly','')
name=list(filter(None,names))
print(name)

# sets
# Given the sets a = {10,12,13,14,15} and b = {14,15,16} print
#   values in a but not in b
# Returns a set of values that are in the first set but not in the second.
a={10,12,13,14,15}
b={14,15,16}
c=a.difference(b)
print(c)

# returning a set that contains values that are in both set
# return a set containing two values in two sets duplicates excluded.
d={10,12,13,14,15}
e={14,15,16}
f=d.union(e)
print(f)
# Returns a set containing value existing in both sets intersection




