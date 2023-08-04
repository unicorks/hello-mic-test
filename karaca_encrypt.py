def encryption_algo(string):
    string = string[::-1]
    change = {'a': 0, 'e': 1, 'i': 2, 'o': 2, 'u': 3}
    return ''.join([str(change[x])  if x in change else x for x in string]) + 'aca'

print(encryption_algo('apple'))
