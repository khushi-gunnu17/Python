

def binary_search(arr, key) :
    size = len(arr)

    start = 0
    end = size - 1

    mid = start + (end - start) // 2

    while(start <= end) :
        if (arr[mid] == key) :
            return mid
        
        if (arr[mid] < key) :
            start = mid + 1

        else :
            end = mid - 1

        mid = start + (end - start) // 2

    return -1


arr = [0, 1, 2, 4, 9]
target = 1
result = binary_search(arr, target)

if result != -1 :
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the array")