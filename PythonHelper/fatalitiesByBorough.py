infile = open("cartodb-query (3).csv","r",encoding = "utf-8")

first = True
boroughs = ["MANHATTAN","BROOKLYN","QUEENS","BRONX","STATEN ISLAND"]
fatalitiesByBorough = [0,0,0,0,0]
fatalitiesByBoroughPct = [0,0,0,0,0]
for line in infile:
    if first:
        first = False
    else:
        splitLine = line.split(",")
        if splitLine[8].strip().upper() in boroughs:
            fatalitiesByBorough[boroughs.index(splitLine[8].strip().upper())] = fatalitiesByBorough[boroughs.index(splitLine[8].strip().upper())] +1

total = 0
for item in fatalitiesByBorough:
    total = total + item

for item in fatalitiesByBorough:
    fatalitiesByBoroughPct[fatalitiesByBorough.index(item)] = item/total

commutersByBorough = [20092,21918,5795,2457,632]

commutersTotal = 0
for commuters in commutersByBorough:
    commutersTotal = commutersTotal + commuters

commutersByPct = [0,0,0,0,0]
for commuters in commutersByBorough:
    commutersByPct[commutersByBorough.index(commuters)] = commuters/commutersTotal

for item in fatalitiesByBorough:
    index = fatalitiesByBorough.index(item)
    print(str(boroughs[index])+"\n")
    print("Fatalities: "+str(item))
    print("Percent of Total Fatalities: "+str(round(fatalitiesByBoroughPct[index],2)))
    print("Commuters: "+str(commutersByBorough[index]))
    print("Percent of Total Commuters: "+str(round(commutersByPct[index],2))+"\n")
