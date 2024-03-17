# func will take a number of m&ms
# 1. if it is odd number eat one to make it even
# 2. divide m&ms in half
# 3. leave the first half
# 4. take one of those halves and divide it in half again, and eat one if it's an odd num 
# 5. leave the first half of that pile
# 6. take the other half and divide.... 

def prepare_mms(number_of_mms):
    if number_of_mms == 1:
        return []
    else:
        half = number_of_mms // 2 # we are using floor division to get our cut
        return [["(*)" * half]] + prepare_mms(half)