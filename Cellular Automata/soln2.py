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
def num_conserving(i,string):
    flag=-1
    flag1=-1
    #print("\n",i)
    for i in range(0,len(string)):
        x=bin(i)[2:]
        #print("initial wt =",sum(i=='1' for i in x),"\t Final wt=",sum(j=='1' for j in string[i]))
        if sum(i=='1' for i in x) <= sum(j=='1' for j in string[i]):
            if flag!=0:
                flag=1
        else:
            flag=0
        if sum(i=='1' for i in x) >= sum(j=='1' for j in string[i]):
            if flag1!=0:
                flag1=1
        else:
            flag1=0
    return flag,flag1


x=int(input("Enter elements of rule vector "))
st=input("Enter the rule vector :")
rule=list(map(int, st.split(' ')[:x]))

n=int(input("Enter no of elements of rule vector "))

comb=list(itertools.product(rule,repeat=n))
cnt1=0
cnt2=0
for i in comb:
    p=print_pattern_defined(n,i)
    x,y=num_conserving(i,p)
    if x>0:
        cnt1+=1
        print(i,"  incr ")
    if y>0:
        cnt2+=1
        print(i,"  decr ")
print("increasing : ",cnt1,"\t decreasing : ",cnt2)
