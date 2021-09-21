infile = open("bikeFatalities5years.csv","r",encoding = "utf-8")
outfile = open("bikeFatalitiesMarkers","w",encoding = "utf-8")

for line in infile:
    arr=line.split(",")
    outfile.write("var circle = L.circle(["+arr[0]+", "+arr[1].strip()+"], {\n"
        +"color: 'red',\n"+"fillColor: 'red',\n"+"fillOpacity: 1.0,\n"+
        "radius: 25\n"+"}).addTo(myCircles);")
    outfile.write("\n\n")
infile.close()
outfile.close()
