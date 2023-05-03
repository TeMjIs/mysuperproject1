#----------------------------------
#Program by Tem
#
#
#Version    Date        Info
#1.0        2023    Initital version
#
#----------------------------------

def binarysearch(mylist, iskat, start, stop):
    if start > stop:
        return False
    else:
        mid = (start + stop) // 2
        if iskat == mylist[mid]:
            return mid
        elif iskat < mylist[mid]:
            return binarysearch(mylist, iskat, start, mid - 1)
        else:
            return binarysearch(mylist, iskat, mid + 1, stop)


