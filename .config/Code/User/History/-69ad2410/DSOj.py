def code():
    alphabet=("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    select=input("Select letters:")
    index=alphabet.find(select)
    new_index=index+3
    print(alphabet[new_index])

code()    
