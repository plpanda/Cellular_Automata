import itertools
import numpy as np
from cellular_functions import *

def pattern_defined(n,rule):
    output=[]
    for i in range(0,2**n):
        s=bin(i)[2:]
        string='0'*n
        string=string[:-len(s)]+s
        output.append(apply(string,rule))
    output=[int('0b'+i,2) for i in output]
    return output

def pattern2(n,vctr,rule):
    output=[]
    for i in vctr:
        s=bin(i)[2:]
        string='0'*n
        string=string[:-len(s)]+s
        output.append(apply(string,rule))
    output=[int('0b'+i,2) for i in output]
    return output

def check2(n,rule):
    print("\n Rule : ",rule)
    
    x=pattern_defined(n,rule)
    print([i for i in range(0,2**n)],"\t",x)
    x=np.unique(np.array(x))
    

    for i in range(10):
        y=pattern2(n,x,rule)
        print(x,"\t\t\t",y)
        y=np.unique(np.array(y))
        if np.array_equal(x,y):
            break
        else:
            x=y
def check1(n,rule):
    print("\n Rule : ",rule)

    var=[]
    global cnt
    var.append(16)
    x=pattern_defined(n,rule)
    x=np.unique(np.array(x))
    var.append(len(x))
    count=1
    for i in range(10):
        y=pattern2(n,x,rule)
        y=np.unique(np.array(y))
        if np.array_equal(x,y):
            break
        else:
            x=y
            count=count+1
            var.append(len(x))
    print('No of layers : ',count)
    print('Distinct count in layers: ',var)
    cnt[var[-1]]=cnt[var[-1]]+1
    print('Output vector: ',x)
cnt=[0 for i in range(17)]
def check(n,rule):
    print("\nRule : ",rule)
    arr=[[0 for i in range(16)] for i in range(16)]
    x=pattern_defined(n,rule)
    x1=np.unique(np.array(x))
    for i in range(16):
        arr[i][x[i]]=1
    for i in range(10):
        y=pattern2(n,x,rule)
        y1=np.unique(np.array(y))
        if np.array_equal(x1,y1):
            for j in range(16):
                if(arr[j][x[j]]==0):
                    arr[j][x[j]]=1+i
            break
        else: 
            for j in range(16):
                if(arr[j][x[j]]==0):
                    arr[j][x[j]]=1+i
            x=y
            x1=y1
    print("  \t::> ",[i for i in range(16)])
    for i in range(16):
        print(i,"\t::> ",arr[i])
#check1(4,[136,184,184,252])
#check(4,[136,184,184,252])
'''for l in range(0,256):
    x=[l,l,l,l]
    check(4,x)
    print("\n")'''
x=[171, 174, 175, 185, 186, 187, 188, 189, 190, 191, 205, 206, 207, 220, 221, 222, 223, 227, 230, 231, 234, 235, 236, 237, 238, 239, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255]
for i in x:
    y=[i,i,i,i]
    check(4,y)
    print("\n")
