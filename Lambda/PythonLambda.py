#A lambda function is a small anonymous function.
#The power of lambda is better shown when you use them as an anonymous function inside another function.
#Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:

x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))