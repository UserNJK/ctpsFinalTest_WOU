'''
2. Given a string containing both upper and lower case letters. Write a Python program to
count the number of repeated characters and display the maximum count of a character
along with the character.
'''

inpstr2 = str(input())

countlist = set()

a = inpstr2.upper()
for letter in a:
    countlist.add(letter)

for element in countlist:
    num = a.count(element)
    print(f"{num}{element}")
