def find(l1,item):
    try:
        if l1.index(item)>=0:
            return 1
    except ValueError:
        return 0
def rotate(l):
    y=l[0]
    l=l[1:]
    l.append(y)
    return l
def find_all(l1,it):
    for i in range(6):
        y=rotate(it)
        if find(l1,y)==1:
            return 0
        it=y
    return 1            
f=open('input3.txt','r')
y=[]
while (1):
    x=f.readline()
    if x=="":
        break;
    x=x[1:-2]
    x=x.split(", ")
    x=list(map(int,x))
    y.append(x)
z=[]
for i in y:
    if find_all(z,i)==1:
        z.append(i)
print("Total no of Unique Rotational NCCA rules of 7 bit :",len(z))
for i in z:
    print(i)

    
