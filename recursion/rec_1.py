# Print name n times using recursion

def print_name(index, limit):

    # base case
    if (index>limit):
        return
    
    # print name
    print("hello")
    # recursive call = tail recursion
    print_name(index+1,limit)

# function call
print_name(0, 5)



