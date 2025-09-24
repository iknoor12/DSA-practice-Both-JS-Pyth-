#  PRACTICE   QUESTION   NUMBER  3  // 

#  Write a program that takes a number as input and prints a pyramid pattern of stars.

n = int(input("Enter the number: "))

def leftPyramid(n):
    for i in range(1, n+1):
        line = ""
        for a in range(1, i+1):
            line += "*"
        print(line)

leftPyramid(n)

#     OUTPUT:  *
#              **
#              ***
#              ****
#              *****

