#   3.  Two-Pointer Technique

# Given a sorted array and a target sum, use the two-pointer approach to find if a pair exists that adds up to the target. 
# Return the indices or boolean result based on the problem requirement.

array = [5, 19, 11, 7, 3, 13, 6, 8, 17, 10, 19,1]

target = 20

left = 0
right = len(array)-1

for left in range(len(array)):
    for right in range(len(array)-1, left, -1):
        sum = array[left] + array[right]
        if sum == target  :
            print(array[left], array[right])
            break
    
    
