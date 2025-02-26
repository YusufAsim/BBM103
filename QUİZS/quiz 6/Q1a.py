n = 8
dictionary_star = {i: ['*' for j in range(i)] for i in range(1, n+1)}
for value in dictionary_star.values():
    string = ''
    for i in value:
        string = string + i
    print(string)
