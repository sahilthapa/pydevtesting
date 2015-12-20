#import gettext
#import os
from pydoc import describe

#gettext.textdomain('hello-python')
#gettext.bindtextdomain('hello-python', '@localedir@')

def fileReadTesting(str):
    describe("This just checks for reading data from a file")
    txt = open(str)
    dat = txt.readlines()
    for lines in dat:
        words = lines.split()
        print words
       

def fileWriteTesting(fname,str):
    describe("This just checks for reading data from a file")
    fHandle = open(fname,"a")
    fHandle.write("\n" + str)
    fHandle.close()
#print gettext.gettext("Hello, world!")
#print gettext.gettext("This program is running as process number %(pid)d.") \
#      % { 'pid': os.getpid() }
fname = "../data/testdata.csv"
fileWriteTesting(fname,"testing,123")
fileReadTesting(fname)