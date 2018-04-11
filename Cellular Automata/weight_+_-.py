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
    arr1=[]
    arr2=[]
    arr3=[]
    for i in range(0,len(string)):
        x=bin(i)[2:]
        p=sum(i=='1' for i in x)
        q=sum(j=='1' for j in string[i])
        if p==q:
            arr3.append(i)
        if p<=q:
            arr1.append(i)
        if p>=q:
        	arr2.append(i)
    return(arr1,arr2,arr3)
q1=[]
q2=[]
q3=[]
n=int(input())
for i in range(256):
    x=[i for j in range(n)]
    arr1,arr2,arr3=num_conserving(n,print_pattern_defined(n,x))
    perc=(len(arr1)/(2**n))*100
    if perc==100.0:
        q1.append(i)
    perc=(len(arr2)/(2**n))*100
    if perc==100.0:
        q2.append(i)
    perc=(len(arr3)/(2**n))*100
    if perc==100.0:
        q3.append(i)
print('Less than equal to : Total :',len(q1),'\n',q1)
print('Greater than equal to : Total :',len(q2),'\n',q2)
print('Equals to : Total :',len(q3),'\n',q3)
        
