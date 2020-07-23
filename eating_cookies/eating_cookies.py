'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    three = n-3
    two = n-2
    one = n-1

    if three >= 1:
        #number of times can eat 3

        #number of times can eat 3 and 2

        #number of times can eat 3 and 1
    if two >= 1:
        #number of times can eat 2

        #number of times can eat 2 and 3

        #number of times can eat 2 and 1

    if one > 1:
        #number of times can eat 1

        #number of times can eat 1 and 2

        #number of times can eat 1 and 3

    # print(f"Cookie Monster can eat 1 Cookie {n} times!")
    # if n == 0:
    #     # why is there 1 way to eat 0 cookies according to unit tests?
    #     return 1
    # if n == 2:
    #     return 2
    # ways = n
    # #can we eat 2 cookies at a time?
    # if int(n/2) > 0:
    #     #number of times we can eat 2 cookies
    #     two_times = int(n/2)
    #     if two_times >= 1:
    #         ways += two_times
    #         remainder = n-(two_times * 2)
    #         if remainder >= 1:
    #             #number of times we can eat 2 + 3
    #             three_times = n-int((n/3) + (n/2))
    #             if three_times >= 1:
    #                 ways += three_times
    #                 print(f"Cookie Monster can eat 2 Cookies {two_times} and 3 Cookies {three_times}")

    #         if remainder < 1:
    #             suffix = "!"
    #         else:
    #             #number of 2+1 times
    #             ways += remainder
    #             suffix = f" and 1 Cookie {remainder} time(s)"                
    #         print(f"Cookie Monster can eat 2 Cookies { int(two_times) } times{suffix}")
    # #can we eat 3 cookies at a time?
    # if n/3 > 0:
    #     three_times = int(n/3)
    #     if three_times >= 1:
    #         ways += three_times
    #         remainder = n-(three_times * 3)
    #         if remainder < 1:
    #             suffix = "!"
    #         #number of 3+2 times
    #         if remainder >= 2:
    #             two_times = int(remainder/2)
    #             if two_times >= 1:
    #                 ways += two_times
    #                 suffix = f" and 2 Cookies { int(two_times) } time(s)"
    #         print(f"Cookie Monster can eat 3 Cookies { int(three_times) } times{suffix}")
    #         #number of 3+1 times
    #         if remainder >= 1:                
    #             ways += remainder
    #             print(f"Cookie Monster can eat 3 Cookies { int(three_times) } and 1 Cookie {remainder} time(s)")
    # return ways

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 2

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")
