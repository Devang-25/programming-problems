def bubble_sort(a_list):
    while sorted(a_list) != a_list:
        for x in xrange(len(a_list)-1):
            if a_list[x] > a_list[x+1]:
                temp = a_list[x]
                a_list[x] = a_list[x+1]
                a_list[x+1] = temp
    return a_list
"""
def bubble_sort(a_list):
    checker = True
    while checker:
        checker = False
        for x in xrange(len(a_list)-1):
            if a_list[x] > a_list[x+1]:
                temp = a_list[x]
                a_list[x] = a_list[x+1]
                a_list[x+1] = temp
                checker = True
    return a_list
    
   # More understable code I guess  
"""
