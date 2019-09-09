
def quicksort(my_list):
        pivot = my_list[0]
        i = 0
        for j in range(len(my_list)-1):
            if my_list[j+1] < pivot:
                my_list[j+1],my_list[i+1] = my_list[i+1], my_list[j+1]
                i += 1
        my_list[0],my_list[i] = my_list[i],my_list[0]
        first_part = quicksort(my_list[:i])
        second_part = quicksort(my_list[i+1:])
        first_part.append(my_list[i])
        return first_part + second_part

my_list = [54,26,93,17,77,31,44,55,20]
print(quicksort(my_list))
