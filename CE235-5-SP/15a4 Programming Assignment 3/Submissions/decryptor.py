#****************************
#* Decryptor by Alex Mezodi *
#****************************
# Student Number: 1401665
def swap(s, i, j):
    lst = list(s);
    lst[i], lst[j] = lst[j], lst[i]
    return ''.join(lst)

def swapChar(s,i,j):
    lst = list(s);
    lst[i] = j
    return ''.join(lst)

def swapNibble(s,i,j,n):
    lst = list(s);
    lst[i], lst[j] = n[6], n[7] 
    return ''.join(lst)

array1 = [132, 201, 141, 74, 140, 94, 141, 140,
        141, 15, 31, 164, 90, 229, 201, 141,
        78, 114, 241, 217, 141, 217, 140, 180,
        141, 164, 51, 141, 188, 221, 31, 164,
        241, 177, 141, 140, 51, 217, 141,
        201, 229, 152, 141, 78, 241, 114,
        78, 102, 94, 141, 74, 152, 31, 152,
        141, 94, 201, 31, 164, 102, 164, 51,
        90, 141, 201, 229, 164, 31, 201, 152,
        152, 51, 115]
array2 = []
key = 84
for number in array1:
    #result = int(bin(number^key)[2:].zfill(8),2) #do XOR and also convert to int
    result = bin(number^key)[2:].zfill(8) #step1

    result = swap(result,4,6) #step2
    result = swap(result,5,7)

    for i in range(0,8): #step3
        if(i%2 == 0):
            if(result[i:i+2] == '10'):
                result = swapChar(result,i+1,'1')
            elif(result[i:i+2] == '11'):
                result = swapChar(result,i,'0')
            elif(result[i:i+2] == '00'):
                result = swapChar(result,i,'1')
            elif(result[i:i+2] == '01'):
                result = swapChar(result,i+1,'0')
            
    result = bin(int(result,2)^key)[2:].zfill(8) #step4

    nb1 = result[0:2] #step5
    nb2 = result[2:4]
    nb3 = result[4:6]
    nb4 = result[6:8]
    if(int(nb1) < int(nb3)):
        nb1 = "1" + nb1   
    if(int(nb2) < int(nb4)):
        nb2 = "1" + nb2     
    nb1 = int(nb1,2) - int(nb3,2)
    nb1 = bin(nb1)[2:].zfill(8) 
    nb2 = int(nb2,2) - int(nb4,2)
    nb2 = bin(nb2)[2:].zfill(8)
    result = swapNibble(result,0,1,nb1)
    result = swapNibble(result,2,3,nb2)

    result = swap(result,4,6) #step6
    result = swap(result,5,7)

    for i in range(0,8): #step7
        if(i%2 == 0):
            if(result[i:i+2] == '10'):
                result = swapChar(result,i+1,'1')
            elif(result[i:i+2] == '11'):
                result = swapChar(result,i,'0')
            elif(result[i:i+2] == '00'):
                result = swapChar(result,i,'1')
            elif(result[i:i+2] == '01'):
                result = swapChar(result,i+1,'0')

    result = bin(int(result,2)^key)[2:].zfill(8) #step8
    
    array2.append(result)
    
#print result
print("The numbers decrypted are:")    
for number in array2:
    #chr(int(number))
    print(int(number,2),end=', ')
print("")    
print("And the message is:")
for number in array2:
    print(chr(int(number,2)), end="")

