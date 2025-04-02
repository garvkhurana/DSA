sorted_list = [10, 20, 30, 40, 50, 60]
target = 20

def binary_search(array, target):
    size = len(array) - 1
    start = 0
    end = size

    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid  # Target found, return index
        
        elif array[mid] < target:  # Move to the right half
            start = mid + 1
            
        else:  # Move to the left half
            end = mid - 1
            
    return -1  # Target not found

result = binary_search(sorted_list, target)
print(result)
