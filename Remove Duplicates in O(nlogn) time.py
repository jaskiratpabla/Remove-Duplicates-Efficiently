##
##=======================================================
## Jaskirat Pabla
## Remove Duplicates in O(nlogn) time
##=======================================================
##


import check


## Global Constant:
duplicate_replacement = -1


def search_index_of_target(lst_of_nat, target_nat):
    '''
    Returns the index of any instance of target_nat in lst_of_nat.
    
    search_index_of_target: (listof Nat) Nat -> Nat
    Requires: - lst_of_nat must be a list of natural numbers sorted 
                in increasing order.
              - target_nat must appear at least once in lst_of_nat.
    '''
    start = 0
    end = len(lst_of_nat)
    while (start < end):
        mid = (start + end) // 2
        if lst_of_nat[mid] == target_nat:
            return mid
        elif lst_of_nat[mid] > target_nat:
            end = mid
        else:
            start = mid + 1


def remove_duplicates(L):
    '''
    Mutates L so that all elements that appear 
    more than once in L are replaced with -1.
    
    Effects: Mutates L.
    
    remove_duplicates: (listof Nat) -> None
    
    Examples:
    lst = []
    remove_duplicates(lst) => None
    and lst is unchanged.
    
    lst = [0]
    remove_duplicates(lst) => None
    and lst is unchanged.
    
    lst = [6,1,2,3,3,4,5,6,232002]
    remove_duplicates(lst) => None
    and lst is mutated to [-1,1,2,-1,-1,4,5,-1,232002].
    '''
    if (len(L) > 1):
        sort_lst = sorted(L)
        for index in (range(len(L))):
            index_sort_lst = search_index_of_target(sort_lst, L[index])
            if (index_sort_lst == 0):
                if (L[index] == sort_lst[1]):
                    L[index] = duplicate_replacement
            
            elif (index_sort_lst == (len(sort_lst) - 1)):
                if (L[index] == sort_lst[len(sort_lst) - 2]):
                    L[index] = duplicate_replacement
            
            elif (L[index] == sort_lst[index_sort_lst - 1]):
                L[index] = duplicate_replacement
            
            elif (L[index] == sort_lst[index_sort_lst + 1]):
                L[index] = duplicate_replacement


## Examples:
lst = []
check.expect('Empty list', remove_duplicates(lst), None)
check.expect('Empty list - mutation', lst, [])

lst = [0]
check.expect('one element list', remove_duplicates(lst), None)
check.expect('one element list - mutation', lst, [0])

lst = [6, 1, 2, 3, 3, 4, 5, 6, 232002]
check.expect('Typical list', remove_duplicates(lst), None)
check.expect('Typical list - mutation', lst, 
             [-1, 1, 2, -1, -1, 4, 5, -1, 232002])


## Tests:
lst = [0, 0]
check.expect('list of only one pair of dupicates', 
             remove_duplicates(lst), None)
check.expect('list of only one pair of dupicates - mutation', 
             lst, [-1, -1])

lst = [1, 2]
check.expect('list of only one pair of unique numbers', 
             remove_duplicates(lst), None)
check.expect('list of only one pair of unique numbers - mutation', 
             lst, [1, 2])

lst = list(range(25))
check.expect('unique list', remove_duplicates(lst), None)
check.expect('unique list - mutation', lst, list(range(25)))

lst = list(range(100000))
check.expect('Extremely long unique list', remove_duplicates(lst), None)
check.expect('Extremely long unique list - mutation', lst, 
             list(range(100000)))

lst = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
check.expect('list of all duplicates', remove_duplicates(lst), None)
check.expect('list of all duplicates - mutation', lst, 
             [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1])

lst = [5] * 100000
check.expect('Extremely long duplicate list', 
             remove_duplicates(lst), None)
check.expect('Extremely long duplicate list - mutation', 
             lst, [-1] * 100000)

lst = [0, 6, 7, 34, 21, 1, 3, 67, 95, 31, 531, 2021, 2, 10, 0]
check.expect('list of unique numbers with duplicates at the start' +
             ' and end of the list', remove_duplicates(lst), None)
check.expect('list of unique numbers with duplicates at the start' +
             ' and end of the list - mutation', lst, 
             [-1, 6, 7, 34, 21, 1, 3, 67, 95, 31, 531, 2021, 2,
              10, -1])

lst = [100, 26, 63, 37, 99, 82, 44, 82, 37, 44, 26, 63, 82, 99, 10]
check.expect('list of duplicate numbers with uniques at the start' +
             ' and end of the list', remove_duplicates(lst), None)
check.expect('list of duplicate numbers with uniques at the start' +
             ' and end of the list - mutation', lst,
             [100] + [-1] * 13 + [10])

lst = [905, 136, 18, 56, 214, 454, 48, 61, 484, 41, 905, 214, \
       136, 60, 41, 34, 63, 214, 87, 56, 48]
check.expect('Typical list', remove_duplicates(lst), None)
check.expect('Typical list - mutation', 
             lst, [-1, -1, 18, -1, -1, 454, -1, 61, 484, -1, \
                   -1, -1, -1, 60, -1, 34, 63, -1, 87, -1, -1])
