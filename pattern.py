a="""Passwd12!
letmein2@
!!pwd12!!
@B4kili@
Salamm23@
gedebey2!
abcdefg5@
Strong23^
##qwerty33"""
b=a.split("\n")
patern=[]
#counter=0
for i in b:    
    current_patter=""
    for f in i:        
         if (ord(f)>=97 and ord(f)<= 122):
             current_patter+="?l"
         elif (ord(f)>=65 and ord(f)<= 90):
             current_patter+="?u"
         elif (ord(f)>=48 and ord(f)<= 57):
             current_patter+="?d"
         elif (ord(f)>=33 and ord(f)<= 47):
             current_patter+="?s"
         else:
             current_patter+=f
    patern.append(current_patter)    
print(patern)

#print("/s", end = "")   # meselen her printden line dan sonra normalda \n yeni bir setr asagi dusurdu, cunki default olanda orda yazilmasa bele end="\n" demekdir. biz end = "" ederek yeni setr i hecne ile deyise bilerik.
