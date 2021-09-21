infile = open("ACSST5Y2019.S2001_data_with_overlays_2021-04-07T164413.csv","r",encoding = "utf-8")
medIncomeByTract = []

for line in infile:
    splitLine = line.split(",")
    dummyValue = splitLine[1][splitLine[1].find("Tract")+6:]
    medIncomeByTract.append([float(dummyValue[:dummyValue.find(" ")]),splitLine[4]])

infile.close()

for medinc in medIncomeByTract:
    print(medinc[1])
    #if medinc[1].find(" ") != -1:
        #print("yo")

'''

infile2 = open("geoJSON","r",encoding = "utf-8")
outfile = open("newGeoJSON.txt","w",encoding = "utf-8")

for line in infile2:
    outfile.write(line)
    censusTract = ""
    if line.find("CTLabel") != -1:
        censusTract = line[line.find("CTLabel")+12:]
        censusTract = censusTract[:censusTract.find(",")-1]
        for i in medIncomeByTract:
            if i[0] == float(censusTract):
                outfile.write('        "MedianIncome" : "'+i[1]+'",\n')
                break
                

infile2.close()
outfile.close()'''
                
