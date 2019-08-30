import random
f= open("rando.txt","w+")
randoList = [] 
for x in range(1000):
    temp = str(random.randint(1,1000000))
    f.write(temp + "\n")
    randoList.append(temp)
f.close()
