# convert to binary
# add a space every 4th char

get_bin = lambda x, n: format(x, 'b').zfill(n)
inputbasenumber = int(input("Input Number to Convert to BIN        ::: "))
binarylength = int(input("Input Binary Digits, 4-8-16-32-64-etc ::: "))
binarynumber = get_bin(inputbasenumber, binarylength)

print(binarynumber)

# initializing a empty string for  
# storing the string data 
str_data = ""
   
# slicing the input and converting it  
# in decimal and then converting it in string 
for i in range(0, len(binarynumber), 4): 
      
    # slicing the bin_data from index range [0, 6] 
    # and storing it as integer in temp_data 
    temp_data = int(binarynumber[i:i + 4])
    str_data = temp_data
    print(str_data.zfill(binarylength))
    print(" ")
       
    # passing temp_data in BinarytoDecimal() fuction 
    # to get decimal value of corresponding temp_data 
#    decimal_data = BinaryToDecimal(temp_data) 
       
    # Deccoding the decimal value returned by  
    # BinarytoDecimal() function, using chr()  
    # function which return the string corresponding  
    # character for given ASCII value, and store it  
    # in str_data 
#    str_data = str_data + chr(decimal_data)  
   
# printing the result 
#print("The Binary value after string conversion is:",  
#       str_data) 