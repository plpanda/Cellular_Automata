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
def num_conserving(n,string):
    arr=[]
    for i in range(0,len(string)):
        x=bin(i)[2:]
        p=sum(i=='1' for i in x)
        q=sum(j=='1' for j in string[i])
        #if p==n:
            #continue
        if p==q:
            arr.append(i)
    return(arr)
q=[]
n=int(input())
for i in range(256):
    x=[i for j in range(n)]
    arr=num_conserving(n,print_pattern_defined(n,x))
    perc=(len(arr)/(2**n))*100
    if perc==100.0:
        q.append(i)
print(q)
print(len(q))
        
