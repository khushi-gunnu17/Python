

def merge_sort(arr) :
    if len(arr) <= 1 :
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)





def merge(left, right):
    sorted_arr = []
    left_idx, right_idx = 0, 0

    # Merge the two halves while sorting
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            sorted_arr.append(left[left_idx])
            left_idx += 1
        else:
            sorted_arr.append(right[right_idx])
            right_idx += 1

    # Append any remaining elements from left or right halves
    sorted_arr.extend(left[left_idx:])
    sorted_arr.extend(right[right_idx:])

    return sorted_arr



# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)