from TopWordLists import getTopLists
from MakeFileName import makeFileName
from MakeSentencesWithId import extractSent
from MakeBag import makeBagOfWords
from Apriori import apriori
import os
from CheckSpan import checkSpan
from OrderCheck import checkOrder
from familyWiseReport import familyReport


def main():
    
    """
    Step 0:
    makeFileName() will take the directory where medical records are stored and ...
    returns path to text file that stores file paths to Medical records.
    
    """
    filenames = makeFileName()
    
    print "\n\nstep 0 done... 6 more to go "
    print "From the directory of data files : a file containing their path is generated."
    print "=========================================================================\n\n"
    
    """
    Step 1:
    extractSent(filename) will take the text file containing file paths to Medical records..
    writes 3 files and returns their paths :
    -- file1 = Candidate sentences (stop words included)
    -- file2 = Candidate sentences (stop words removed and Record Id added)
    -- file3 = Run record file -that writes summary of the run
    """   

    fullSentFile, sentFile, runFile = extractSent(filenames)
    print "step 1 done... 5 more to go "
    print " This step writes three files: "
    print "1) candidate sentences (full i.e including stop words)"
    print "2) candidate sentences (no stop words and contains Id -indicating medical record)"
    print "3) Run file that summarizes the run process"
    print "================================================================================\n\n"
    """
    Step 2:
    makeBagOfWords() takes the sentence file with ids and makes bag of words file 
    This is a csv file.
    Returns the path to the file.
    """
    bagFile = makeBagOfWords(sentFile)
    print "step 2 done... 4 more to go "
    print "This step creates bag of words-csv file for Apriori alg."
    print "=================================================================================\n\n"
    
    """
    Step 3:
    apriori - takes the bag of the word calculates the sets that satisfy the support .
    apriori(dataset, idList, min_support=5, verbose=True)
    Returns : file path as string
    """
 
    mydirectory = os.path.dirname(bagFile) # get the directory of bagFile
    apOut = apriori(bagFile, mydirectory, min_support=5, verbose=False)
    print apOut
    print "step 3 done... 3 more to go "
    print "This step takes bag of words with ids and runs apriori algorithm."
    print "All association sets that satisfy support> 5 are generated ."
    print "ID's are used to count the support at the Report level"
    print "=================================================================================\n\n"
    
    """
    Step 4:
    checkspan():
    
    """
    filespan3 = checkSpan(fullSentFile, apOut, mydirectory, 3 )
    print "3-span satisfying sets stored in "+ filespan3
    filespan5 = checkSpan(fullSentFile, apOut, mydirectory, 5 )
    print "5-span satisfying sets stored in "+ filespan5
    filespan10 = checkSpan(fullSentFile, apOut, mydirectory, 10 )
    print "10-span satisfying sets stored in "+ filespan10
    
    print "step 4 done... 2 more to go "
    print "Checks if association words lie in k span. "
    print "K values 3, 5 and 10 are checked - generates 3 files"
    print "=================================================================================\n\n"
    
    """
    Step 5:
    OrderCheck():
    
    """
    freq_3 = checkOrder(fullSentFile, filespan3, mydirectory, 3)
    freq_5 = checkOrder(fullSentFile, filespan5, mydirectory, 5)
    freq_10 = checkOrder(fullSentFile, filespan10, mydirectory, 10)
    
    print "step 5 done... 1 more to go "
    print " The association sets permutations for e.g. {mother, diabetes} and {diabetes, mother} are checked for frequency in candidate sentences"
    print " Two files for each run : "
    print "1) one with all permutations"
    print "2) ordered Wordlists "
    print "for each span (3,5,10) are generated."
    print "=================================================================================\n\n"
    
    
    
    getTopLists(freq_3, 3, mydirectory)
    getTopLists(freq_5, 5, mydirectory)
    getTopLists(freq_10, 10, mydirectory)
    
   
    print "Step 6 part 1 done : "
    print "5 files are generated , each answering the respective questions: "
    print " a.txt : contain at least one family member?"
    print " b.txt : contain at least one of the diseases? (disease file in package)"
    print " c.txt : one family member but no disease? "
    print " d.txt : both a family member and a disease? "
    print " e.txt : neither a family nor a disease?"
    
    print "check out Put files in : " + mydirectory 
    print "=================================================================================\n\n"
    
      
    familyReport(freq_3, 3, mydirectory)
    familyReport(freq_5, 5, mydirectory)
    familyReport(freq_10, 10, mydirectory)
    
    print "Step 6 part 2 done : PROCESS COMPLETE !! "
    print "=================================================================================\n\n"
    
   
    
if __name__ == "__main__":
    main()