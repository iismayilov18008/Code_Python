# not complete


import random

try:
    def a():
        santaclaus = ["nuraya", "saida", "ismayil", "vinly", "emiray", "lamiye", "albert", "murad"]
        counter=0        

        hediyyeVerenList=santaclaus.copy()
        hediyyeAlanList=santaclaus.copy()
        while True:
            counter+=1
            # if counter > 9:
            #     raise Exception()
            #     print("try again:")
            #     a()
            
            hediyyeAlan=random.choice(hediyyeAlanList)
            hediyyeVeren=random.choice(hediyyeVerenList)
            if (hediyyeAlan == hediyyeVeren and counter<8):
                continue
            elif(hediyyeAlan == hediyyeVeren and counter>8):
                print("too many attempts")
                a()
            else: 
                print(f"{hediyyeVeren}, {hediyyeAlan} a hediyye aldi ")
                hediyyeAlanList.remove(hediyyeAlan)
                hediyyeVerenList.remove(hediyyeVeren)
            if((not hediyyeVerenList )and (not hediyyeAlanList)):
                print("bitti.")
                exit()
except Exception as e:
    print(e)
    
    
            
        
