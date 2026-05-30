movies = {
    "Action": 15,
    "Comedy": 10,
    "Drama": 12
}
def Y():
    X=input("What Genre do you Want?(Action/Comedy/Drama):")
    if X==movies["Action"]["Comedy"]["Drama"]:
        print("Welcome")
    else:
        print("Choose from our bucket")    


Y()