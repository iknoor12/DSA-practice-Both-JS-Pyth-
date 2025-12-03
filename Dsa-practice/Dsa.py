# 26 Nov:
# 1 question: Given an array, find the largest element in it.
# arr = [1, 2, 3, 4]
# x = 3
# if x in arr:
#     print("true")
# else:
#     print("false")



# 2 question: Given a string s, return the index of the first character that does not repeat.If no such character exists, return -1.
# s = 'practice'
# for i in range(len(s)):
#     if s.count(s[i]) == 1:
#         print(i)
#         break
# else:
#     print("-1")


# 27 Nov:
# 1 question: "Count even numbers in an array. 
# Input: [2, 5, 6, 7, 8], Output: 3"
arr = [2, 5, 6, 7, 8]
count = 0
for i in range(len(arr)):
    if arr[i] % 2 == 0:
        count += 1
# print(count)


# 2 question: "5. Count occurrences of a character. 
# Input: string = ""banana"", char = ""a"", Output: 3"
string = 'banana'
char = 'a'
# print(string.count(char))


# 3 question: "Bubble Sort Question
# Q:Given an array of integers, sort the array in ascending order using Bubble Sort. 
# Input: [5, 2, 9, 1, 5, 6], Output: [1, 2, 5, 5, 6, 9]"
arr = [5, 2, 9, 1, 5, 6]
for i in range(len(arr)):
    for j in range(0, len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

# print(arr)




# 28 Nov
# 1 question: "Find the maximum element in an array.    
# Input: [3, 1, 7, 4, 2], Output: 7"
arr = [3, 1, 7, 4, 2]
max = 0
for i in range(len(arr)-1):
    if arr[i] > arr[i+1] and arr[i] > max:
        max = arr[i]

# print(max)


# 2 question: "Remove duplicates from an array while keeping order. 
# Input: [1, 2, 2, 3, 1, 4], Output: [1, 2, 3, 4]"
arr = [1, 2, 2, 3, 1, 4]
result = []
for i in range(len(arr)):
    if arr[i] not in result:
        result.append(arr[i])
# print(result)


# 3 question: "Two Sum Problem Given an array and a target number, find two numbers whose sum equals the target. 
# Input: nums = [2,7,11,15], target = 9, Output: [0,1]"
nums = [2,7,11,15]
target = 9
# for i in range(len(nums)-1):
#     for j in range(i+1, len(nums)):
#         sum = nums[i] + nums[j]
#         if sum == target:
#             print(i, j)


# 29 Nov
# 1 question: "Find the second largest element in an array. 
# Input: [3, 5, 2, 9, 7], Output: 7"
arr = [3, 5, 2, 9, 7]
arr.sort(reverse=True)
# print(arr[1])


# 2 question: "Check if two strings are anagrams (same letters, different order).
# Input: ""listen"", ""silent"", Output: True"
str1 = 'listen'
str2 = 'silent'
match = False
for i in str1:
    char = i
    for j in str2:
        if char == j:
            match = True
            break
        else: 
            match = False

# if match == True:
#     print("True")
# else:
#     print("False")



# 30 Nov
# 2 question: "Use Linear Search to find the number 7 in the array: [2, 4, 7, 1, 9], At which index is it found?"
arr = [2, 4, 7, 1, 9]
tar = 7
# for i in range(len(arr)):
#     if arr[i] == tar:
#         print(i)


# 3 question: "Use Selection Sort to sort the array: [29, 10, 14, 37, 13]"
arr = [29, 10, 14, 37, 13]
for i in range(len(arr)):
    min_idx = i
    
    for j in range(i+1, len(arr)):
        if arr[j] < arr[min_idx]:
            min_idx = j

    arr[i], arr[min_idx] = arr[min_idx], arr[i]

print(arr)