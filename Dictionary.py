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

# print(output)
# Output: {"apple": 3, "banana": 2, "orange": 1}



# 3. Iterating through a Dictionary: a dictionary of student scores, print each student's name and their score.
scores = {
    "John": 85, 
    "Emily": 92, 
    "David": 78
}
for stu in scores:
    print(stu, scores[stu])

# Another loop:
# for stu, scr in scores.items():
#     print(stu, scr)



# 4. Creating a Dictionary from a List: given two lists, one for keys and one for values, create a single dictionary from these lists.
keys = ["a", "b", "c"]
values = [1, 2, 3]

data = {}
for a,b in zip(keys, values):
    data[a] = b
print(data)



#  Intermediate
# 1. 