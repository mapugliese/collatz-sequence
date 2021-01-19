def collatz(num):
    '''Returns a sequence in which the first and each subsequent number is 
    divided by two if it is even and is multiplied by 3 and one is added if 
    it is odd. This sequence should eventually create 1, no matter the 
    starting value.'''

    # If the input == 1, the while loop won't begin
    if num != 1:

        # Creates the return list
        num_list = []

        # Stops the loop when 1 is reached
        while num != 1:

            # Determines if the number is even
            if num%2 == 0:
                num = num/2
                num_list.append(int(num))
            
            # Procedure for an odd number
            elif num%2 == 1:
                num = (num*3)+1
                num_list.append(int(num))
        return num_list
    else:
        return [1]

print(collatz(3467890))
