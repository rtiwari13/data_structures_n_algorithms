# 1 to N ( by backtracking ) 
# it’s “printing forward” but on the way back up, which is why we call it backtracking.
def print_to_n (i):

    if (i<1):
        return
    
    # so it will call until base condition hits 
    # otherwise starts printing in reverse order from 1 to 7 (tail recursion)
    print_to_n(i-1)
    print(i)
    

print_to_n (7)



# N to 1 ( by backtracking )

def print_to_n (i):

    if (i<1):
        return
    
    # head recursion
    print(i)
    print_to_n(i-1)

print_to_n (7)