#sum numbers in list
def sum(list):
    if list != []:
        return list[0] + sum(list[1:])
    else:
        return 0

#test
print(sum([2, 4, 6, 8]))


#count element in list
def count(list):
    if  list != []:
        return 1 + count(list[1:])
    else:
        return 0

#test
print(count([2, 4, 6, 8]))


#find the biggest number
def max_num(list):
    if len(list) != 2:
        sub_max = max_num(list[1:])
        return list[0] if list[0] > sub_max else sub_max
    else:
        return list[0] if list[0] > list[1] else list[1]

#test
print(max_num([2, 4, 6, 8]))