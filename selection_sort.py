# import selection sort
from pygorithm.sorting import selection_sort

myList = [12,3,2,14,3,97,2345,6590129,5,125,]


# print time complexities
print(selection_sort.time_complexities())

def sort(List):
    for i in range(len(List) - 1):
        minimum = i
        for j in range(i + 1, len(List)):
            if(List[j] < List[minimum]):
                minimum = j
            if(minimum != i):
                List[i], List[minimum] = List[minimum], List[i]
        return List

print(sort(myList))
