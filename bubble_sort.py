# import the required sort
from pygorithm.sorting import bubble_sort

myList = [12, 4, 2, 14, 3, 7, 5]

# for printing time complexities of bubble_sort
print(bubble_sort.time_complexities())

#Here it is written out
def sort(List):
    for i in range(len(List)):
        for j in range(len(List)) -1, i, -1):
        if List[j] < List[j-1]:
            List[j], List[j-1] = List[j-1],List[j]
            return List

print(sort(myList))
