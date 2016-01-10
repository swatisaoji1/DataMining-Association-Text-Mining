import csv
import operator


def apriori(filepaths, out_file_path, min_support=5, verbose=False):
    """Implements the Apriori algorithm.

    The Apriori algorithm will iteratively generate new candidate 
    k-itemsets using the frequent (k-1)-itemsets found in the previous 
    iteration.

    Parameters
    ----------
    dataset : list
        The dataset (a list of transactions) from which to generate 
        candidate itemsets.

    min_support : float
        The minimum support threshold. Defaults to 0.5.
    
    out_file_path: string
        The path to the folder where output results will be stored
        
    Returns
    -------
    String: path of the file where output is stored. 

    References
    ----------
    .. [1] R. Agrawal, R. Srikant, "Fast Algorithms for Mining Association 
           Rules", 1994.

    """
    dataset, idList = makeDataset(filepaths)
    C1 = create_candidates(dataset) # c1 is frozenset
    D = map(set, dataset) # D is a list of mutable set created from the datset
    F1, support_data = support_prune(D, idList, C1, min_support, verbose=False) # prune candidate 1-itemsets
    F = [F1] # list of frequent itemsets; initialized to frequent 1-itemsets
    k = 2 # the itemset cardinality
    while (len(F[k - 2]) > 0):
        print ("apriori ->"+ str(len(F[k - 2]))+ " " + str(k) + " item sets meet min-support...")
        Ck = apriori_gen(F[k-2], k) # generate candidate itemsets
        Fk, supK = support_prune(D, idList, Ck, min_support) # prune candidate itemsets
        support_data.update(supK) # update the support counts to reflect pruning
        F.append(Fk) # add the pruned candidate itemsets to the list of frequent itemsets
        k += 1

    if verbose:
        # Print a list of all the frequent itemsets.
        for kset in F:
            for item in kset:
                print("" \
                    + "{" \
                    + "".join(str(i) + ", " for i in iter(item)).rstrip(', ') \
                    + "}" \
                    + ":  sup = " + str(round(support_data[item], 3)))
    filewritten = writeResults(support_data, out_file_path)
    return filewritten

def writeResults(sup_data, out_file):
    
    
    # sort the output 
    sorted_support = sorted(sup_data.items(), key=operator.itemgetter(1), reverse=True)
    sup_data = dict(sorted_support)
    # out_file = raw_input('Enter path for output: ')
    open_file = open(out_file+"\\output.csv" , 'w')
   
    for x in sorted_support:
        items = x[0]
        support = x[1]
        open_file.write(" ".join(items))
        open_file.write(" ({0})\n".format(support))
       
    open_file.close()
    return (out_file+"\\output.csv")
    

def makeDataset(filepaths):
    
    myidlist = []
    myDataList = []
    
    f = open(filepaths)
    for line in f:
        
        line = line.strip().rstrip(',').lstrip(',') 
        record = line.split(',')
        myid = record[0]
        del record[0]
        myidlist.append(myid)
        myDataList.append(record)

    return myDataList, myidlist
    
def create_candidates(dataset, verbose=False):
    """Creates a list of candidate 1-itemsets from a list of transactions.

    Parameters
    ----------
    dataset : list
        The dataset (a list of transactions) from which to generate candidate 
        itemsets.

    Returns
    -------
    The list of candidate itemsets (c1) passed as a frozenset (a set that is 
    immutable and hashable).
    """
    c1 = [] # list of all items in the database of transactions
    for transaction in dataset:
        for item in transaction:
            if not [item] in c1:
                c1.append([item])
    c1.sort()

    if verbose:
        # Print a list of all the candidate items.
        print("" \
            + "{" \
            + "".join(str(i[0]) + ", " for i in iter(c1)).rstrip(', ') \
            + "}")

    # Map c1 to a frozenset because it will be the key of a dictionary.
    return map(frozenset, c1)

def support_prune(dataset, idList, candidates, min_support, verbose=False):
    """Returns all candidate itemsets that meet a minimum support threshold.

    By the apriori principle, if an itemset is frequent, then all of its 
    subsets must also be frequent. As a result, we can perform support-based 
    pruning to systematically control the exponential growth of candidate 
    itemsets. Thus, itemsets that do not meet the minimum support level are 
    pruned from the input list of itemsets (dataset).

    Parameters
    ----------
    dataset : list
        The dataset (a list of transactions) from which to generate candidate 
        itemsets.

    candidates : frozenset
        The list of candidate itemsets.

    min_support : float
        The minimum support threshold.

    Returns
    -------
    retlist : list
        The list of frequent itemsets.

    support_data : dict
        The support data for all candidate itemsets.
    """
    
    sscnt = {}
    for can in candidates:
        found = -1
        index = -1
        for tid in dataset:
            index +=1
            currentIndex = int(idList[index])
            if can.issubset(tid):
                if currentIndex != found: # avoids repeat counting of support from same record
                    sscnt.setdefault(can, 0)
                    sscnt[can] += 1
                    found = currentIndex
            
    

   
    retlist = [] # array for unpruned itemsets
    support_data = {} # set/dict for support data for corresponding itemsets
    for key in sscnt:
        support = sscnt[key] # code changes to count absolute instead of percentage
        if support >= min_support:
            retlist.insert(0, key) # inserts in the beginning
            support_data[key] = support

    # Print a list of the pruned itemsets.
    if verbose:
        for kset in retlist:
            for item in kset:
                print("{" + str(item) + "}")
        print("")
        for key in support_data:
            print("" \
                + "{" \
                + "".join([str(i) + ", " for i in iter(key)]).rstrip(', ') \
                + "}" \
                + ":  sup = " + str(support_data[key]))

    return retlist, support_data

def apriori_gen(freq_sets, k):
    """Generates candidate itemsets (via the F_k-1 x F_k-1 method).

    This operation generates new candidate k-itemsets based on the frequent 
    (k-1)-itemsets found in the previous iteration. The candidate generation 
    procedure merges a pair of frequent (k-1)-itemsets only if their first k-2 
    items are identical.

    Parameters
    ----------
    freq_sets : list
        The list of frequent (k-1)-itemsets.

    k : integer
        The cardinality of the current itemsets being evaluated.

    Returns
    -------
    retlist : list
        The list of merged frequent itemsets.
    """
    retList = [] # list of merged frequent itemsets
    lenLk = len(freq_sets) # number of frequent itemsets
    for i in range(lenLk):
        for j in range(i+1, lenLk):
            a=list(freq_sets[i])
            b=list(freq_sets[j])
            a.sort()
            b.sort()
            F1 = a[:k-2] # first k-2 items of freq_sets[i]
            F2 = b[:k-2] # first k-2 items of freq_sets[j]

            if F1 == F2: # if the first k-2 items are identical
                # Merge the frequent itemsets.
                retList.append(freq_sets[i] | freq_sets[j])

    return retList



        
