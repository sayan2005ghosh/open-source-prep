#unique Randomization

import random

participants = ["Alice", "Bob", "Charlie", "Diana", "Edward"]

# Pick 3 unique winners
winners = random.sample(participants, 3)

print(f"The winners are: {winners}")
# Output will always have 3 distinct names.