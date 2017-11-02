"""
Fibonacci sequence generator
"""

__author__ = "Joseph Gaynor"
__email__ = "U1753547@hud.ac.uk"
__date__ = "2017/10/20"

def fib(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    return fib(n-1) + fib(n-2)

while 1:
    try:
        number_of_sequences = int(input("How many Fibonacci numbers: "))
        for x in range(number_of_sequences):
            print(fib(x))
    except ValueError:
        print("Please enter an actual number")

