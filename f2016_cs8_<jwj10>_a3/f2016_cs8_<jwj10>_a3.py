#Choosing the data with all the files in it
datasources = "f2016_cs8_a3.data.txt"
fj = open(datasources, 'r')
#opening it in read form
mainfile = fj.readlines()
fj.close("mainfile")

filenames = ['f2016_cs8_a3.data.1.csv', 'f2016_cs8_a3.data.2.csv', 'f2016_cs8_data.3.csv']
with open('path/to/output/file', 'r') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            outfile.write(infile.read())
#this was to combine my files

sourcefiles = [item.strip('/n') for item in mainfile]
#initialize data container
#loop on all the data files
data = []
for sources in sourcefiles:
    #open current data file for reading
    fj = open (sources, 'r')
    for line in data:
        if not 'distance' in line:
            data.append(line.strip('\n'))
        data.append(line)
        data = data.append(fj.readlines)

    fj.close()
len (data)

distances = [item.strip('\n').split(',')[1]] for item in data
totaldistance = sum([float([item.strip('\n').split(',')[1]] for item in data)])

indydistance = [item.strip('\n').plit)','[0] for item in data
 # I don't know exactly what I have so far. I don't even really know how to read it.
#I'm pretty sure that I have the files combined.
# I think I have the length of the files and the the distance, total distance, and individual distance.
#I am going to attempt to do the rest of the actions. I already know that I won't be able to get the print format.

# Just want you to know that I'm doing my best!
# Since i don't know how to do it im just going to tell you what i would do.

# I would write a loop that goes through the file and seperates the name from the distances.
    #then it would find the corresponding max and min for those names.
    #if there are more than one instance of a name i want it to still pick the lowest and highest.
    #

# I want to write a loop that looks through all of the names and counts how many there are.
    #then for each repeat in a name, i want it to add the distance to the distance of the other instance of the neame
    #then i would tell it to report how many times it found the name

# After I got all the necessry information I would print it in the format given on the sheet.
    #then I would also create the file with all the names and distances on it.

# I just got lost in all the work I was doing to get the files togehter.
    #I also didn't know how to go through and get the names and do anything with the repeats.
    #I also don't know how to figure out the print format. I've never succesfully done it.