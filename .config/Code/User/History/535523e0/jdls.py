names=["ankan","barshan","kabita","pallabi","morgan","sayan"]
target="sayan"
low=0
high=len(names)-1

while low<=high:
    mid=(low+high)//2
    guess=names[mid]


    if guess==target:
        return mid
        print(f"Found it at index {mid}")
    if guess>target:
        high=mid-1
    else :
        low=mid+1    
