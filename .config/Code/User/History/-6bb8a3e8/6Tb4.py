
#Bagles
def game():
    Clue="comes after 4"
    print(Clue)
    select_number=int(input("Select a number:(1,2,3,4,5,6,7,8,9,0)"))
    if select_number==5:
        print("Pico")
    else:
        print("Bagles")
        second_clue="Comes before 10"
        if select_number==9:
           print("Pico")
        else:
             print("Bagles")



game()    