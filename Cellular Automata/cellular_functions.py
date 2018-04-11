import random
from test15 import create
import numpy as np

'''creates a random rule vector of size n
   print(create_rule(5))'''
def create_rule(n):
    temp=[random.randint(0,255) for i in range(n)]
    return(temp)

''' defines a single transition and returns the changed state value
    print(transition('001',191)) '''
def transition(st,r):
    r=bin(r)[2:]
    r='00000000'[:-len(r)]+r
    r=r[::-1]
    st=int('0b'+st,2)
    return r[st]


'''returns a binary string by applying <rule> to string <bi>
    print(apply('111',[192,23,44]))'''
def apply(bi,rule):
    bi=bi[-1]+bi+bi[0]
    temp=[]
    for i in range(1,len(bi)-1):
        temp.append(transition(bi[i-1:i+2],rule[i-1]))
    return(''.join(temp))

'''print a random pattern of size(length) <n>
   print_pattern(10)'''
def print_pattern(n,k):
    for i in range(0,2**n):
        s=bin(i)[2:]
        string='0'*n
        string=string[:-len(s)]+s
        for i in range(k):
            rule=np.array(create_rule(len(string)))
            print('k=',i,'\t',string,"\t",rule)
            string=apply(string,rule)
        print('k=',k,'\t',string,'\n')

'''Given a rule vector and a size n (4<= n <=8),function to apply the rule vector to all the possible binary strings (2n)'''
def apply_all(n,rule):
	print('For Rule : ',rule)
	for i in range(0,2**n):
		s=bin(i)[2:]
		string='0'*n
		string=string[:-len(s)]+s
		print('String :',string,'\t->\t',apply(string,rule))


'''draw the space time diagram of given <string> and given <rule>
   particular_pattern('0'*80+'1'+'0'*80,[153]*161)'''
def particular_pattern(string,rule):
    st=[]
    for i in range(len(string)):
        st.append(string)
        string=apply(string,rule)
    create(st)
