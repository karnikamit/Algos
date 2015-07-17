import time
start = time.clock()
alphabets = ['one','two','three','four', 'five', 'six', 'seven', 'eight', 'nine','ten', 
             'eleven','twelve','thirteen', 'fourteen','fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen','twenety',
             'thirty','fourty','fifty','sixty','seventy', 'eighty', 'ninety', 'hundred', 'thousand']
 
a_dic = {}
for i in range(len(alphabets)):
    a_dic[i+1] = alphabets[i]
#print a_dic
k = []
alph = 0
alp1 = 0
alp11 = 0
for n in range(1, 1001):
    k = list(str(n))
    l = len(k)
    if l == 3:
        for i in a_dic:
            if k[0] == i:
                alph += len(a_dic[i])+len('hundred')
                break
                    
            
    elif l == 2 or l == 1:
        for i in a_dic:
            if n == i:
                alp1 += len(a_dic[i])
                break
                
            
    elif l==4:
        for i in a_dic:
            if k[0] == i:
                alp11 += len(a_dic[i])+len('thousand')
                break
print (alph+alp1+alp11)
print ('Runtime:', time.clock()-start, 'sec')
'''
print count 
def hundred():
    global k, a_dic
    num = []
    for i in a_dic:
        if k[0] == i:
            num.append(a_dic[i])
    return num[0]
def tenth():
    global k, a_dic
    num1= []
    for i in a_dic:
        if k[0] == i:
            num1append(a_dic[i])
    return num1[0]
'''
