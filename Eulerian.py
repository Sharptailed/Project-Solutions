from copy import *

def degree_checker(g):
    odd_list=[]
    for i in g:
        if len(g[i])%2==1:
            odd_list.append(i)
    return odd_list

def connected(g,search,current):
    for i in g[current]:
        if search[i]=="found":
            continue
        g[i].remove(current)
        g[current].remove(i)
        search[i]="found"
        g,search=connected(g,search,i)
    return g,search

def is_connected(g):
    search={}
    for i in g:
        search[i]=""
    search[1]="found"
    g,search=connected(g,search,1)
    for i in search:
        if search[i]=="":
            return True
    return False

def circuit(g,t):
    i,path,current,subpath,to_add=1,[],t,[],[]
    while len(g[i])!=0:
        while len(g[current])!=0:
            subpath.append(current)
            going=g[current][0]
            g[going].remove(current)
            g[current].remove(going)
            current=going
        subpath.append(current)
        while subpath!=[]:
            i=subpath[0]
            if len(g[i])!=0:
                subpath.remove(i)
                to_add,subpath,current=subpath+to_add,[],i
                continue
            path.append(i)
            subpath.remove(i)
    path=path+to_add
    return path

def Eulerian(g):
    oddlist,c,i=degree_checker(g),deepcopy(g),1
    if len(oddlist)==1 or len(oddlist)>2:
        return "Not Eulerian"
    if len(oddlist)==2:
        print("Path")
        c[oddlist[0]].append(oddlist[1])
        c[oddlist[1]].append(oddlist[0])
        t=oddlist[1]
    path=circuit(c,t)
    if not is_connected(g):
        return "Not Eulerian"
    elif len(oddlist)==2:
        path=path[:-1]
        return path
    else:
        return path
print(Eulerian({1:[2,5],2:[1,3],3:[2,4],4:[3],5:[1]}))