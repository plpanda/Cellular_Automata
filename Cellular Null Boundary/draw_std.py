import itertools
from cellular_functions import *
import networkx as nx
import matplotlib.pyplot as plt

'''x=int(input("Enter elements of rule vector "))
st=input("Enter the rule vector :")
rule=list(map(int, st.split(' ')[:x]))
n=int(input("Enter elements of rule vector "))
comb=list(itertools.product(rule,repeat=n))'''


#problem 1 solution
def print_pattern_defined(n,rule):
    output=[]
    for i in range(0,2**n):
        s=bin(i)[2:]
        string='0'*n
        string=string[:-len(s)]+s
        output.append(apply(string,rule))
    return output
x=int(input("Enter the size of rule vector "))
st=input("Enter the rule vector :")
rule=list(map(int, st.split(' ')[:x]))
ans=print_pattern_defined(x,rule)
ans=[int('0b'+i,2) for i in ans]
print(ans)
g = nx.DiGraph()
g.add_nodes_from([i for i in range(len(ans))])
for i in range(0,len(ans)):
    g.add_edge(i,ans[i])
#pos=nx.fruchterman_reingold_layout(g)
#pos=nx.spring_layout(g)
pos=nx.shell_layout(g)
nx.draw(g,pos,with_labels=True)
#plt.savefig("weighted_graph.png")
plt.draw()
plt.show()

