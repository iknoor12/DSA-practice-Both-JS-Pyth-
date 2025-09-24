#  PRACTICE   QUESTION   NUMBER  2  // 

#  Takes a number as input and prints an inverted right-angled triangle pattern of *numbers*.  //

# n = int(input("write the numbers: "))

def reverseTriangle(n):
    for i in range(n, 0, -1):     # this range will go from 5 to 0 by decreasing.
        row = ""
        for a in range(1, i+1):   # this range will go from 1 to i(5) by increasing.
            row += str(a)
        print(row)


# reverseTriangle(n)


# OUTPUT:  12345
#          1234
#          123
#          12
#          1




# prints an inverted right-angled triangle pattern of *Characters*.

n = int(input("enter number of characters: "))

def reverseTriangle(n):
    for i in range(n, 0, -1):
        char = ""
        for a in range(0, i):
            char += chr(ord("A")+a)
        print(char)

reverseTriangle(n)

# OUTPUT:  ABCDE
#          ABCD
#          ABC
#          AB
#          A