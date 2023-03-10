#sum numbers in array
def sum(arr):
    if arr != []:
        return arr[0] + sum(arr[1:])
    else:
        return 0

#test
print(sum([2, 4, 6, 8]))
