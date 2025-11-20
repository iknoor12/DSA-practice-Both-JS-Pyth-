# Easy
# Given an integer array nums, return True if any value appears at least twice in the array, and return False.
# Input: nums = [1, 2, 3, 1],  Output: True

def containsDuplicate(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return True

nums = [1, 2, 3, 1]
print(containsDuplicate(nums))


# Medium
# Given an array nums, rotate the array to the right by k steps.
# Input: nums = [1, 2, 3, 4, 5, 6, 7], k = 3,  Output: [5, 6, 7, 1, 2, 3, 4]

def rotate(nums, k):
    n = len(nums)
    for i in range(k):
        last  = nums[n-1]
        for j in range(n-1, 0, -1):
            nums[j] = nums[j-1]
        nums[0] = last
    return nums

nums = [1, 2, 3, 4, 5, 6, 7]
k = 3 
print(rotate(nums, k))


# BY SIR

# "Print all the even numbers from the given array.
# Input:- [1, 4 ,5, 8, 10, 3], Output:- [4,8,10]"
def evenNum(arr):
    even = []
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            even.append(arr[i])
    return even

arr = [1, 4, 5, 8, 10, 3]
print(evenNum(arr))


# "Find the Majority Element
# Input:-[3, 3, 4, 2, 4, 4, 2, 4, 4], Output:- 4"
def majorEle(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            maj = arr[i]
    return maj

arr = [3, 3, 4, 2, 4, 4, 2, 4, 4]
print(majorEle(arr))