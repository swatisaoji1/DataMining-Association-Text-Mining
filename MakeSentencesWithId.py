'''
Created on Mar 6, 2015

@author: Swati
Modified from : 
'''
import sys
import re
import nltk
import os
from nltk.corpus import stopwords


def extractSent(filepaths):
    reload(sys)
    sys.setdefaultencoding("ISO-8859-1")  # @UndefinedVariable
    
    
    mydirectory = os.path.dirname(filepaths)
    outputfile = mydirectory+"\\Step1out"
    
    # make directory if does not exist
    if not os.path.exists(outputfile):
        os.makedirs(outputfile)

          
    #load all files
    files =[]
    for filename in open(filepaths, 'r'): files.append(filename.strip())
    
    #initialize sentence detector
    sentdetector = nltk.data.load('tokenizers/punkt/english.pickle')  
    
    #initialize regular expression pattern for family members
    familynames = re.compile(r'\b(mother|brother|grandfather|sister|grandmother|father|mom|dad|son|daughter|uncle|aunt|niece|nephew|cousin)(\'s|s)*\b', re.I)

    familysentences =[] 
    familysentences_nowords=[]

    counter = 0;
    sentence_count = 0
    for onefile in files:
        counter = counter + 1
        text = open(onefile, 'r').read() 
        #split into sentences
        sentences = sentdetector.tokenize(text.strip(), realign_boundaries=True)
             

        
        for sent in sentences:
            if familynames.search(sent) is not None :
                sentence_count = sentence_count+1
                sent =  sent.lower()
                # remove charaters other that alph numeric
                pattern = re.compile('[\W_]+', re.UNICODE)
                sent = re.sub(pattern, ' ', sent) 
                list_of_words =  sent.split()
                
                finalsent = ' '.join(list_of_words) #replace multiple spaces within sentence by one
                familysentences.append(finalsent.replace('\n','')) #sentences with stop words
                
                
                # removing the stop words =======================================
                
                list_of_words = [x for x in list_of_words if not (x.isdigit() or len(x) < 2)] 
                objStopWords = stopwords.words("english")
                finalsent = ' '.join([word for word in list_of_words if word not in objStopWords])
                familysentences_nowords.append(str(counter)+' '+ finalsent) # sentences without stop words
                  

    

    #===========================================================================
    # write output to file (full sentences)
    #===========================================================================
    file1 = outputfile+"\sentences_allwords.txt"
    outfile = open(file1 , 'w')
    for sent in familysentences:
    #print sent
        outfile.write(sent + '\n')

    outfile.close()  
    
    #===========================================================================
    # write output to file (no stop words) - id of record in the beginning of sent
    #===========================================================================
    file2 = outputfile+"\sentences_nostopwords.txt"
    outfile = open(file2, 'w')
    for sent in familysentences_nowords:
    #print sent
        outfile.write(sent + '\n')

    outfile.close()
    
    
    #===========================================================================
    # write output to file (My Runs)
    #===========================================================================
    file3 = outputfile+"\\MyRun.txt"
    outfile2 = open( file3, 'a')
    outfile2.write("Step 1: Output from sentence Splitter: \n")
    outfile2.write ('sentences containing one or more family members written:{} '.format(sentence_count))
    print (" ")
    print ('sentences containing one or more family members written:{} '.format(sentence_count))
    print ("Total Medical Records:{} ".format(counter))  

    return file1, file2, file3
    