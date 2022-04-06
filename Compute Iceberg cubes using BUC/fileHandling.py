import csv

def readCsv(fileName): #here we read firstly read the dataset that we have to sort 
    header = ""
    with open(fileName, newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        data = []
        f = False
        for row in spamreader:
            if f == False:
                f = True
                header = row # texual heading extracted
                continue
            data.append([row[0],row[1],row[2],row[3],int(row[4])])
    return header,data

def writeResult(fileName,one,two,x,it,jt,yTick): #write the cuboids in result
    it = [x+1 for x in it]
    it.insert(0,0)
    jt = [x+1 for x in jt]
    jt.insert(0,0)
    with open(fileName, 'w') as write:
        #insert Item cuboids in text file
        write.writelines('-'*25+"Item"+'-'*25+"\n")
        for i in one:
            for j in i:
                write.write("{:^20}".format(j))
            write.write("\n")
        write.write("\n\n\n")
        #insert ItemLocation cuboids in text file
        write.writelines('-'*50+"ItemLocation"+'-'*50+"\n")
        for i in two:
            for j in i:
                write.write("{:^20}".format(j))
            write.write("\n")
        write.write("\n\n\n")
        #insert ItemLocationLocation cuboids in text file
        write.writelines('-'*50+"ItemLocationYear"+'-'*50+"\n")

        for k in range(len(x)):
            write.writelines('-'*25+"Year = "+ yTick[k]+'-'*25+"\n")
            cuboid = x[k]
            for i in it:
                for j in jt:
                    write.write("{:^20}".format(cuboid[i][j]))
                write.write("\n")
            write.writelines('\n')