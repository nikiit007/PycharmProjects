import datetime
def main(args):
    if len(args)==0:
        currdate=datetime.datetime.now()
    else:
        currdate=args[0]
    print(currdate)


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))

