def binary_search_recursive(arr, low, high, target):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search_recursive(arr, low, mid - 1, target)
        else:
            return binary_search_recursive(arr, mid + 1, high, target)
    else:
        return -1

array = [2, 3, 4, 10, 40]
x = 10
result = binary_search_recursive(array, 0, len(array) - 1, x)
print("Element is present at index " + str(result))
