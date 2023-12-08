def bubble_sort(arr):
    arr_len = len(arr)
    for x in range(arr_len-1):
        a = 0
        for y in range(0, arr_len-x-1):
            if arr[y] > arr[y+1]:
                arr[y+1], arr[y] = arr[y], arr[y+1] 
                a = 1
                if a == 0:
                    break
    return arr

print(bubble_sort([42,71, 9, 58, 13, 15, 45, 97, 91, 85, 19, 26, 65, 8, 38, 47, 69, 59, 33, 67,]))
