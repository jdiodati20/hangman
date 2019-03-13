def square (var):
    """
    returns var squared.
    :parameter var: int.
    """
    return(var ** 2)

print(square(5))


def printing (string):
    print(string)

printing("hello")

def optional (str0, str1, str2, str3 = 2, str4 = 1):
    print("nice")
    print(str3)
    print(str4)

optional(0, 1, 2, 10)


def division2 (integer):
    return integer / 2

result = division2(31)

def multiply4 (integer):
    return integer * 4

print(multiply4(result))
