#unique Randomization
#unique sample()

#import random

#participants = ["Alice", "Bob", "Charlie", "Diana", "Edward"]

# Pick 3 unique winners
#winners = random.sample(participants, 1)

#print(f"The winners are: {winners}")
# Output will always have 3 distinct names.


#
import random

deck = ["Jack", "Queen", "King", "Ace"]

# Shuffle the list in-place
random.shuffle(deck,1)

print(f"Shuffled deck: {deck}")
# Every card is present, but the order is randomized.