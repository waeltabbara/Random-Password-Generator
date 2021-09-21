#A Python script to generate a random password of 8 characters. Each time the program is run, a new password will be generated randomly

import random
import string


def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)


uppercaseLetter1 = chr(random.randint(65, 90))
uppercaseLetter2 = chr(random.randint(65, 90))
lowercaseLetter1 = chr(random.randint(97, 122))
lowercaseLetter2 = chr(random.randint(97, 122))
digit1 = int(random.randint(1, 9))
digit2 = int(random.randint(1, 9))
punct1 = random.choice(string.punctuation)
punct2 = random.choice(string.punctuation)

password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + str(digit1) + str(
    digit2) + punct1 + punct2
password = shuffle(password)

print(password)
