arr_str = input('Please enter three integers:\n')

arr = arr_str.split()

for i in range(len(arr)):
    arr[i] = int(arr[i])

arr.sort(reverse=False)

print('Sort result:\n' + str(arr))