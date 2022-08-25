# Move Zeros
# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Example:
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example Input: [0,0,11,2,3,4]
# Example Output: [11,2,3,4,0,0]

def func(arr):
    count = 0
    for x in arr:
        count += 1
        if x == 0:
            arr.remove(x)
            arr.append(0)
    return arr

def func(arr):
    count = 0
    for x in arr:
        if x == 0:
            arr.remove(x)
            count += 1
    for i in range(count):
        arr.append(0)
    return arr

arr = [0,1,0,3,12]
print(func(arr))

arr = [11,2,3,4,0,0]
print(func(arr))