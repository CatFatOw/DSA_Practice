# INSERTION SORT
def insertion_sort_algo(arr):
    for i in range(1, len(arr)):
        j = i - 1
        while j >= 0 and arr[j+1] < arr[j]:
            arr[j+1], arr[j] = arr[j], arr[j+1]
            j -= 1
    return arr


# MERGE SORT
#------------

def merge(arr, start, end, mid):
    L = arr[start:mid+1]
    R = arr[mid+1:end+1]
    i = j = 0
    k = start 

    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1


def merge_sort(arr, start, end):
    mid = (start + end) // 2

    if end - start + 1 <= 1:
        return arr 
    left = merge_sort(arr, start, mid)
    right = merge_sort(arr, mid+1, end)
    merge(arr, start, end, mid)


# QUICK SORT 
# ------------------

def quick_sort(arr, s, e):
    pivot = arr[e-1]
    pointer = s

    if e - s + 1 <= 1:
        return arr

    for i in range(s, e):
        if arr[i] < pivot:
            arr[i], arr[pointer] = arr[pointer], arr[i]
            pointer += 1
    arr[pointer], arr[e-1] = arr[e-1], arr[pointer]

    quick_sort(arr, s, pointer-1)
    quick_sort(arr, pointer+1, e)
    return arr 


# BUCKET SORT  (assuming 3 finite elements)
# --------------
def bucket_sort(arr):
    counts = [0,0,0]
    for n in arr:
        counts[n] += 1

    i = 0
    for n in range(len(counts)):
        for j in range(counts[n]):
            arr[i] = n
            i += 1
    return arr

    

    
        
        
        
arr = [4,1,3,6,2]
print(insertion_sort_algo(arr))

arr2 = [4,1,3,6,2]
merge_sort(arr2, start=0, end=len(arr2))
print(arr2)


arr3 = [4,1,3,6,2]
print(quick_sort(arr3, 0, len(arr3)))
            

arr = [0,1,0,2,1]
print(bucket_sort(arr))
