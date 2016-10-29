def processFile(File):
    PD = 0
    PTN = 0
    for line in File:
        line = line.rstrip("\n")
        Temp = line.split(",")
        Dist = float (Temp[1])
        PD += Dist
        PTN += 1
    return PD,PTN

def printkv (key,value,klen):
    kl = max(len(key),klen)
    if isinstance(value, str):
        FS = '20s'
    elif isinstance(value, float):
        FS = '10.3f'
    elif isinstance(value, int):
        FS = '10s'
    else:
        print key
        print ':'
        print value
        print '/n'


File = input("First File")
totalnum = 0
totaldist = 0
while File and File != "quit" and File != "Q":
    FO = open(File,"r")
    partials = processFile(FO)
    file.close(FO)
    totalnum = partials[0]+totalnum
    totaldist = partials[1]+totalnum
    printkv('Partial #', partials[0])
    printkv('Partial Distance', partials[1])
    File = input("What is the name of the file?")
printkv('Total #', totalnum)
printkv('Total Distance', totaldist)






