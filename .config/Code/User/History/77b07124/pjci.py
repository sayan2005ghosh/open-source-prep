#Problem 1: The Secret Santa. You have a list of names. Write a script that assigns each person one unique person to buy a gift for.
#            A person cannot be assigned to themselves, and no two people can be assigned to the same recipient.
#import random
#name=["Sayan","Barshan","Ankan","Shibom","Pallabi","Suman"]
#gifts=["car","book","bag","picture","bat","ball","mobile"]

#select_name=random.sample(name,1)
#select_gifts=random.sample(gifts,1)
#name_select=random.sample(name,1)

#print(f"The secret Santa is:{select_name}  who gifts:{name_select} and the gift is:{select_gifts}")

#********************************************************************************************************************************************************

#Problem 2: Unique Dice Roll. Generate a  list of all numbers from 1 to 100 in a completely random order without 
#           using random.shuffle(). (Hint: Use a set or while loop to track what has been seen).
i=1
while i<=100:
    printi+=1
    print(i)