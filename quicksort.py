#O(n log n)

def quicksort(array):
    if len(array) < 2:
        return array                                    #tablice puste i jednoelementowe są z góry posortowane
    else:
        pivot = array[0]                                #przypadek rekurencyjny/ pivot = element osiowy
        less = [i for i in array[1:] if i <= pivot]     #podtablica zawierająca wszystkie elementy mniejsze od pivot
        greater = [i for i in array[1:] if i > pivot]   #podtablica zawierające wszystkie elementy większe od pivot
        return quicksort(less) + [pivot] + quicksort(greater)

#test
print(quicksort([10, 5, 2, 3]))