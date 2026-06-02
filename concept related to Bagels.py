#unique Randomization
#*****************************************************************************************************************************************************

#################unique sample()

import random

participants = ["Alice", "Bob", "Charlie", "Diana", "Edward"]

################## Pick 1 unique winners
winners = random.sample(participants, 1)

print(f"The winners are: {winners}")
################## Output will always have 1 distinct names.
#*********************************************************************************************************************************************************

Random.Suffle


import random

deck = ["Jack", "Queen", "King", "Ace"]

#Shuffle the list in-place
random.shuffle(deck)

print(f"Shuffled deck: {deck}")
# Every card is present, but the order is randomized.


#*********************************************************************************************************************************************
#UUID


import uuid

# Generate a unique random ID
unique_id = uuid.uuid4()

print(f"Your unique session ID is: {unique_id}")



#****************************************************************************************************************************************************************

#Stateful Iteration.

names = ["Sayan", "Barshan", "Ankan"]

for x in names:
   print(x)


###########1. for and in (The Loop)
############ Think of for as a way to say "For every item in this pile..."

############ If you have a list of names, you don't want to type print six times. You use a for loop to tell Python to look at each name one by one.
###in: Tells Python which "pile" or list to look inside.
####x: Is just a temporary name for the item Python is currently holding.

###names = ["Sayan", "Barshan", "Ankan"]
#gifts = ["Car", "Book", "Bag"]

# This loop goes through the numbers 0, 1, 2
for i in [0, 1, 2]:
  item = gifts[i]
    print(f"{person} gets a {item}")
names = ["Sayan", "Barshan", "Ankan"]
gifts = ["Car", "Book", "Bag"]

# This loop goes through the numbers 0, 1, 2
for i in [0, 1, 2]:
    person = names[i]
    item = gifts[i]
    print(f"{person} gets a {item}")
