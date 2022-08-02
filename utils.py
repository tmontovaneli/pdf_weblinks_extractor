def sort_by_amount_of_values(dict, reverse=True):
    tmp = {}
    for k in dict.keys():
        tmp[k] = len(dict[k])

    return sorted(tmp.items(), key=lambda kv: kv[1], reverse=reverse)