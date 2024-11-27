# bitti
cumle=input("enter sentence: ")
array=cumle.split()

for i in range(len(array)):
    if(len(array[i])>5):
        array[i]="long"


samitler="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

mod_sentence=' '.join(array) # list mutable, array mutable, string immutable
#print(mod_sentence)

xello=''.join([char.upper() if char in samitler else char for char in mod_sentence])
print(xello)


