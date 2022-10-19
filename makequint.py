def make(route):
    route+=".txt"
    print("masukan simbol")
    simbol= input().split()
    print("masukan state")
    state=input().split()
    transtate=[]
    for i in state:
        sub=[]
        for z in simbol:
            print("masukan arah transisi pada 𝛿({},{})=".format(i,z),end="")
            sub.append(input())
        transtate.append(sub)
    print("masukan startstate")
    startstate=input()
    while not (startstate in state):
        print("masukan startstate")
        startstate=input()
    print("masukan finalstate")
    finalstate=input().split()
    with open(route,"w") as f:
        f.write(",".join(simbol)+"\n")
        f.write(",".join(state)+"\n")
        for i in range(len(transtate)):
            f.write(",".join(transtate[i])+"\n")
        f.write(startstate+"\n")
        f.write(",".join(finalstate)+"\n")
        f.close()