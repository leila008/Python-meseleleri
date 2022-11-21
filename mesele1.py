eded=int(input("Neceye qederki sade ededleri tapmaq isteyirsiniz?:"))
sade=[]
for i in range(2,eded):
    for j in range(2,i):
        if i%j==0:
            break
    else:
         sade.append(i)
print("0 ile {} arasinda {} dene sade eded var".format(eded,len(sade)))
