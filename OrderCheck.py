'''
Created on Mar 6, 2015
@author: Swati

'''
import itertools
import re
import sys
import operator

  
    
def checkOrder(sentenceFile, mysetfile, mydir,  k ):

    
    outFile = mydir + "\\WordList_" + str(k) + ".txt"
    newFile = mydir + "\\FrequencySets_" + str(k) + ".txt"
    # put full sentences into a data struct - list of sentences
    sentfile = open(sentenceFile, 'r')
    sent = sentfile.readlines()
    sentfile.close()
    
    # Open the file for writting
    new_file = open(newFile, 'w')
    
    # open file for reading sets
    myfile = open(mysetfile, 'r')
    
    count =0
    frequencyd = {}
    for lines in myfile:
        # remove parenthesis and trailing and leading space if any
        lines = lines.replace('(','').replace(')','').strip() 
        bag = lines.split(' ')
        # support = bag[-1] #last item is support
        del bag[-1] # delete support
        
        permBag = list(itertools.permutations(bag))
        for onelist in permBag:
            count += 1
            frequency = 0
            
            for onesent in sent:
                onesent = onesent.strip()   
                pattern = re.compile('[\W_]+', re.UNICODE) # remove all charaters other than alpha numeric
                onesent = re.sub(pattern, ' ', onesent)  
                list_of_words = onesent.split(' ') # split into word list
                setwords = set(list_of_words)
                ok = 1    
                if set(onelist).issubset(setwords):
                    
                    index  = 0
                    for oneword in onelist:
                        if ok==1:
                            try:
                                # find the word and then reduce the wordlist to include only words after found word
                                # if all the following word is found the remaining lists -they are in order 
                                index = list_of_words.index(oneword)
                                list_of_words = list_of_words[index+1:]
                                
                            except:
                                ok= 0
                else:
                    ok = 0   
                if ok==1:
                    frequency += 1
            frequencyd[onelist] = frequency
            new_file.write(" ".join(onelist)
                           + " "
                           + str(frequency)
                           + "\n")
            

        if count%100 == 0 : sys.stdout.write('*')
            
    # out.close()  
    print ("\n" + str(count) + " sets checked for frequency in " + str(k) + " spanned sets")   
    myfile.close()
    return writeResults(frequencyd, outFile)
    
def writeResults(sup_data, out_file):
    
    # sort the output :
    sorted_support = sorted(sup_data.items(), key=operator.itemgetter(1), reverse=True)
    open_file = open(out_file , 'w')
    
    for x in sorted_support:
        items = x[0]
        frequency = x[1]
        if frequency > 0: #leave out frequency 0 associations
            open_file.write(" ".join(items))
            open_file.write(" ({0})\n".format(frequency))
    
    open_file.close()
    

        
        
   
        
    return out_file

