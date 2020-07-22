'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    i = 0
    z = 0
    
    while i is not len(arr):        
        if arr[i] == 0:
            arr.__delitem__(i)
            print(f"deleting at: {i}")
            # decrement current index            
            i-=1
            # increase zero count
            z+=1  
        # increase current index         
        i+=1
        print(arr)
    #append zeroes
    for _ in range(z):
        arr.append(0)
        print("i")
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 0, 0, 0, 3, 2, 1]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")