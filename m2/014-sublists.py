#this function check if the list2 is a sublist of list1

def isSublist(list1,list2):
    list1.append(' ')
    if list2[0] in list1:
        indx=list1.index(list2[0])
        c=1
        indx=int(indx+1)
        num=1
        while num != len(list2):
            if list2[c] == list1[indx]:
                print(' ')
            else:
                break
            c=c+1
            indx=indx+1
            num=num+1
        if c == len(list2):
            print('list2 are sublist of list1')
        else:
            print('list2 are not sublist of list1')
