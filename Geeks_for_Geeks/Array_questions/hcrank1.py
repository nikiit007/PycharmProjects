#!/usr/bin/env python3

def main(args):

   cl=[[38, 130, 500], [21, 280, 1800], [13, 120, 1500]]
   W = 300
   res=findTruckCargo(W, cl)
   print(res)






def findTruckCargo(maxCargoWeight,cargoList):
    W=maxCargoWeight
    cl=cargoList
    val = [i[2] for i in cl]
    wt = [i[1] for i in cl]
    name = [i[0] for i in cl]
    n = len(val)
    res = knapSzeroone(W, wt, val, n, name)
    return res

def knapSzeroone(W, wt, val, n,name):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
    items=[[None for x in range(W + 1)] for x in range(n + 1)]


    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
                items[i][w]=None
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
                if (val[i - 1] + K[i - 1][w - wt[i - 1]]> K[i - 1][w]):
                    items[i][w]=str(name[i-1])+","+str(items[i - 1][w - wt[i - 1]])
                else:
                    items[i][w]=str(items[i-1][w])
            else:
                K[i][w] = K[i - 1][w]
                items[i][w]=str(items[i-1][w])

    c=[int(i) for i in (items[n][W]).split(",") if i!='None']
    c.reverse()
    c.append(K[n][W])

    return c






if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
