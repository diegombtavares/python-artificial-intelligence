def linear_search(arr, key):
    for index, value in enumerate(arr):
        if value == key:
            return index
    return -1
        

arr = [3,4,1,6,14]

key = 6

result = linear_search(arr, key)
print(f"O valor {key} está na posição {result}")