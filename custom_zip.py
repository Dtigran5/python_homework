ls1 = [1, 2, 3]
ls2 = ['a', 'b', 'c']

def custom_zip(*iterables, strict = False):
    min_len = [len(i) for i in iterables]
    if bool(strict) == True:
        if len(set(min_len)) > 1:
            return " must have the same size"
    min_len = min(min_len)
    return [tuple([j[i] for j in iterables]) for i in range(min_len)]


res = custom_zip(ls1,ls2,strict = True)
print(res)
