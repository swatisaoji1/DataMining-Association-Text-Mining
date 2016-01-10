'''
Created on Mar 7, 2015

@author: Swati
'''
import os
def getTopLists(filename, k , mydir):
    
    pathout = mydir + "\\Ans_freqSpan_"+ str(k)
    if not os.path.exists(pathout):
        os.makedirs(pathout)
        
    # Read input file
    myfile = open(filename, 'r')
    
    
    # open files to write
    
    a = open(pathout+"\\a.txt", 'w') # contain at least one family member?
    b = open(pathout+"\\b.txt", 'w') # contain at least one of the following diseases?
    c = open(pathout+"\\c.txt", 'w') # one family member but no disease?
    d = open(pathout+"\\d.txt", 'w') # both a family member and a disease?
    e = open(pathout+"\\e.txt", 'w') # neither a family nor a disease?
    answers = open(pathout+"\\answers.txt", 'w')
    
    
    # bag of family members:
    family = ["mother" , "brother", "grandfather",
               "sister", "grandmother", "father",
               "mom", "dad", "son", "daughter",
               "uncle", "aunt", "niece", "nephew", 
               "cousin"]
    
    
    
    #bag of diseases
    diseasefile = open("DiseasesList.txt" , 'r')
    diseaseBag = []
    for everyDisease in diseasefile:
        everyDisease = everyDisease.strip().lower()
        diseaseBag.append(everyDisease)
    
    
    
      
    #variables to count
    count = 0 
    aCount = 0
    bCount = 0
    cCount = 0
    dCount = 0
    eCount = 0
    
    for lines in myfile:
        count += 1
        # remove parenthesis and trailing and leading space if any
        lines = lines.replace('(','').replace(')','').strip() 
        bag = lines.split(' ')
        frequency = bag[-1] #last item is frequency
        del bag[-1] # delete support
        
     
        # check if in family and in disease
        isfamily = any(item in bag for item in family)
        isdisease = any(item in bag for item in diseaseBag)
        
       
        
        if isfamily:
            aCount += 1
            a.write(' '.join(bag)
                    + ' '
                    + str(frequency)
                    +'\n')
            
        if isdisease:
            bCount += 1
            b.write(' '.join(bag)
                    + ' '
                    + str(frequency)
                    +'\n')
        if isfamily and not isdisease:
            cCount += 1
            c.write(' '.join(bag)
                    + ' '
                    + str(frequency)
                    +'\n')
        if isfamily and isdisease:
            dCount += 1
            d.write(' '.join(bag)
                    + ' '
                    + str(frequency)
                    +'\n')
        if not isfamily and not isdisease:
            eCount += 1
            e.write(' '.join(bag)
                    + ' '
                    + str(frequency)
                    +'\n')
        
        if count == 100:
            answers.write("In first 100 word list: \n")
            answers.write("There are {} associations with at least one family member.\n".format(aCount))
            answers.write("There are {} associations with at least one Disease.\n".format(bCount))
            answers.write("There are {} associations with at least one family member and NO disease.\n".format(cCount))
            answers.write("There are {} associations both family member and disease.\n".format(dCount))
            answers.write("There are {} associations with neither family nor disease.\n".format(eCount))
            answers.write("====================================================================\n\n")
            
        if count == 200:
            answers.write("In first 200 word list: \n")
            answers.write("There are {} associations with at least one family member.\n".format(aCount))
            answers.write("There are {} associations with at least one Disease.\n".format(bCount))
            answers.write("There are {} associations with at least one family member and NO disease.\n".format(cCount))
            answers.write("There are {} associations both family member and disease.\n".format(dCount))
            answers.write("There are {} associations with neither family nor disease.\n".format(eCount))
            answers.write("====================================================================\n\n")
            
        if count == 500:
            answers.write("In first 500 word list: \n")
            answers.write("There are {} associations with at least one family member.\n".format(aCount))
            answers.write("There are {} associations with at least one Disease.\n".format(bCount))
            answers.write("There are {} associations with at least one family member and NO disease.\n".format(cCount))
            answers.write("There are {} associations both family member and disease.\n".format(dCount))
            answers.write("There are {} associations with neither family nor disease.\n".format(eCount))
            answers.write("====================================================================\n\n")
            
        if count == 1000:
            answers.write("In first 1000 word list: \n")
            answers.write("There are {} associations with at least one family member.\n".format(aCount))
            answers.write("There are {} associations with at least one Disease.\n".format(bCount))
            answers.write("There are {} associations with at least one family member and NO disease.\n".format(cCount))
            answers.write("There are {} associations both family member and disease.\n".format(dCount))
            answers.write("There are {} associations with neither family nor disease.\n".format(eCount))
            answers.write("====================================================================\n\n")
    
    answers.write("The total associations studied in {} spanned sets are {} : The pattern :\n.".format(k,count))
    answers.write("There are {} associations with at least one family member.\n".format(aCount))
    answers.write("There are {} associations with at least one Disease.\n".format(bCount))
    answers.write("There are {} associations with at least one family member and NO disease.\n".format(cCount))
    answers.write("There are {} associations both family member and disease.\n".format(dCount))
    answers.write("There are {} associations with neither family nor disease.\n".format(eCount))
    answers.write("====================================================================\n\n")
    print ("done")   
                    
        
            
        
    