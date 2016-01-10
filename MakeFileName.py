'''
Created on Mar 8, 2015

@author: Swati

'''

import os
def makeFileName():
    somedirectory = raw_input("Enter Data Directory: ")
    outDirectory = raw_input("Enter OutPut directory: ")
    
    # open file to write
    out = open(outDirectory+"\\filename.txt", 'w')
    
    # make list of files in directory
    files = os.listdir(somedirectory)
    
    # write each file to output
    for eachfile in files:
        out.write(somedirectory + "\\" + eachfile + "\n")
    
    # return path to file created    
    return (outDirectory+"\\filename.txt")
    out.close()
