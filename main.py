
import readinput

route="new.txt"
simbol,state,dictornary,start,final = readinput.bacainput(route)
martix={}
for i in range(1,len(state)):
    martix[state[i]]={}
    for z in range(i):
        martix[state[i]][state[z]]=""
for i in range(1,len(state)):
    for z in range(i):
        if ((state[z] in final)!= (state[i] in final)):
            martix[state[i]][state[z]]="ε"
            # martix[state[z]][state[i]]="ε"   

flag=True
while flag:
    flag=False
    for i in range(1,len(state)):
        for z in range(i):
            for k in simbol:
                fs=dictornary[state[i]][k]
                ss=dictornary[state[z]][k]
                if ss==fs:
                    continue
                if fs<ss :
                    fs ,ss = ss ,fs
                if(martix[state[i]][state[z]]=="" and fs!=ss and martix[fs][ss]!=""):
                    martix[state[i]][state[z]]=k
                    # martix[state[z]][state[i]]=k
                    flag=True
                    break

for i in martix:
    print(i,end=": ")
    print(martix[i])

newstate=[]
transis={}
for i in state:
    transis[i]=set([i])

for i in martix:
    for z in martix[i]:
        if martix[i][z]=="":
            kws=transis[i].union(transis[z])
            transis[i]=kws
            transis[z]=kws

for i in transis:
    transis[i]="/".join(sorted(transis[i]))

newnext={}
newfinal=[]
for i in dictornary:
    newnext[transis[i]]={}
    for z in dictornary[i]:
        newnext[transis[i]][z]=transis[dictornary[i][z]]
for i in final:
    newfinal.append(transis[i])
newfinal=set(newfinal)
newstart=transis[start]

print(" "*20,end="  ")
for i in simbol:
    print(f"{i:^10}",end=" ")
print("")
for i in newnext:
    print(f"{i:<20}: ",end="")
    [print(f"{newnext[i][x]:^10}",end=" ") for x in simbol]
    print("")
print("start state         : " + str(newstart))
print(f"final state         : " + str(newfinal))
