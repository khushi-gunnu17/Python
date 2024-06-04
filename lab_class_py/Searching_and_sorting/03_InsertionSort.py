

def insertion_sort(arr) :
    n = len(arr)

    for i in range(n) :
        temp = arr[i]

        j = i-1

        while j >= 0 and temp < arr[j] :
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = temp

    return arr


arr = [12, 11, 13, 5, 6]
sorted_arr = insertion_sort(arr)
print("Sorted array:", sorted_arr)