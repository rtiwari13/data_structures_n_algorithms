# Print 1 to N 

def print_to_n (i,n):

    if (i>n):
        return

    print(i)
    print_to_n (i+1,n)

print_to_n (1,7)


# Print n to 1

def print_to_one (i,n):

    if (i>n):
        return
    
    # make function call first then print
    # so after making function calls to n 
    # it will return in reverse order

    print_to_one (i+1,n)
    print(i)
    
print_to_one (1,7)