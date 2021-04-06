#Linear Search vs Binary Search

import time

def linear_search(list, target):
    for index in range(len(list)):
        if list[index] == target:
            return index
    return -1
    
def binary_search(list, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(list)-1
    if high<low:
        return -1
        
    midpoint = (low + high)//2
    
    if list[midpoint] == target:
        return midpoint
    elif target < list[midpoint]:
        return binary_search(list, target, low, midpoint-1)
    else:
        return binary_search(list, target, midpoint+1, high)

def time_lapse(start, end):
    elapse = end - start
    print('Time:',elapse)
    return elapse

if __name__ == '__main__':
    list = [1,2,3,4,5,6,7,8,9,10]
    target = 10
    
    lst = time.time()
    print(linear_search(list, target))
    let = time.time()
    linear_time = time_lapse(lst, let)
    
    bst = time.time()
    print(binary_search(list, target))
    bet = time.time()
    binary_time = time_lapse(bst, bet)
    
    if linear_time <binary_time:
        print('Linear search was faster.')
    else:
        print('Binary search was faster.')