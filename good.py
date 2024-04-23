arr = [1, 2, 3, 4, 5, 6]
def bin_search(arr, n, low, high): 
    if low <= high: 
        mid = (low+high) // 2 
        if arr[mid] == n: 
            return mid 
        elif arr[mid] < n: 
            return bin_search(arr, n, mid+1, high)
        else: 
            return bin_search(arr, n, low, mid-1)
    else: 
        return -1
