'''
4. Write a python program which takes string as input and reverses the words of the given 
string and print it. Note: You cannot use split()
'''

def reversed_words(inpstrtorev):

    givenword = ''
    revword = ''

    for character in inpstrtorev:

        if character == " ":
            reversed = givenword + ' ' + revword
            revword = reversed
            givenword = ''

        else:
            givenword += character


    reversed = givenword + ' ' + revword

    return reversed.strip()



inpstr4 = input()

sol4 = reversed_words(inpstr4)
print("Reversed string is:", sol4)

