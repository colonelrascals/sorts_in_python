# import heap sort
from pygorithm.sorting import heap_sort

myList = [12,3,2,14,3,97,2345,6590129,5,125,]
# sort the list

sorted_list = heap_sort.sort(myList)

# I sees it
print(sorted_list)

# print time complexities of heap sort
print(heap_sort.time_complexities())

def heapify(alist):
    #This function helps to maintain the heap property
    # start = (len(alist) - 2) // 2         (faster execution)
    start = len(alist) // 2
    while start >= 0:
        shiftDown(alist, start, len(alist) - 1)
        start -= 1

def shiftDown(alist, start, end):
    root = start
    while root * 2 + 1 <= end:
        child = root * 2 + 1
        # right child exists and is greater than left child
        if child + 1 <= end and alist[child] < alist[child + 1]:
            child += 1
        # if child is greater than root(parent), then swap their positions
        if child <= end and alist[root] < alist[child]:
            alist[root], alist[child] = alist[child], alist[root]
            root = child
        else:
            return

# heap in python
def sort(alist):
    heapify(alist) # creates heap
    end = len(alist) - 1
    while end > 0:
        alist[end], alist[0] = alist[0], alist[end]
        shiftDown(alist, 0, end - 1)
        end -= 1
    return alist

print(sort(myList))
