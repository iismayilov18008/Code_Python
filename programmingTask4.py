import os
inpath=input("inpath daxil edin: ").strip() 
outpath=input("outpath daxil edin: ").strip()

inpath=inpath.replace("\\", "\\\\")
outpath=outpath.replace("\\", "\\\\")
if(os.path.exists(outpath)):
    print("bele bir path artiq var")
    exit()
def copying(inpath, outpath):
    try:
        if ( (not os.path.exists(inpath)) or os.path.isfile(inpath) ):
            print(" Information u provided is not correct. ")
            exit()
        else:
            
            if(not os.path.exists(outpath)):
                os.makedirs(outpath)
            mezmun=os.listdir(inpath)
            
            for i in mezmun:
                altfile=inpath+"\\\\"+i
                altoutfile=outpath+"\\\\"+i
                if(os.path.isfile(altfile)):
                    yenifilepath=outpath+"\\\\"+i
                    with open(yenifilepath, 'w') as file:
                        pass
                elif(os.path.isdir(altfile)):
                    yeniqovluq=outpath+"\\\\"+i
                    os.mkdir(yeniqovluq)
                    copying(altfile, altoutfile)
                    
                                                                        
    except Exception as e:
        print(e)

copying(inpath, outpath)


        


