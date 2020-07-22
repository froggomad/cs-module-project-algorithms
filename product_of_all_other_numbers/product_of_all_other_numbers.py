'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    result = 1
    results = []
    for i in range(len(arr)):
        # O(n^2) <---- eek!
        for j, number in enumerate(arr):
            if i != j:
                result*=number
        results.append(result)
        result = 1
    return results



if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]    
    #arr = [9, 90]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
