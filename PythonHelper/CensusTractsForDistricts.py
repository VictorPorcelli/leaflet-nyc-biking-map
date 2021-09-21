infile = open("NYC Council District Data - main database.csv","r",encoding = "utf-8")
#outfile = open("CouncilDistrictCensusTracts.txt","w",encoding = "utf-8")

tractsForDistricts = []
x = 1
for line in infile:
    arr = []
    arr.append(x)

    splitLine = line.split(",")
    notDone = True
    for i in splitLine:
        if notDone:
            newString = str(i)
            if newString.find("Census Tracts") != -1:
                newString = newString[newString.find(":")+2:]
                arr.append(newString)
                splitLine = splitLine[splitLine.index(i)+1:]
                notDone = False
            else:
                splitLine = splitLine[splitLine.index(i)+1:]

    for i in splitLine:
        if i != '' and i != '\n':
            arr.append(int(i.strip()))

    tractsForDistricts.append(arr)
    x+=1

print(tractsForDistricts)
infile.close()
