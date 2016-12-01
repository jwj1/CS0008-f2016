#
# MN: need header with info about user, instructor, course
#
# Notes:
# MN: you need to insert more comments describing each block of code
#

# MN: what does this function do?
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

# MN: what does this function do?
def printkv (key,value,klen=20):
    kl = max(len(key),klen)
    if isinstance(value, str):
        FS = '20s'
    elif isinstance(value, float):
        FS = '10.3f'
    elif isinstance(value, int):
        FS = '10d'
    # MN: if you insert this else, the prints will never be executed
    #else:
    #    print key
    #    print ':'
    #    print value
    #    print '/n'
    # MN: here how it should be done with format
    print(format(key,str(kl) + 's') + ' : ' + format(value,FS)) 


File = input("First File")
totalnum = 0
totaldist = 0
# MN: you need to transform File to lower case when you test it
#while File and File != "quit" and File != "q":
while File and File.lower() != "quit" and File.lower() != "q":
    FO = open(File,"r")
    partials = processFile(FO)
    #
    # MN: file is not defined. You need to close the file handle that is FO
    #file.close(FO)
    FO.close()

    totalnum = partials[0]+totalnum
    # MN: you need to add the total distance
    #totaldist = partials[1]+totalnum
    totaldist = partials[1]+totaldist
    printkv('Partial #', partials[0])
    printkv('Partial Distance', partials[1])
    File = input("What is the name of the file?")
printkv('Total #', totalnum)
printkv('Total Distance', totaldist)






