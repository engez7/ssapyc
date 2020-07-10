
# Python program for implementation of heap Sort

def heap_sort(arr):
    """
    heap_sort on array of integers
    """

    def heapify(arr, n, i):    # To heapify subtree rooted at index i. n is size of heap
        largest = i  # Initialize largest as root
        l = 2 * i + 1     # left = 2*i + 1
        r = 2 * i + 2     # right = 2*i + 2

        if l < n and arr[i] < arr[l]:   # See if left child of root exists and is greater than root
            largest = l
        if r < n and arr[largest] < arr[r]:    # See if right child of root exists and is greater than root
            largest = r
        if largest != i:      # Change root, if needed
            arr[i],arr[largest] = arr[largest],arr[i]

            heapify(arr, n, largest)   # Heapify the root

    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):   # Build a maxheap. Since last parent will be at ((n//2)-1) we can start at that location.
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):   # One by one extract elements
        arr[i], arr[0] = arr[0], arr[i]   # swap
        heapify(arr, i, 0)

    return arr

def main():
    print('\nHEAP SORT\t')
    arr = []
    size = int(input("\nEnter size of the array: \t"))
    for i in range(size):
        elements = int(input("Enter the element: \t"))
        arr.append(elements)
    print('\nThe unsorted array: \t', arr)
    heap_sort(arr)
    print('\nThe sorted array: \t', arr)
    print('\n')


if __name__ == "__main__":
    main()
