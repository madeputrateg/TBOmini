def make(route):
    route+=".txt"
    #menambahkan .txt di namanya agar lebih mudah dipanggil nantinya.
    print("masukan simbol")
    simbol= input().split()
    #meminta simbol DFA berupa 1 line yang dipisahkan oleh spaci
    print("masukan state")
    state=input().split()
    #meminta state pada 1 line yang dipisahkan oleh spaci
    transtate=[]
    for i in state:
        sub=[]
        for z in simbol:
            print("masukan arah transisi pada 𝛿({},{})=".format(i,z),end="")
            sub.append(input())
        transtate.append(sub)
    #meminta seluruh transisi yang ada pada transisi
    print("masukan startstate")
    startstate=input()
    #memintak starting state
    while not (startstate in state):
        print("masukan startstate")
        startstate=input()
    #memintak ulang starting state apabila starting state tidak  ada di state yang ada
    print("masukan finalstate")
    finalstate=input().split()
    #memintak final state
    with open(route,"w") as f:
        f.write(",".join(simbol)+"\n")
        f.write(",".join(state)+"\n")
        for i in range(len(transtate)):
            f.write(",".join(transtate[i])+"\n")
        f.write(startstate+"\n")
        f.write(",".join(finalstate)+"\n")
        f.close()
    #menyimpan seluruh data pada file 