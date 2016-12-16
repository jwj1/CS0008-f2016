#
# MN: header with user, instructor and course info is missing
#
# Notes:
# MN: there is a good chunk missing but I do really appreciate the effort. Keep it up!!!
#


#Choosing the data with all the files in it
datasources = "f2016_cs8_a3.data.txt"
fj = open(datasources, 'r')
#opening it in read form
# MN: in mainfile, now you should have the list of the data files
mainfile = fj.readlines()
# MN: close does not need an argument
#fj.close("mainfile")
fj.close()

# MN: why do you define the list of data files here?
#     you do not know which data file you get unless you read the master list file
#     which you did right above
filenames = ['f2016_cs8_a3.data.1.csv', 'f2016_cs8_a3.data.2.csv', 'f2016_cs8_a3.data.3.csv']

# MN: it is unclear why you are doing this action below
#     I see that you combine the content of the data files. Why?
# MN: you need to specify a valid path and you need to open in writing
#with open('path/to/output/file', 'r') as outfile:
with open('temp_file.txt', 'w') as outfile:
    for fname in filenames:
        # MN: you need to open the file in reading
        #with open(fname) as infile:
        with open(fname,'r') as infile:
            outfile.write(infile.read())
#this was to combine my files

#
sourcefiles = [item.strip('/n') for item in mainfile]
#initialize data container
#loop on all the data files
data = []
for sources in sourcefiles:
    #open current data file for reading
    # MN: you need to remove \n from the end
    sources = sources.strip('\n')
    fj = open (sources, 'r')
    # MN: you need to use the file handle here
    #for line in data:
    for line in fj:
        # MN: you are appending the line 2 times
        #     if it is a header, you have to skip
        if not 'distance' in line:
            data.append(line.strip('\n'))
        #data.append(line)
        # 
        # MN: this statement is not needed
        #     you are already reading the lines with the loop above
        #     also here you are going to read everything else in the file in one shot
        #data = data.append(fj.readlines)

    fj.close()

# MN: you are computing the len of data, but where do you save the results?
#     remember you always need to assign any result to a variable, otherwise you loose it
#len (data)
number_of_lines_read = len(data)

# MN: there is a syntax error, the second ] needs to enclose the whole expression
#     also, you should convert it to float
#distances = [item.strip('\n').split(',')[1]] for item in data
distances = [float(item.strip('\n').split(',')[1]) for item in data]

# MN: this works, but have you thought that you already did some of the work in the statement right above?
#     you should reuse data as much as you can
# MN: same as above. syntax error
# 
#totaldistance = sum([float([item.strip('\n').split(',')[1] for item in data])])
totaldistance = sum(distances)

# MN: I assume that here you were trying to compute the individual distances run.
#     In order to do that you need a for loop because the expression is to complicated for a one liner
#indydistance = [item.strip('\n').plit)','[0] for item in data
# MN: initialize dictionary for partitipants tital distance
ind_distance = {}
# MN: loop on all the lines from the files
for line in data:
   # MN: split the line and extract the 2 portions
   temp = line.strip('\n').split(',')
   # MN: now in temp you have a list of 2 values: the first one is the name the second is the distance run
   # MN: check if you already found the name
   if temp[0] in ind_distance.keys():
      # MN: name already found
      #     add new distance
      ind_distance[temp[0]] += float(temp[1])
   else:
      # MN: new name
      #     define new element
      ind_distance[temp[0]] = float(temp[1])

# MN: now in ind_distance you have all the participants with their total distance run
#     key of the ditionary are the participant names
#     value is the total distance run by the participant
print("Number of lines read : " + str(number_of_lines_read))


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
