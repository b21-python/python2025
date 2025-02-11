# Introduction to Python

We will cover python and programming concepts as build a game.  We will start by introducing a few concepts that you can test interactively.

> If you want to learn more try the [Python course at Khan Academy](https://www.khanacademy.org/computing/intro-to-python-fundamentals)


## Open Thonny

Open the Thonny app by clicking Berry->Programming 

The main text area is where you can write code and the 'Shell' below is where the code is executed.

## Run your first code

In the text window enter the following code and press the green play button to run the code.

```python
print("Hello World")
```

Congratulations, you have run your first python code!


### Math

You can do math in python easily, just write the math expression inside of the print function.

```python
print(6 * 7)
```

You can do more complex math:

```python
print( (3 + 3) * 7 + 2**5)
```

> `2**5` is 2 to the 5th power.  For a list of all arithmetic operators see [Python docs](https://www.w3schools.com/python/gloss_python_arithmetic_operators.asp)

Try to write your own equation.


### Variables

You can store the result of a math operation or anything else you do in a variable so you can use it later.

```python
theAnswer = 6 * 7
print(theAnswer)
```

This does the same thing as `print(6 * 7)` but it stores the result of the math operation so it can be used later


### Conditions

For your program to make decisions you can use logical conditions.  

```python
a = 42
b = 64
if a < b:
  print ("a is smaller than b")
else:
  print ("a is greater than or equal to b")
```

We have introduced two concepts here, logical conditions and the if/else statement.  Modify the code so  the text in the else condition is printed.

> NOTE: Python requires that you get indentation correct.  Try removing the spaces before either print and see what happens when you run the code.


### Loops

Loops allow you to repeat something multiple times without writing it out multiple times.  It also lets you repeat something any number of times based on a variable.

Write the code to print the word `banana` 3 times, once on each line like this:

```
banana
banana
banana
```

This could be done by calling print three times:

```python
print("banana")
print("banana")
print("banana")
```

Or it could be done with a loop:

```python
i = 0
while i < 3:
  print("banana")
  i = i + 1
```

Modify the loop to print out banana 11 times.


### Functions

You have already used a function without knowing it, `print`!  A function is a named block of code that is only run when it is called.  Like `print` it can take input (parameters) and return output.  You can use functions that someone else wrote, like `print` or you can write your own.  For now we will just stick to using existing functions.

Functions are often grouped together into libraries that you can use.  Pygame is a library, another common library is `math`.  To use a library you must import it.

```python
import math
x = math.pi
print(x)
```

We just printed Pi on a Raspberry Pi!


### Comments

Comments are not code, they are for the person reading the code to help them understand what is going one.

```python
# This is a comment
# they can be on their own line
a = 42 # or they can be at the end of a line
```


### Lists

Lists, also known as arrays store a number of values.  You can add and remove values from the list.

```python
numbers = [1,5,3,89,1000, "banana"]
print(numbers)

number.append(42)
print(numbers)

number.pop(0)
print(numbers)
```

#### Looping over lists

```python
for number in numbers:
  print(number)
```

Create a list and a loop that says something funny.