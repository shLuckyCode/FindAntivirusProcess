# -*-coding:utf-8-*-
import os
import sys

ANTIVIRUS = 'Antivirus.txt'


def LoadTraitTxtToDict(FilePath):
    try:
        File = open(FilePath, 'r')
    except IOError:
        print "File is not accessible."

    txtDict = {} #create Dict

    while True:
        line = File.readline()
        if line == '':
            break

        index = line.find('|')
        key = line[:index]
        value = line[index+1:]
        txtDict[key] = value[:-1]

    File.close()
    return txtDict




if __name__=="__main__":
    i = 0
    dstDict = LoadTraitTxtToDict(ANTIVIRUS)

    try:
        srcFile = open(sys.argv[1], 'r')
    except IOError:
        print "File is not accessible."

    while True:
        proLine = srcFile.readline()
        if proLine == '':
            break

        index = proLine.find(' ')
        key = proLine[:index]

        if '.exe' not in key.lower():
            continue

        if dstDict.has_key(key):
            print '%d %s %s' % (i, key, dstDict[key])
            i += 1

    if i == 0:
        print 'Dont find Antivirus process! '