import itertools
from cellular_functions import *

def print_pattern_defined(n,rule):
    output=[]
    for i in range(0,2**n):
        s=bin(i)[2:]
        string='0'*n
        string=string[:-len(s)]+s
        output.append(apply(string,rule))
    return output
def num_conserving(string):
    flag=0
    for i in range(0,len(string)):
        x=bin(i)[2:]
        p=sum(i=='1' for i in x)
        if p==0:
            continue
        if p-1 == sum(j=='1' for j in string[i]):
            flag=1
        else:
            flag=0
            break
    return flag
def dense(n,no):
    r=bin(no)[2:]
    r=('0'*n)[:-len(r)]+r
    a=sum(j=='1' for j in r)
    b=n-a
    if a>b:
        return 0
    elif a<b:
        return 1
    else:
        return 2
def chk_dense(n):
    x=[[],[],[]]
    for i in range(0,2**n):
        if(dense(n,i))==0:
            x[0].append(i)
        elif (dense(n,i))==1:
            x[1].append(i)
        else:
            x[2].append(i)
    for i in x:
        print(i)
chk_dense(8)
        
    
    
