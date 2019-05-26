# 8) Write a recursive code to search an element in a list using binary search technique.

# function to search value present in list
# and if present this returns true else false
def binary_search(item_list,item):
    first = 0
    last = len(item_list)-1
    found = False
    while( first<=last and not found):
        mid = (first + last)//2
        if item_list[mid] == item :
            found = True
        else:
            if item < item_list[mid]:
                last = mid - 1
            else:
                first = mid + 1	
    return found

# list
lists = [1,2,3,5,8,34,12]
l = int(input('enter value to search : '))
print('value is avilabe : {}'.format( binary_search(lists, l)))