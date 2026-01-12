# Linear sort (ascending order) with mistakes

def linear_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i, n-1):  # mistake: should be range(i+1, n)
            if arr[i] > arr[j]:  # mistake: comparison should be arr[j] > arr[j+1]
                arr[i], arr[j] = arr[j], arr[i]  # swapping might be wrong
    return arr

def main():
    numbers = [5, 2, 9, 1, 5, 6]
    sorted_numbers = linear_sort(numbers)
    print("Sorted numbers are: ", sorted_numbers)  # might print wrong result

if __name__ == "__main__":
    main()
