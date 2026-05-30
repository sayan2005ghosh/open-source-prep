#bicyles
"""bicycles=["trek","hero","bsa"]
print(bicycles)"""

#indexing
"""bicycles=["trek","hero","bsa"]
print(bicycles[2])"""

#indexing by title
"""bicycles=["trek","hero","bsa"]
print(bicycles[2].title())"""

#Using of negative index
"""bicycles=["trek","hero","bsa"] 
print(bicycles[-3])"""


#using of string
"""bicycles=["trek","hero","bsa"]
print(f"My first cycle is:{bicycles[-2].title()}")"""

#Modifying Elements in a List
"""bicycles=["trek","hero","bsa"]
bicycles[0]="honda"

print(f"My first cycle is:{bicycles[-3].title()}")"""

# .append 
"""bicycles=["trek","hero","bsa"]
bicycles.append("honda")
print(bicycles)"""

# .append
"""bicycles=[]
bicycles.append("bsa")
bicycles.append("honda")
print(bicycles[-1])"""

# Inserting Elements into a List
"""motorcycles=["bsa","honda"]
motorcycles.insert(0,"bmw")
print(motorcycles)"""

#Removing an Item Using the del Statement

"""motorcycles=["bas","honda","bmw"]
del motorcycles[0]
print(motorcycles)"""


#Removing an Items Using the pop() 
"""motorcycles=["hero","honda","bmw","bullet"]
popped_motorcycles=motorcycles.pop(1)
print(motorcycles)
print(popped_motorcycles)"""

#remove method

"""motorcycles=["hero","honda","bmw","bullet"]
motorcycles.remove("bmw")
print(motorcycles)"""


#...
"""motorcycles=["hero","honda","bmw","bullet"]
too_expensive="bmw"
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"{too_expensive}, is too expesive for me")"""

#Shorting a List permanently with sort() method
"""motorcycles=["hero","honda","bmw","bullet"]
motorcycles.sort()
print(motorcycles)"""

#.....
"""motorcycles=["hero","honda","bmw","bullet"]
motorcycles.sort(reverse=True)
print(motorcycles)"""

#Sorting a List temporarily with sorted() function
"""motorcycles=["hero","honda","bmw","bullet"]
print(f"The list is:{motorcycles}")
print(sorted(motorcycles))
print(motorcycles)"""

#Printing a list in reverse order
"""motorcycles=["hero","honda","bmw","bullet"]
motorcycles.reverse()
print(motorcycles)"""

#determine the length of a list
motorcycles=["hero","honda","bmw","bullet"]
len(motorcycles)
print()