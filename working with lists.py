#binary search concept

names=["1","2","3","4","5"]
names.sort()
target=input("choose the name:")
low=0
high=len(names)-1

while low<=high:
    mid=(low+high)//2
    guess=names[mid]


    if guess==target:
        print(f"Found it at index {mid}")
        break
    if guess>target:
        high=mid-1
    else :
        low=mid+1    
