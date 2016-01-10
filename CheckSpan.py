'''
Created on Mar 6, 2015

@author: Swati
'''
import re
def checkSpan(sentenceFile, mysetfile, outpath, k ):
    
    outFile = outpath +"\\span" + str(k) + ".txt"
    
    # put full sentences into a data struct - list of sentences
    sentfile = open(sentenceFile, 'r')
    sent = sentfile.readlines()
    sentfile.close()
    
   
    
    # Open the file for writting
    out = open(outFile, 'w')
    
    myfile = open(mysetfile, 'r')
    countsetsdone =0
    items = 0
    for lines in myfile:
        countsetsdone +=1
        
        # remove parenthesis and trailing and leading space if any
        lines = lines.replace('(','').replace(')','').strip() 
        bag = lines.split(' ')
        support = bag[-1] #last item is support
        del bag[-1] # delete support
        myset = set(bag)
        
        # the count of all sentences and k-spanned sentences containing sets 
        allCount =0
        kspancount =0
        
        
        # now check sentences for span of the current set
        lengthOfset =len(myset)
        if  lengthOfset > 1 and lengthOfset <= k:
            for onesent in sent:
                onesent = onesent.strip()   
                pattern = re.compile('[\W_]+', re.UNICODE) # remove all charaters other than alpha numeric
                onesent = re.sub(pattern, ' ', onesent)  
                
                list_of_words = onesent.split(' ') # split into word list
                setwords = set(list_of_words)
                
                if myset.issubset(setwords):
                    allCount +=1  #set found in sentence 
                    indices = [list_of_words.index(x) for x in myset]
                    mini = min(indices)
                    maxi = max(indices)
                    if (maxi-mini) <= k:
                        kspancount+=1 # set found in sentence and within k-span
            if float(kspancount)/float(allCount) > 0.4:
                items+=1
                out.write(' '.join(myset)
                          + ' ('
                          + str(support)
                          + ')\n')
    
    out.close()
    myfile.close()
    print ("{} items printed.\n".format(items))
    return outFile
                
                        