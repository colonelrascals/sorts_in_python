from pygorithm.sorting import counting_sort

myList = [12,3,2,14,3,97,2345,6590129,5,125,]

print(counting_sort.time_complexities())


def sort(List):
    try:
        maxValue = 0
        for i in range(len(myList)):
            if myList[i] > maxValue:
                maxValue = myList[i]

        buckets = [0] * (maxValue + 1)

        for i in myList:
            buckets[i] += 1

        i = 0
        for j in range(maxValue + 1):
            for a in range(buckets[j]):
                myList[i] = j
                i += 1

        return myList

    except TypeError: # didn't know this was a thing
        print('Counting sort only works on ints')

print(sort(myList))
