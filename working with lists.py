# Looping Through a Entire List

family_members=["sayan","barshan","subrata","kabita"]
family_members.sort()
for family_member in family_members:
    print(family_member)

# A Closer Look at Looping

# Doing More Work within a for Loop
family_members=["sayan","barshan","subrata","kabita"]
family_members.sort()

for family_member in family_members:
    print(f"{family_member.title()} , are great member in a family.")


#use on \n


family_members=["sayan","barshan","subrata","kabita"]
family_members.sort()

for family_member in family_members:
    print(f"{family_member.title()} , are great.\n") #If you want a huge gap, you can even use multiple ones together: \n\n\n. 
                                                     #Every time you type it, the computer jumps down one more line.


#Making Numerical Lists

# Using the range() Function

for value in range(1,100):                                                     
 print(value)
 
# Using Range to make a list of Numbers

numbers=list(range(1,1001))
print(numbers)
#######################################
even_numbers=list(range(2,1001,2))
print(even_numbers)
#######################################
squres=[]
for value in range(1,1001):
    squre=value**2
    squres.append(squre)
print(squres)    
########################################
squres=[]
for value in range(1,11):
    squres.append(value**3)
print(squres)    

# simple Statistics with a List of Numbers

dig=list(range(1,11))
print(min(dig))
print(max(dig))
print(sum(dig))

# List Comrehensions

values=[value**3 for value in range(1,11)]
print(values)

# Working with Part of a List
#Slicing a List
members=["Sayan","Ankan","Pallabi","Shibom","Argha","Sompriti"]
print(members[0:4])
print(members[1:5])
print(members[:3])
print(members[2:])
print(members[-6:])

#Looping Through a Slice
members=["Sayan","Ankan","Pallabi","Shibom","Argha","Sompriti"]
print("There are some members pf my family:")
for member in members[:3]:
    print(member.title())
#############################

members=["Sayan","Ankan","Pallabi","Shibom","Argha","Sompriti"]
print("\n".join(member.title() for member in members [:3]))

# Copying a List
given_foods=["apple","banana","mango","watermelon"]
print(f"my favourite fruits are-{given_foods}")
foods=given_foods[:]
print("\n"f"my friend like-{foods}")
#########################################
given_foods=["apple","banana","mango","watermelon"]
print(f"my favourite fruits are-{given_foods}")
foods=given_foods[:]
foods.append("orange")
print("\n"f"my friend likes-{foods}")

# Defination of Tuples:
#In Python, a tuple is a built-in data type used to store collections of data.
# While they might look similar to lists at first glance, they have one defining characteristic: immutability.


#When should you use one over the other?
#Feature	          List []	                            Tuple ()
#Mutability	    Mutable (can change)	              Immutable (cannot change)
#Performance	Slower                                Faster (more memory efficient)
#Safety     	Risky for fixed data	              Provides data integrity
#Methods	    Many (append, remove, pop)	          Few (only count and index)

dimensions=(200,50)
print(dimensions[0])
print(dimensions[1])

# Looping Through All Values in a Tuple
dimensions=(200,50)
for dimension in dimensions:
    print(dimension)

# Writing over a Tuple

dimensions=(200,50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions=(400,100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
