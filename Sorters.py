import time
import random


def bubble(numbers):
    """
    Bubble sort compares each adjacent value in the list and swaps them if the second one is smaller
    Best case: O(n)
    Average case: O(n^2)
    Worst case: O(n^2)
    """
    startTime = time.time()
    for i in range(len(numbers)-1):
        for j in range(len(numbers)-1-i):
            if numbers[j] > numbers[j+1]:
                temp = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = temp
    endTime = time.time()
    totalTime = endTime - startTime
    return numbers, totalTime


def insertion(numbers):
    """
    Insertion sort places each value in the list one at a time sorting them
    Best case: O(n)
    Average case: O(n^2)
    Worst case: O(n^2)
    """
    startTime = time.time()
    for i in range(len(numbers)):
        currentValue = numbers[i]
        currentPosition = i
        while currentPosition > 0 and numbers[currentPosition-1] > currentValue:
            temp = numbers[currentPosition]
            numbers[currentPosition] = numbers[currentPosition-1]
            numbers[currentPosition-1] = temp
            currentPosition -= 1
    endTime = time.time()
    totalTime = endTime - startTime
    return numbers, totalTime


def selection(numbers):
    """
    Selection sort continuously finds the minimum value from the list and places it at the beginning
    Best case: O(n^2)
    Average case: O(n^2)
    Worst case: O(n^2)
    """
    startTime = time.time()
    for i in range(len(numbers)):
        minimumIndex = i
        for j in range(i, len(numbers)):
            if numbers[minimumIndex] > numbers[j]:
                temp = numbers[minimumIndex]
                numbers[minimumIndex] = numbers[j]
                numbers[j] = temp
    endTime = time.time()
    totalTime = endTime - startTime
    return numbers, totalTime


def merge(numbers):
    """
    Merge sort repeatedly splits the list until there are n lists then they ar merged back together
    Best case: O(nlogn)
    Average case: O(nlogn)
    Worst case: O(nlogn)
    """
    startTime = time.time()

    def _merge(_numbers):
        if len(_numbers) < 2:
            return _numbers
        result = []
        mid = round(len(_numbers) / 2)
        y, z = _merge(_numbers[:mid]), _merge(_numbers[mid:])
        while (len(y) > 0) and (len(z) > 0):
            if y[0] > z[0]:
                result.append(z[0])
                z.pop(0)
            else:
                result.append(y[0])
                y.pop(0)
        result += y
        result += z
        return result
    numbers = _merge(numbers)
    endTime = time.time()
    totalTime = endTime - startTime
    return numbers, totalTime


def quick(numbers):
    """
    Quick sort repeatedly picks an anchor moving all the smaller values to the left and the larger values to the right
    Best case: O(nlogn)
    Average case: O(nlogn)
    Worst case: O(n^2)
    """
    startTime = time.time()

    def quicksort(array):
        less = []
        equal = []
        greater = []
        if len(array) > 1:
            temp = array
            temp.sort()
            pivot = int(len(temp)/2)
            for x in array:
                if x < array[pivot]:
                    less.append(x)
                elif x == array[pivot]:
                    equal.append(x)
                elif x > array[pivot]:
                    greater.append(x)
            return quicksort(less)+equal+quicksort(greater)
        else:
            return array
    numbers = quicksort(numbers)
    endTime = time.time()
    totalTime = endTime - startTime
    return numbers, totalTime


def bogo(numbers):
    """
    Bogo sort randomly sorts the list and checks if the list is sorted
    Best case: O(n)
    Average case: O((n+1)!)
    Worst case: O(infinite)
    """
    startTime = time.time()
    sort = False
    temp = None
    while not sort:
        temp = [None] * len(numbers)
        for i in range(len(numbers)):
            randomIndex = random.randint(0, len(numbers)-1)
            while temp[randomIndex] is not None:
                randomIndex = random.randint(0, len(numbers)-1)
            temp[randomIndex] = numbers[i]
        isSorted = all([temp[index] <= temp[index+1] for index in range(len(temp)-1)])
        if isSorted:
            sort = True
    endTime = time.time()
    totalTime = endTime - startTime
    return temp, totalTime


def gnome(numbers):
    """
    Gnome sort compares the current item with the next. If they are swapped then it steps back one index and repeats
    Best case: O(n)
    Average case: O(n^2)
    Worst case: O(n^2)
    """
    startTime = time.time()
    searchIndex = 0
    while searchIndex < len(numbers):
        if searchIndex == 0:
            searchIndex += 1
        if numbers[searchIndex] >= numbers[searchIndex-1]:
            searchIndex += 1
        else:
            temp = numbers[searchIndex]
            numbers[searchIndex] = numbers[searchIndex-1]
            numbers[searchIndex-1] = temp
            searchIndex -= 1
    endTime = time.time()
    totalTime = endTime - startTime
    return numbers, totalTime
