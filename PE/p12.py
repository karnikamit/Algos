import random
# number = 0
name = ''
number = random.randrange(0, 5)
num = str (number)
if num == '0':
# return 0
elif num == '1':
    print("Player pics- Spock")
elif num == '2':
    print("Player pics- paper")
elif num == '3':
    print("Player pics- lizard")
elif num == '4':
    print("Player pics- scissors")
else:
    print("Wrong number")

print ("-----------------------------------")

numb = random.randrange(0, 5)
num = str (numb)
if num == '0':
    print("Computer pics- rock")
elif num == '1':
    print("Computer pics- Spock")
elif num == '2':
    print("Computer pics- paper")
elif num == '3':
    print("Computer pics- lizard")
elif num == '4':
    print("Computer pics- scissors")
else:
    print("Wrong number")
