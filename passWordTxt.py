f = open("ctf.txt", "r")

list = f.readlines()

# print(list)
counter=0
str=""
for line in list[2:]:
    
    counter+=1    
    # print(line)
    newline=line.split(" ")
    if counter==3:
        for i in newline:
            str+=chr(int(i))    
        
    # print(newline)
    # print(type(newline))
    
    # for i in newline:
    #     print(chr(int(i)), end="")
        
    # print(f"          line: {counter}")
    if (counter == 3):
        
         break
    # print("\n")
    
# newcounter=0
# for i in list[counter]:
#     newcounter+=1
#     if(newcounter<=12):
#         continue
    
#     # print(chr(int(i)), end="")
# print(newcounter)
# # print(list[counter])
# print(str)

line=str.split(": ")
print(line[1].strip())