__author__ = 'CYBORG'
listA = range(1, 5)
listB = [2, 1, 4, 3]
print all(item in listB for item in listA)