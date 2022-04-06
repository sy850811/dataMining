from helpers import uniqun,findFirst
def Item(cuboids,data,numDims,cardinality,cardinalityUn,header):
    it=[]
    for i in uniqun(data,0):
        it.append(findFirst(cardinalityUn[0][1], numDims, i))
    yTick = cardinality[header.index('Item')][1]
    one = [[yTick[i],cuboids['Item'][i]] for i in it]
    one.insert(0,[' ','Sales'])
    return it,one,yTick

def ItemLocation(cuboids,data,numDims,cardinalityUn,it,header,yTick):
    two=[]
    jt=[]
    for i in uniqun(data,1):
        jt.append(findFirst(cardinalityUn[1][1], numDims, i))
    cuboid = cuboids['ItemLocation']
    two.append([' '] + cardinalityUn[header.index('Location')][1])
    for i in it:
        c = [yTick[i]]
        for j in jt:
            c.append(cuboid[i][j])
        two.append(c)
    return jt,two

def ItemLocationYear(cuboids,cardinality,cardinalityUn,header,numDims,data,it,jt):

    arrC = list([ [[0 for k in range(4)] for j in range(4)] for i in range(2)])
    for i in range(4):
        for j in range(4):
            for k in range(2):
                arrC[k][i][j] = cuboids['ItemLocationYear'][i][j][k]
    x = arrC
    for i in range(len(x)):
        for j in range(len(x[i])):
            x[i][j].insert(0,cardinality[header.index('Item')][1][j])
        x[i].insert(0,[' '*7]+cardinality[header.index('Location')][1])
    return jt,x





    # x=[]
    # arrC = list([ [[0 for k in range(4)] for j in range(4)] for i in range(2)])
    # for i in range(4):
    #     for j in range(4):
    #         for k in range(2):
    #             arrC[k][i][j] = cuboids['ItemLocationYear'][i][j][k]
    # x = arrC
    # for i in it:
    #     for j in jt:
    #         x[i][j-1].insert(0,cardinality[header.index('Item')][1][j-1])
    #     x[i].insert(0,[' ']+cardinality[header.index('Location')][1])
    # jt=[0]
    # for i in uniqun(data,1):
    #     jt.append(findFirst(cardinalityUn[1][1], numDims, i)+1)
    # return jt,x