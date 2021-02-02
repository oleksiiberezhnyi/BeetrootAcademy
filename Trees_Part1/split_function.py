def my_splits(s: str):
    math_signs = {'*', '-', '/', '+', '(', ')'}
    res = []
    math_index = []
    n = 0
    for i in range(len(s)):
        if s[i] in math_signs:
            math_index.append(i)
    for i in math_index:
        res.append(s[n:i].replace(' ', ''))
        res.append(s[i])
        n = i + 1
        if i == math_index[-1]:
            res.append(s[n:])
    res = list(filter(lambda i: i != '', res))
    return res


def my_splits_bool(s: str):
    bool_operator = {'/', '+', '-', '(', ')'}
    bool_string = s.replace('or', '/')
    bool_string = bool_string.replace('and', '+')
    bool_string = bool_string.replace('not', '-')
    res = []
    math_index = []
    n = 0
    for i in range(len(bool_string)):
        if bool_string[i] in bool_operator:
            math_index.append(i)
    for i in math_index:
        res.append(bool_string[n:i].replace(' ', ''))
        res.append(bool_string[i])
        n = i + 1
        if i == math_index[-1]:
            res.append(bool_string[n:])
    for i in range(len(res)):
        if res[i] == '/':
            res[i] = 'or'
        elif res[i] == '+':
            res[i] = 'and'
        elif res[i] == '-':
            res[i] = 'not'
    res = list(filter(lambda i: i != '', res))
    return res


print(my_splits_bool("not ( ( True and False ) or False )"))
