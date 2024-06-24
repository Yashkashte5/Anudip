def interchange(lst):
    if len(lst) < 2:
        return lst
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst
oglist = [1, 2, 3, 4, 5]
interchanged_list = interchange(oglist)
print("Original List:", oglist)
print("Interchanged List:", interchanged_list)