class DFAmachine:
    def __init__(self,route):
        route+=".txt"
        with open(route,'r') as f:
            dictornary={}
            lines =f.readlines()
            for i in range(len(lines)):
                lines[i]=lines[i][:len(lines[i])-1]
            simbol=lines[0].split(',')
            state=lines[1].split(',')
            for i in range(2,len(state)+2):
                dictornary[state[i-2]]={}
                arah=lines[i].split(',')
                for z in range(len(simbol)):
                    dictornary[state[i-2]][simbol[z]]=arah[z]
            start=lines[len(lines)-2]
            final=lines[len(lines)-1].split(',')
            state.sort()
            f.close()
            self.simbol=simbol
            self.state=state
            self.start=start
            self.final=set(final)
            self.trasition=dictornary
    def minimalize(self):
        martix={}
        state=self.state
        simbol=self.simbol
        dictornary=self.trasition
        final=self.final
        start=self.start
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
        self.start=transis[start]
        self.trasition=newnext
        self.state=[x for x in newnext]
        self.final=set(newfinal)
    def printDfa(self):
        print(" "*20,end="  ")
        for i in self.simbol:
            print(f"{i:^10}",end=" ")
        print("")
        for i in self.trasition:
            print(f"{i:<20}: ",end="")
            [print(f"{self.trasition[i][x]:^10}",end=" ") for x in self.simbol]
            print("")
        print("Quintuple:")
        sig="Σ"
        qu="Q"
        pristate="start state"
        prifina="final state"
        print(f"{qu:<25}: "+"{ε,"+",".join(self.state) +"}")
        print(f"{sig:<25}: "+"{"+",".join(self.simbol) +"}")
        print(f"{pristate:<25}: " + str(self.start))
        print(f"{prifina:<25}: " + str(self.final))
        print("delta:")
        for i in self.trasition:
            for z in self.simbol:
                print("𝛿({},{})={}".format(i,z,self.trasition[i][z]))

