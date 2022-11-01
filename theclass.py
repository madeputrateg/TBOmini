class DFAmachine:
    def __init__(self,route):
        #fungsi ini dipanggil sebagai constructor mesin dfa
        route+=".txt"
        with open(route,'r') as f:
            dictornary={}
            #membuat ditonary untuk menyimpan seluruh transisi yang bisa dilakukan state
            lines =f.readlines()
            #membaca semua lines yang ada
            for i in range(len(lines)):
                lines[i]=lines[i][:len(lines[i])-1]
            #menghapus \n pada semua line yang ada
            simbol=lines[0].split(',')
            state=lines[1].split(',')
            #memisahkan semua state dan simbol yang dipisahkan menggunakan koma
            for i in range(2,len(state)+2):
                dictornary[state[i-2]]={}
                arah=lines[i].split(',')
                for z in range(len(simbol)):
                    dictornary[state[i-2]][simbol[z]]=arah[z]
            #menyimpan transisi dari state di dalam dictonary berdasarkan state dan simbol
            start=lines[len(lines)-2]
            final=lines[len(lines)-1].split(',')
            #menyimpan starting state dan final state yang ada
            state.sort()
            f.close()
            #menutup file yang dibaca
            self.simbol=simbol
            self.state=state
            self.start=start
            self.final=set(final)
            self.trasition=dictornary
            #menyimpan data bahasa di dalam object DFAmachine
    def minimalize(self):
        martix={}
        #membuat dictonary agar dapat menyimpan martix segitiga mengunakan table filling
        state=self.state
        simbol=self.simbol
        dictornary=self.trasition
        final=self.final
        start=self.start
        #meyimpan semua data object ke dalam fungsi agar tidak merubah data object jika terjadi kesalahan
        for i in range(1,len(state)):
            martix[state[i]]={}
            for z in range(i):
                martix[state[i]][state[z]]=""
        #membuat matrix segitiga mengunakan dictonary
        for i in range(1,len(state)):
            for z in range(i):
                if ((state[z] in final)!= (state[i] in final)):
                    martix[state[i]][state[z]]="ε"
                    # martix[state[z]][state[i]]="ε"
        #memngisi semua epsilon yang ada   
        flag=True
        while flag:
            flag=False
            for i in range(1,len(state)):
                for z in range(i):
                    for k in simbol:
                        fs=dictornary[state[i]][k]
                        ss=dictornary[state[z]][k]
                        #mentrasisi state dan menyimpan hasil transisi kedalam ss dan fs
                        if ss==fs:
                            continue
                        #apabila hasil transisi sama maka akan diskip
                        if fs<ss :
                            fs ,ss = ss ,fs
                        #apabila state fs lebih besar dari pada ss maka akan ditukar karena menggunakan matrix segita agar tidak melebihi
                        if(martix[state[i]][state[z]]=="" and fs!=ss and martix[fs][ss]!=""):
                            martix[state[i]][state[z]]=k
                            # martix[state[z]][state[i]]=k
                            flag=True
                            break
        #loop akan terulang hingga semua state tidak berubah lagi
        transis={}
        for i in state:
            transis[i]=set([i])
        #menyiapkan sebuah dictonary yang dapat mentranslate state yang sebelumnya dan yang baru.
        for i in martix:
            for z in martix[i]:
                if martix[i][z]=="":
                    kws=transis[i].union(transis[z])
                    transis[i]=kws
                    transis[z]=kws
        #mengset hasil transisi yang baru mengukan set union jika terdapat tabel yang kosong
        for i in transis:
            transis[i]="/".join(sorted(transis[i]))
        #mengubah transisi yang menghasilkan set menjadi string agar bisa digunakan untuk dictonary
        newnext={}
        newfinal=[]
        for i in dictornary:
            newnext[transis[i]]={}
            for z in dictornary[i]:
                newnext[transis[i]][z]=transis[dictornary[i][z]]
        #membuat tabel transisi dari bahasa DFA yang telah diminimalisasi dan menyimpannya di dalam dictonary newnext
        for i in final:
            newfinal.append(transis[i])
        #mengubah final state menjadi state di dfa baru
        self.start=transis[start]
        self.trasition=newnext
        self.state=[x for x in newnext]
        self.final=set(newfinal)
        #menyimpan data ke dalam object
    def printDfa(self):
        #intinya fungsi ini mencetak semua data yang ada pada suatu object DFAmachine
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

