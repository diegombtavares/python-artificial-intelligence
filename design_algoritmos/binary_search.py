def binary_search(arr, start, end, key):
    while start <= end:
        mid = start + (end - start) // 2
        
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            start = mid + 1
        else:
            end = mid - 1

arr = [4, 5, 8, 10, 15, 20, 27, 38]
key = 20

result = binary_search(arr, 0, len(arr) -1, key)
