def bubble_sort(arr):
    """
    bubble_sort on array of integers
    """
    for sorted in range(0, len(arr)):
        for j in range(1, len(arr) - sorted):
            if arr[j - 1] > arr[j]:
                tmp = arr[j - 1]
                arr[j - 1] = arr[j]
                arr[j] = tmp
    return arr

def main():
    print('\nBUBBLE SORT \t')
    arr = []
    size = int(input("\nEnter size of the array: \t"))
    for i in range(size):
        elements = int(input("Enter the element: \t"))
        arr.append(elements)
    print('\nThe unsorted array: \t', arr)
    bubble_sort(arr)
    print('\nThe sorted array: \t', arr)
    print('\n')


if __name__ == "__main__":
    main()
