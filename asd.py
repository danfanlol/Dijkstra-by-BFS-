graph = {1:[[2,1]],2:[[3,1],[1,1],[4,1]],3:[[2,1],[4,1],[5,5]],4:[[2,1],[3,1],[5,2]],5:[[4,2],[3,5],[6,4]],6:[[5,4],[7,2]],7:[[6,2]]}

pointer = {1:{2:0},2:{3:0,1:1,4:2,7:3},3:{2:0,4:1,5:2},4:{2:0,3:1,5:2},5:{4:0,3:1,6:2},6:{5:0,7:1},7:{6:0,2:1}}


c = 0

q = []
filler = []
values = [0,-1,-1,-1,-1,-1,-1]
CN = 1

while True:
    smallestedge = 100000000
    for nodeset in graph[CN]:
        if nodeset[1] < smallestedge and nodeset[1] > 0:
            smallestedge=  nodeset[1]
    c += smallestedge
    for i in range(len(graph[CN])):
        node = graph[CN][i][0]
        if (values[node-1] == -1):
            graph[CN][i][1] -= smallestedge
            graph[node][pointer[node][CN]][1] -= smallestedge
            if (graph[node][pointer[node][CN]][1] == 0):
                filler.append(node)
                values[node-1] = c
        else:
            graph[CN][i][1] = 0
            graph[node][pointer[node][CN]][1] = 0
    
    for extra in q:
        for i in range(len(graph[extra])):
            node = graph[extra][i][0]
            if (values[node-1] == -1):
                graph[extra][i][1] -= smallestedge
                graph[node][pointer[node][extra]][1] -= smallestedge
                if (graph[node][pointer[node][extra]][1] == 0):
                    q.append(node)
                    values[node-1] = c
            else:
                graph[extra][i][1] = 0
                graph[node][pointer[node][extra]][1] = 0
    
    for k in filler:
        if k != CN and k not in q:
            q.append(k)
    
    allzero = True
    for nodeset in graph[CN]:
        if nodeset[1] != 0:
            allzero = False
            break
    lowest = 1000000
    smallestnode = -1
    for node in q:
        for nodeset in graph[node]:
            if nodeset[1] < lowest and nodeset[1] > 0:
                lowest=  nodeset[1]
                smallestnode = node
    if smallestnode == -1:
        break
    if allzero:
        q.remove(smallestnode)
        CN = smallestnode
    else:
        smallestedge = 10000000
        for nodeset in graph[CN]:
            if nodeset[1] < smallestedge and nodeset[1] > 0:
                smallestedge=  nodeset[1]
        if lowest < smallestedge:
            q.append(CN)
            q.remove(smallestnode)
            CN = smallestnode


    for node in q:
        allzero = True
        for nodeset in graph[node]:
            if nodeset[1] != 0:
                allzero = False
                break
        if allzero:
            q.remove(node)
    if CN in q:
        q.remove(CN)

 
