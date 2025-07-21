arr = [3,4,5,6,7]
target = 7
found=False
for i in range(len(arr)):
    if arr[i] == target :
        found =True
        print(f"Found at index {i}")
        break
if not found:
    print("Not Foundd")