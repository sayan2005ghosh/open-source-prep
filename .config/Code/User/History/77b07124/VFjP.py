#Problem 1: The Secret Santa. You have a list of names. Write a script that assigns each person one unique person to buy a gift for.
#            A person cannot be assigned to themselves, and no two people can be assigned to the same recipient.       
import random
name=["Ankan","Sayan","Pallabi","Suman"]
name_select=random.suffle(name)
gifts=["toy","books","mobile","car"]
gifts_select=random.suffle(gifts)
print(f"the santas are:{name_select}, and the gifts are:{gifts_select}")
              


                    