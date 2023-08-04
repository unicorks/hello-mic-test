# q 42 from list worksheet

def counter(strings):
    e = [x for x in strings if len(x) >= 2 and x[0] == x[-1]]
    return len(e)

print(counter(['cbc', '121', 'abc']))
