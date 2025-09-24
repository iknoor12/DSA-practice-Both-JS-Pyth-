#  Basic 
#  1.Student Marks: a dictionary with student names and marks.Then print the marks of a specific student.
dict1 = {
    "Riya": 90,
    "Iknoor": 89,
    "Himani": 75,
    "Anisha": 78
}
# print(dict1['Iknoor'])


# 2. Word Count: Given a sentence, count how many times each word appears using a dictionary.
Input = "apple banana apple orange banana apple"
output = {}

wordList = list(map(str, Input.split(" ")))
for word in wordList:
    if word in output:
        output[word] += 1
    else: 
        output[word] = 1

print(output)
# Output: {"apple": 3, "banana": 2, "orange": 1}
