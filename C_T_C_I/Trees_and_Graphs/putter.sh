#!/bin/bash
filename=$1
echo "#!/usr/bin/env python3
def main(args):
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))">$filename

