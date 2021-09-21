infile = open("Bicycle Routes.txt","r",encoding = "utf-8")
outfile = open("newBikeRoutes.txt","w",encoding = "utf-8")

for line in infile:
    '''if line.find('"properties"')!=-1:
        outfile.write(line[:line.find('"properties”')+12]+'"stroke-width":"5"'+line[line.find('"properties”')+12:])
    else:
        outfile.write(line)'''
        
infile.close()
outfile.close()
