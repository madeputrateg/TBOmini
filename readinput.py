def bacainput(route):
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
    return simbol,state,dictornary,start,final
    
