# 5. write a recursive code to sum all the elements in the list


def sumListValues(lists):
    if(len(lists) == 0):
        return 0
    else:
        return lists[0]+sumListValues(lists[1:])


# list with integer values
lists = [4, 7, 2, 10, 5, 9, 8, 6]

# funnction call
print('sum of given list', sumListValues(lists))
