"""
Checks if a string is a palindrome
"""

__author__ = "Joseph Gaynor"
__email__ = "U1753547@hud.ac.uk"
__date__ = "2017/11/02"
left = 0
text = input("Enter the text you want to check: ").lower()
right = len(text)-1
while left <= right:
    if text[left] != text[right]:
        print("Not a palindrome")
        break

    left += 1
    right -= 1

    if left == right:
        print("is a palindrome")
