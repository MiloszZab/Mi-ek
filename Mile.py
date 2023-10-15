def sweap_max(items: list) -> list:
    item_one = items[0]
    max_item = items[0]
    for x in range(0,len(items)):
        if max_item < items[x]:
            max_item = items[x]
            max_pos = items.index(max_item)
            items[0] = items[x]
    items[max_pos] = item_one
    return items

print(sweap_max([2,8,3,10]))