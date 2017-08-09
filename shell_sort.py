# import shell sort
from pygorithm.sorting import shell_sort

myList = [12,3,2,14,3,97,2345,6590129,5,125,]


# print time complexities
print(shell_sort.time_complexities())

def sort(List):
    gap = len(List) // 2
    while gap > 0:
        for i in range(gap, len(List)):
            currentItem = List[i]
            j = i
            while j >= gap and List[j - gap] > currentItem:
                List[j] = List[j - gap]
                j -= gap
                List[j] = currentItem
        gap //= 2
    return List
print(sort(myList))
