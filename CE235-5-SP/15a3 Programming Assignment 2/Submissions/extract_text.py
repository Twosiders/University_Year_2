file = open("flower.bmp","rb")
data = bytearray(file.read())
file.close()

#Name : Alex Mezodi 1401665
#Correct p = 7
#Correct q = 15

for x in range(1,20):
        for y in range(1,20):
                p = x
                q = y
                header_len = 54

                text_as_bits = bytearray((len(data) - header_len - p) // q)

                for i in range(0, len(text_as_bits)):
                             text_as_bits[i] = data[header_len + p + i * q] & 0b00000001 
  
                text = bytearray(len(text_as_bits)//8)
                print(len(text))
                for i in range(0, len(text)):
                        text[i] = 0
                        for j in range(0,8):
                                text[i] = text[i] | (text_as_bits[i * 8 + j] << j)
 
                file = open("textFound.txt","wb")
                file.write(text)
                f = open('textFound.txt')
                file.close()

	
