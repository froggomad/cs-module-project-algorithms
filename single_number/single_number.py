'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    i=0
    for num in arr[::2]:
        num_sq = num*num
        num_next = num * arr[i+1]
        nums_match = num_sq == num_next
        i+=2

        if not nums_match:
            return num


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")