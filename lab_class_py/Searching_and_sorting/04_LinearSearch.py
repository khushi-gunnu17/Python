

def linear_search(arr, target) :
    for index, element in enumerate(arr) :
        if element == target :
            return index
    return -1

arr = [2, 4, 0, 1, 9]
target = 1
result = linear_search(arr, target)

if result != -1 :
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the array")