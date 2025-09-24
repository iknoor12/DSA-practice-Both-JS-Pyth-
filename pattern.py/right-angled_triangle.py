#   PRACTICE   QUESTION   NUMBER  1  

#  Takes a number as input and prints a right-angled triangle pattern of *numbers* using an array.  

n = int(input("Enter the number: "))

def triangle(n):
    for i in range(1, n+1):
        row = ""
        for a in range(1, i+1):
            # a=str(a)
            row += str(a)
        print(row)


triangle(n)


# OUTPUT : 1
#          12
#          123
#          1234
#          12345




#  prints a right-angled triangle pattern of *characters*.

n = int(input("Enter number of character: "))

def charTriangle(n):
    # char = "A"                         //  This won't take A in every row.
    for i in range(n):
        row = ""
        char = "A"
        for j in range(i+1):
            row += char
            char = chr(ord(char)+1)
        # char = chr(ord(char)+1)                  //  This will increase character after every iterations(row).
        print(row)

charTriangle(n)


# OUTPUT:   A                        if char is in outer loop-> OUTPUT:    A
#           AB                                                             BB
#           ABC                                                            CCC
#           ABCD                                                           DDDD


