#!/usr/bin/env python3
def main(args):
    a=DJob("a")
    b=DJob("bs")
    c=DJob("sas")
    a.depjobs=[b,c]

    print(a.name)
    print(" ")
    print(c.name)
    print(" ")
    recur_jobstatus(a)



def recur_jobstatus(Djob_obj):
    print(Djob_obj.name)
    if Djob_obj is None:
        return
    for i in Djob_obj.depjobs:
        recur_jobstatus(i)



class DJob:
    def __init__(self,name):
        self.name=name
    depjobs=[]
    deppaths=[]



if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))

