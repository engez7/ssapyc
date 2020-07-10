def quick_sort(arr):
    """
    quick_sort on array of integers
    """
    def partition(arr, p, r):
        pivot = arr[r]
        i = p-1
        for j in range(p, r):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[r] = arr[r], arr[i+1]
        return i+1

    def quick_sort_rec(arr, p, r):
        if p < r:
            q = partition(arr, p, r)
            quick_sort_rec(arr, p, q-1)
            quick_sort_rec(arr, q+1, r)

    n = len(arr)
    quick_sort_rec(arr, 0, n-1)
    return arr


def main():
    print('\nQUICK SORT \t')
    arr = []
    size = int(input("\nEnter size of the array: \t"))
    for i in range(size):
        elements = int(input("Enter the element: \t"))
        arr.append(elements)
    print('\nThe unsorted array: \t', arr)
    quick_sort(arr)
    print('\nThe sorted array: \t', arr)
    print('\n')


if __name__ == "__main__":
    main()
