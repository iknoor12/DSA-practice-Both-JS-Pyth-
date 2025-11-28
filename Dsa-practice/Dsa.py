# 26 Nov:
# 1 question: Given an array, find the largest element in it.
arr = [1, 2, 3, 4]
x = 3
if x in arr:
    print("true")
else:
    print("false")



# 2 question: Given a string s, return the index of the first character that does not repeat.If no such character exists, return -1.
s = 'practice'
for i in range(len(s)):
    if s.count(s[i]) == 1:
        print(i)
        break
else:
    print("-1")


# 27 Nov:
# 1 question: "Count even numbers in an array. 
# Input: [2, 5, 6, 7, 8], Output: 3"
arr = [2, 5, 6, 7, 8]
count = 0
for i in range(len(arr)):
    if arr[i] % 2 == 0:
        count += 1
print(count)


# 2 question: "5. Count occurrences of a character. 
# Input: string = ""banana"", char = ""a"", Output: 3"
string = 'banana'
char = 'a'
print(string.count(char))


# 3 question: "Bubble Sort Question
# Q:Given an array of integers, sort the array in ascending order using Bubble Sort. 
# Input: [5, 2, 9, 1, 5, 6], Output: [1, 2, 5, 5, 6, 9]"
arr = [5, 2, 9, 1, 5, 6]
for i in range(len(arr)):
    for j in range(0, len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(arr)