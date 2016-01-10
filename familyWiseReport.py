'''
Created on Mar 9, 2015

@author: Swati
'''
import os
def familyReport(filename, k , mydir):
  # bag of family members:
    family = ["mother" , "brother", "grandfather",
               "sister", "grandmother", "father",
               "mom", "dad", "son", "daughter",
               "uncle", "aunt", "niece", "nephew", 
               "cousin"]
   
    
    pathout = mydir + "\\FamilyRep"+ str(k)
    if not os.path.exists(pathout):
        os.makedirs(pathout)
        
    # Read input file
    myfile = open(filename, 'r')
        
    # make output files for each family member:
    motherf = open(pathout+"\\mother.txt", 'w')
    fatherf = open(pathout+"\\father.txt", 'w')
    brotherf = open(pathout+"\\brother.txt", 'w')
    grandfatf = open(pathout+"\\grandfather.txt", 'w')
    grandmotf = open(pathout+"\\grandmother.txt", 'w')
    sisterf = open(pathout+"\\sister.txt", 'w')
    sonf = open(pathout+"\\son.txt", 'w')
    daughterf = open(pathout+"\\daughter.txt", 'w')
    others = open(pathout+"\\others.txt", 'w')
    femalef = open(pathout+"\\Females.txt", 'w')
    malef = open(pathout+"\\Males.txt", 'w')
    
    motherList = ["mother", "mothers", "mom"]
    fatherList =["father", "dad", "fathers"]
    brotherList =["brothers", "brother"]
    sisterList =["sisters", "sister"]
    grandmotherList=["grandmother" ,"grandmothers"]
    grandfatherList=["grandfather", "grandfathers"]
    daughterList =["daughters", "daughter"]
    sonList =["sons", "son"]
    
    
    count =0
    for lines in myfile:
        count += 1
        # remove parenthesis and trailing and leading space if any
        lines = lines.replace('(','').replace(')','').strip() 
        bag = lines.split(' ')
        frequency = bag[-1] #last item is frequency
        del bag[-1] # delete support
        
        familyitems =[]
        for item in bag:
            if item in family:
                familyitems.append(item)
        if len(familyitems) > 0:
            for eachone in familyitems:
                
                if eachone in motherList:
                    motherf.write(' '.join(bag)
                                    + ' '
                                    + str(frequency)
                                    +'\n')
                    femalef.write(' '.join(bag)
                                    + ' '
                                    + str(frequency)
                                    +'\n')
                elif eachone in fatherList:
                    fatherf.write(' '.join(bag)
                                    + ' '
                                    + str(frequency)
                                    +'\n')
                    malef.write(' '.join(bag)
                                    + ' '
                                    + str(frequency)
                                    +'\n')
                elif eachone in brotherList:
                    brotherf.write(' '.join(bag)
                                    + ' '
                                    + str(frequency)
                                    +'\n')
                    malef.write(' '.join(bag)
                                    + ' '
                                    + str(frequency)
                                    +'\n')
                elif eachone in sisterList:
                    sisterf.write(' '.join(bag)
                                    + ' '
                                    + str(frequency)
                                    +'\n')
                    femalef.write(' '.join(bag)
                                    + ' '
                                    + str(frequency)
                                    +'\n')
                elif eachone in grandmotherList:
                    grandmotf.write(' '.join(bag)
                                    + ' '
                                    + str(frequency)
                                    +'\n')
                    femalef.write(' '.join(bag)
                                    + ' '
                                    + str(frequency)
                                    +'\n')
                elif eachone in grandfatherList:
                    grandfatf.write(' '.join(bag)
                                    + ' '
                                    + str(frequency)
                                    +'\n')
                    malef.write(' '.join(bag)
                                    + ' '
                                    + str(frequency)
                                    +'\n')
                elif eachone is sonList:
                    sonf.write(' '.join(bag)
                                    + ' '
                                    + str(frequency)
                                    +'\n')
                elif eachone in daughterList :
                    daughterf.write(' '.join(bag)
                                    + ' '
                                    + str(frequency)
                                    +'\n')
                else :
                    others.write(' '.join(bag)
                                    + ' '
                                    + str(frequency)
                                    +'\n')
    
    print ("reports are stores for {} spanned associations in dir: {}".format(k, pathout))
        
    
    
    
        
        
       
    
    