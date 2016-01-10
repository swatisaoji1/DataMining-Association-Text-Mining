'''
Created on Mar 6, 2015

@author: Swati
'''
import csv
import re
import os

"""

"""
 
def makeBagOfWords(filename):
   
    mydirectory = os.path.dirname(filename)
    outputfile = mydirectory+"\\bagOfWords.csv"
    
    myfile = open(filename, 'r')
    with open(outputfile,'w') as out:
        csv_out=csv.writer(out)
        counter = 0
        for oneline in myfile:
            counter += 1
            oneline = oneline.replace('\n', '')
            list_of_words = oneline.split(' ')
            csv_out.writerow(list_of_words)
    myfile.close()
    out.close()
    
    print ( "{} lines broken into words".format(counter))
    return outputfile
