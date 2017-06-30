#!/usr/bin/env python3
def insertcharat(word, first, j):
    start = word[0:j]
    end = word[j:]
    return start + first + end


def getperms(str):
    if str is None:
        return None

    permutations = []

    if len(str) == 0:
        permutations.append("")
        return permutations

    first = str[0]
    remainder = str[1:]
    words = getperms(remainder)

    for word in words:
        for j in range(len(word) + 1):
            s = insertcharat(word, first, j)
            permutations.append(s)

    return permutations


def getperms1(str):
    permutations = []

    if len(str) == 0:
        permutations.append("")
        return permutations

    for i in range(len(str)):
        before = str[:i]
        after = str[i + 1:]
        partials = getperms1(before + after)
        for s in partials:
            permutations.append(str[i] + s)
    return permutations


def getperms2(prefix, str, permutations):
    if len(str) == 0:
        permutations.append(prefix)
        return

    for i in range(len(str)):
        before = str[:i]
        after = str[i + 1:]
        getperms2(prefix + str[i], before + after, permutations)


def getperms_with_dups(freq, prefix, remaining, permutations):
    if remaining == 0:
        permutations.append(prefix)
        return
    for i in freq.keys():
        count = freq[i]
        if count > 0:
            freq[i] -= 1
            getperms_with_dups(freq, prefix + i, remaining - 1, permutations)
            freq[i] += 1.0


def getperms_helper(str):
    result = []
    getperms2('', str, result)
    return result


def getperms_dups_helper(str):
    freq = {}
    result = []
    for i in str:
        if i not in freq.keys():
            freq[i] = 1
        else:
            freq[i] += 1
    getperms_with_dups(freq, "", len(str), result)
    return result


def main(args):
    s = "apple"
    print(getperms_dups_helper(s))
    print(len(getperms_dups_helper(s)))


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
