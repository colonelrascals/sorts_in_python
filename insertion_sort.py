# import insertion sort
from pygorithm.sorting import insertion_sort

myList = [12,3,2,14,3,97,2345,6590129,5,125,]


# print time complexities
print(insertion_sort.time_complexities())

def sort(List):
    for i in range(1, len(List)):
        currentNumber = List[i]
        for j in range(i - 1, -1, -1):
            if List[j] > currentNumber:
                List[j], List[j + 1] = List[j + 1], List[j]
            else:
                List[j + 1] = currentNumber
                break
    return List
    
print(sort(myList))
