def words(stmt):
    words_list = str(stmt).split()
    words_dict = {}
    for wrd in words_list:
        if wrd.isdigit():
            wrd = int(wrd)
        words_dict[wrd] = words_list.count(str(wrd))
        
    return words_dict

def find_max_min(my_list):
    my_list.sort()
    if my_list[0] == my_list[-1]:
        return [len(my_list)]
    return [my_list[0], my_list[-1]]


