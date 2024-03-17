# counts down from num to zero
def recursion_loop(num):
    if num == 0:
        print(num) 
        return("done") 
    else: 
        print(num)
    return recursion_loop(num - 1)

print(recursion_loop(5))

# counts from 0 to num

def print_numbers(n):
    if n < 0:
        return
    print_numbers_helper(n)

def print_numbers_helper(curr):
    if curr == 0:
        print(curr)
        return
    print_numbers_helper(curr - 1)
    print(curr)

# Example usage:
print_numbers(5)

print(recursion_loop2(5))