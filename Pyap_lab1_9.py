
str_to_conv = input()
print("The string that we have taken is ",str_to_conv)
bin_result = ''.join(format(x,'08b') for x in bytearray(str_to_conv,'utf-8'))
print("The string that we obtain binary conversion is ",bin_result)

number=0

for i in range(len(bin_result)):
    number+=1
    if bin_result[i]=="1":
        print(number)

