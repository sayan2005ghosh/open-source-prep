import random

name = ["Ankan", "Sayan", "Pallabi", "Suman"]
gifts = ["toy", "books", "mobile", "car"]

# 1. Shuffle the lists directly (no '=' needed)
random.shuffle(name)
random.shuffle(gifts)

# 2. Use the "Neighbor Shift" logic
# This ensures Santa (index i) gives to the NEXT person (i + 1)
for i in [0, 1, 2, 3]:
    santa = name[i]
    
    # The (i + 1) % 4 trick ensures the last person gives to the first person
    receiver = name[(i + 1) % 4] 
    assigned_gift = gifts[i]
    
    print(f"Santa: {santa} -> gives {assigned_gift} to -> {receiver}")