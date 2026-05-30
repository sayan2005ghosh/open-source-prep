#Problem 1: The Secret Santa. You have a list of names. Write a script that assigns each person one unique person to buy a gift for.
#            A person cannot be assigned to themselves, and no two people can be assigned to the same recipient.
import random
name=["Sayan","Barshan","Ankan","Shibom","Pallabi","Suman"]
gifts=["car","book","bag","picture","bat","ball","mobile"]
select_name=random.sample(name,1)
select_gifts=random.sample(gifts,1)


