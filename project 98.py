from unittest import result


print("Do you want to alter File 1 or File 2?")
print("Type 1 for reading Text 1 and 2 for reading Text 2.Type 3 for altering Text 1 and 4 for altering Text 2")
opted=int(input())

if(opted==1):
    data_1=open("C:/Users/pnb/OneDrive/Desktop/Python/Pro 97/sample1.txt",'r').read()
    print(data_1)

if(opted==2):
    data_2=open("C:/Users/pnb/OneDrive/Desktop/Python/Pro 97/sample2.txt","r").read()
    print(data_2)

if(opted==3):
    alter1=input("Rewrite Text 1 here.")

if(opted==4):
    alter2=input('Rewrite Text 2 here.')

open("C:/Users/pnb/OneDrive/Desktop/Python/Pro 97/sample1.txt",'w').write(alter1)
open('C:/Users/pnb/OneDrive/Desktop/Python/Pro 97/sample2.txt','w').write(alter2)