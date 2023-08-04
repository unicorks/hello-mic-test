def item_frequency(items):
    return {x: items.count(x) for x in set(items)}

print(item_frequency([1, 1, 2, 3, 2, 3, 3]))
