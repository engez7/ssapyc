from insertionsort import insertion_sort
from selectionsort import selection_sort
from bubblesort import bubble_sort
from mergesortrec import merge_sort
from quicksortrec import quick_sort
from heapsort import heap_sort

import random
from time import time

print("\nCOMPARISON BETWEEN SOME SORTING ALGHORITMS\n")
print("The unsorted array of integers will be randomly generate")
print("You can choose array's size")
print("***PAY ATTENTION!! Huge sizes overheat your CPU!!***")

size = int(input("\nEnter size of the list: \t"))
unsarr = [random.randrange(-9999, 9999, 1) for i in range(size)]
print("\nThe unsorted array: \t", unsarr)

print('\nINSERTION')
arr = unsarr[:]
t0 = time()
insertion_sort(arr)
t1 = time()
tins = t1 - t0
print('\nThe sorted array: \t', arr)
print('\n')

print('SELECTION')
arr = unsarr[:]
t2 = time()
arr = selection_sort(arr)
t3 = time()
tsel = t3 - t2
print('\nThe sorted array: \t', arr)
print('\n')

print('BUBBLE')
arr = unsarr[:]
t4 = time()
arr = bubble_sort(arr)
t5 = time()
tbub = t5 - t4
print('\nThe sorted array: \t', arr)
print('\n')

print('MERGE REC')
arr = unsarr[:]
t6 = time()
arr = merge_sort(arr)
t7 = time()
tmer = t7 - t6
print('\nThe sorted array: \t', arr)
print('\n')

print('QUICK REC')
arr = unsarr[:]
t8 = time()
arr = quick_sort(arr)
t9 = time()
tqui = t9 - t8
print('\nThe sorted array: \t', arr)
print('\n')

print('HEAP')
arr = unsarr[:]
t10 = time()
arr = heap_sort(arr)
t11 = time()
thea = t11 - t10
print('\nThe sorted array: \t', arr)
print('\n')

print('PY3 BUILTIN')
arr = unsarr[:]
t12 = time()
arr.sort()
t13 = time()
tpy3 = t13 - t12
print('\nThe sorted array: \t', arr)
print('\n')

print('*****************************************************')
print(f'Sorting an array of {size} elements - Results [sec]:')
print('INSERTION:\t', tins)
print('SELECTION:\t', tsel)
print('BUBBLE:\t\t', tbub)
print('MERGE REC:\t', tmer)
print('QUICK REC:\t', tqui)
print('HEAP:\t\t', thea)
print('PY3 BUILTIN:\t', tpy3)
print('*****************************************************')
