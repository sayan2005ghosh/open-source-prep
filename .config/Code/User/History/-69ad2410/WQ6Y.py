def code():
    alphabet=("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    select=input("Select letters:")
    index=alphabet.find(select)
    new_index=(index+3)%52
    print(alphabet[new_index])

code()    
