def selection_sort(arr):
    """
    selection_sort on array of integers
    """
    for i_first_unsorted in range(0, len(arr)):
        i_min = i_first_unsorted
        for j in range(i_first_unsorted+1,len(arr)):
            if arr[j] < arr[i_min]:
                i_min = j
        arr[i_first_unsorted], arr[i_min] = arr[i_min], arr[i_first_unsorted]
    return arr

def main():
    print('\nSELECTION SORT \t')
    arr = []
    size = int(input("\nEnter size of the array: "))
    for i in range(size):
        elements = int(input("Enter the element {}: \t".format(i+1)))
        arr.append(elements)
    print('\nThe unsorted array: \t', arr)
    selection_sort(arr)
    print('\nThe sorted array: \t', arr)
    print('\n')


if __name__ == "__main__":
    main()
