def merge_sort(arr):
    """
    merge_sort on array of integers
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)

        i = 0                    # Merge two sorted subarrays in a sorted array
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] =right[j]
                j += 1
            k += 1
        while i < len(left):         # Remaining values
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k]=right[j]
            j += 1
            k += 1

    return arr


def main():
    print('\nMERGE SORT RECURSIVE\t')
    arr = []
    size = int(input("\nEnter size of the array: \t"))
    for i in range(size):
        elements = int(input("Enter the element: \t"))
        arr.append(elements)
    print('\nThe unsorted array: \t', arr)
    merge_sort(arr)
    print('\nThe sorted array: \t', arr)
    print('\n')


if __name__ == "__main__":
    main()
