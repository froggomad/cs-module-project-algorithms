'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    results = []
    max_value = nums[0]
    for i, num in enumerate(nums):   
        max_value = num      
        for n in range(i, i+k):            
            if i+k < len(nums)+1:
                print(f"range: {range(i, i+k-1)}")
                if nums[n] > max_value:
                    max_value = nums[n]
                    print(f"max_value: {nums[n]}, at position: {n}")
        if i+k < len(nums)+1:
            results.append(max_value)            
    return results

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
