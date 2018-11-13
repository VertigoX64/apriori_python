# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 16:15:50 2018

@author: PyroX64
"""

from collections import Counter

'''
# i write apriori by way of
# defining a couple of functions
# each of which carry out a phase of the FIM thing.
'''
# dataset = [[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5]]
# Transactions:
# [ 
#  [1,3,4],
#  [2,3,5]
#  [1,2,3,5],
#  [2,5] 
# ]
dataset = [[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5]]
support = 2
# counting distinct items 
def distinct_items(transactions):
    count = Counter()
    for t in transactions:
            count.update(t)
    return count

def frequent_single_itemsets(): # make into frozenset
    distinct = distinct_items(dataset)
    return set(frozenset([i]) for i in distinct)

def generate_candidates(L, k):
    """Generate candidate set from `L` with size `k`"""
    candidates = set()
    for a in L:
        for b in L:
            u = a.union(b)
            if len(u) == k and a != b:
                candidates.add(u)
    return candidates

def itemsets_support_NoPrune(transactions, itemsets):
    """Get support for `itemsets`"""

    support_set = Counter()
    aux = []
    for trans in transactions:
        subsets = [itemset for itemset in itemsets if len(itemset) <= len(trans) and itemset.issubset(set(trans)) ]
        support_set.update(subsets)

    return support_set

def itemsets_support_Prune(transactions, itemsets):
    """Get support for `itemsets`"""

    support_set = Counter()
    aux = []
    for trans in transactions:
        subsets = [itemset for itemset in itemsets if len(itemset) <= len(trans) and itemset.issubset(set(trans)) ]
        support_set.update(subsets)
    for i in support_set:
        if support_set[i] < support:
            aux.append(i)
    for i in aux:
        support_set.pop(i)

    return support_set


        
