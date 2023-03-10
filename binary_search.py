def binary_serach(list, item):
    low = 0
    high = len(list) - 1                #za pomocą high i low kontrolujemy, która część listy jest przeszukiwana

    while low <= high:                  #dopóki obszar poszukiwań nie został zawężony do jednego elementu...
        mid = (low + high)              #...wybieramy środkowy element
        guess = list[mid]
        if guess == item:               #znaleziono element
            return mid
        if guess > item:                #strzelono za dużą liczbę
            high = mid - 1
        else:                           #strzelono za małą liczbę
            low = mid + 1
    return None                         #nie ma takiego elementu w liście

#test
my_list = [1, 3, 5, 7, 8]

print(binary_serach(my_list, 3))
print(binary_serach(my_list, 4))