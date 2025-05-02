def get_num_words(text):
    text_arr = text.split()
    num_words = len(text_arr)
    return num_words

def char_count(text):
    text = text.lower()
    chars = {}
    for i in text :
        if i in chars:
            chars[i] += 1
        else:
            chars[i] = 1
    return chars

def sort_on(dict):
    return dict["num"]

def sort_dict_lists(dict):
    dict_list = []
    for i in dict:
        if str.isalpha(i):
            item = {"char": i, "num": dict[i]}
            dict_list.append(item)
    dict_list.sort(key= sort_on, reverse= True)
    return dict_list