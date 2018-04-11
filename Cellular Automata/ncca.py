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
def print_pattern(n,rule):
    output=[]
    for i in range(0,2**n):
        s=bin(i)[2:]
        string='0'*n
        string=string[:-len(s)]+s
        print(i,' = ',string,' -> ',apply(string,rule))
def num_conserving(string,d):
    flag=0
    for i in range(0,len(string)):
        x=bin(i)[2:]
        p=sum(i=='1' for i in x)
        if p==0:
            continue
        if p == sum(j=='1' for j in string[i]):
            flag=1
        else:
            flag=0
            break
    return flag
'''print("weight of input-1 = weight of output")
for i in range(0,256):
    x=[i,i,i,i,i]
    y = print_pattern_defined(5,x)
    if num_conserving(y,5):
        print(x)'''
'''x=9#int(input("Enter elements of rule vector "))
st="136 170 184 192 204 226 238 240 252"#input("Enter the rule vector :")
rule=list(map(int, st.split(' ')[:x]))

#n=int(input("Enter no of elements of rule vector "))
for n in range(5,8):
    comb=list(itertools.product(rule,repeat=n))
    count=0
    for i in comb:
        x=print_pattern_defined(n,i)
        if num_conserving(x,n):
            print(i)
            count+=1
    print("Total no of ",n," bit NCCA rules ",count,"\n\n")

'''