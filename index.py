# practical
str = "F.R.I.E.N.D.S"

def string(str):
    new_str = ""

    for char in str:
        if char != ".":
            new_str += char

    result = new_str.lower()
    print(result)

string(str)