Reverse a string using recursion in Python

The following code defines a function rreverse that takes a string s as its argument and returns the reverse of the input string using recursion.

python

def reverse(s):
    if s == "":
        return s
    else:
        return rreverse(s[1:]) + s[0]
How it works

The base case is when the input string is empty, in which case the function returns the empty string, "".
When the input string is not empty, the function returns the result of calling itself with the tail of the string (string[1:]) concatenated with the first character of the original string (s[0]).
For example, if you call reverse("hello"), the function will make the following recursive calls:
