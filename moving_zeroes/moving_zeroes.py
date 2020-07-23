'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    i = 0
    #track whether we've deleted the first zero
    deleted = False
    #track its index in the array
    first_zero_i = -1
    #when we hit the first deleted zero, everything after is also zero
    while i is not first_zero_i and i is not len(arr)-1:
        print(i)        
        if arr[i] == 0:
            arr.__delitem__(i)
            print(f"deleting at: {i}")
            arr.append(0)
            if deleted == False:
                #set the first deleted zero's index
                first_zero_i = len(arr)-1
                print(f"deleted first zero and inserted at {len(arr)-1}")
                deleted = True
            else:
                #move it backward to account for deleted zeroes
                first_zero_i -= 1
        else:
            # increase current index         
            i+=1
        
        print(arr)
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 0, 0, 0, 3, 2, 1]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")