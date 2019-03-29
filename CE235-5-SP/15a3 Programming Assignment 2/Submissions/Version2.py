from __future__ import division
file = open("flower.bmp","rb")
data = bytearray(file.read())
file.close()

#Name : Alex Mezodi 1401665
#Correct p = 7
#Correct q = 15
done = False
class GetOutOfLoop( Exception ):
    pass
try:
        for x in range(1,20):
                for y in range(1,20):
                        p = x
                        q = y
                        total0s = 0
                        total1s = 1
                        
                        
                        header_len = 54

                        text_as_bits = bytearray((len(data) - header_len - p) // q)

                        for i in range(0, len(text_as_bits)):
                                text_as_bits[i] = data[header_len + p + i * q] & 0b00000001 
                                if text_as_bits[i] == 0 :
                                        total0s = total0s + 1
                                #else :
                                #        total0s = total0s / len(text_as_bits)
                                if text_as_bits[i] == 1:
                                        total1s = total1s + 1
                                #else :
                                #        total1s = total1s / len(text_as_bits)               
                        text = bytearray(len(text_as_bits)//8)
                        #print(len(text))
                        for i in range(0, len(text)):
                                text[i] = 0
                                for j in range(0,8):
                                        text[i] = text[i] | (text_as_bits[i * 8 + j] << j)

                        
                        file = open("textFound.txt","wb")
                        file.write(text)
                        f = open('textFound.txt')
                        file.close()

                        percentageof0s = total0s/len(text_as_bits)
                        percentageof1s = total1s/len(text_as_bits)
                        print(x," ",y," %of0: ",percentageof0s," %of1: ",percentageof1s)
                        #print(total0s, " and ",len(text_as_bits))
                        if(percentageof0s - percentageof1s > 0.27):
                                file.close()
                                raise GetOutOfLoop
except GetOutOfLoop:
        pass
    
                                

	
