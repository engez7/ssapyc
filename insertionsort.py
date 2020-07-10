def insertion_sort(arr):
    """
    insertion_sort on array of integers
    """
    for i in range(1, len(arr)):
        j = i
        while (j > 0) and (arr[j - 1] > arr[j]):
            tmp = arr[j]
            arr[j] = arr[j - 1]
            arr[j - 1] = tmp
            j -= 1
    return arr

def main():
    print('\nINSERTION SORT \t')
    arr = []
    size = int(input("\nEnter size of the array: \t"))
    for i in range(size):
        elements = int(input("Enter the element {}: \t".format(i+1)))
        arr.append(elements)
    print('\nThe unsorted list: \t', arr)
    insertion_sort(arr)
    print('\nThe sorted array: \t', arr)


if __name__ == "__main__":
    main()
