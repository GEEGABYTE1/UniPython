from random import randrange 

def quicksort(lst, start, end):
    if start >= end:
        return lst 
    else:
        pivot_idx = randrange(start, end)
        pivot_element = lst[pivot_idx]
        lst[end], lst[pivot_idx] = lst[pivot_idx], lst[end]
        lesser_than_pointer = start 
        
        for i in range(start, end):
            if lst[i] < pivot_element:
                lst[i], lst[lesser_than_pointer] = lst[lesser_than_pointer], lst[i]

                lesser_than_pointer += 1 

        lst[end], lst[lesser_than_pointer] = lst[lesser_than_pointer], lst[end]
        quicksort(lst, start, lesser_than_pointer - 1)
        quicksort(lst, lesser_than_pointer + 1, end)