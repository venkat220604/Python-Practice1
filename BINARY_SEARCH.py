arr=[2,4,5,6,8,10]
low=0
high=len(arr)-1
target= 10
while low <= high:
    mid = (low + high)//2
    if arr[mid] == target :
        print("found at",mid) 
        break
    elif arr[mid] < target :
        low = mid +1
    else:
        high = mid-1