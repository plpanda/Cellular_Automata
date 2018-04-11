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
def check1(n,rule):
    print("\n Rule : ",rule)
    var=[]
    global cnt
    var.append(16)
    x=pattern_defined(n,rule)
    print('x :       ',x,'\n')
    x=np.unique(np.array(x))
    var.append(len(x))
    count=1
    for i in range(10):
        y=pattern2(n,x,rule)
        print('x :       ',x,'\ny :       ',y)
        y=np.unique(np.array(y))
        print('unique y :',y,'\n')
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
def pattern2(n,vctr,rule):
    output=[]
    for i in vctr:
        s=bin(i)[2:]
        string='0'*n
        string=string[:-len(s)]+s
        output.append(apply(string,rule))
    output=[int('0b'+i,2) for i in output]
    return output
cnt=[0 for i in range(17)]
check1(4,[25,25,25,25])