## Reverse a string using recursion in Python

The following code defines a function rreverse that takes a string s as its argument and returns the reverse of the input string using recursion

## Get the code.

1. Get the code:

```
git clone https://github.com/wandersonsc/recursion
```

2. Run it! Assuming you have Python setup.

```python
    def reverse(s):
        if not string:
            return string
        else:
            return reverse(string[1:]) + string[0]


```

## How it works

1. The base case is when the input string is empty, in which case the function returns the empty string, "".

2. When the input string is not empty, the function returns the result of calling itself with the tail of the string (string [1:]) concatenated with the first character of the original string (string[0]).
   For example, if you call reverse("hello"), the function will make the following recursive calls:

```python
    reverse("ello") + "h"
    (reverse("llo") + "e") + "h"
    ((reverse("lo") + "l") + "e") + "h"
    (((reverse("o") + "l") + "l") + "e") + "h"
    ((("" + "o") + "l") + "l") + "e" + "h"
    "olleh"
```
