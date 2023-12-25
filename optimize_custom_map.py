ls1 = [1, 2, 3]
ls2 = [4, 5]

def optimized_custom_map(func,*iterables):
    min_length = min(len(i) for i in iterables)
    return [func(*[ j[i] for j in iterables]) for i in range(min_length)]

i = optimized_custom_map(lambda x, y: x + y, ls1, ls2)
print(i)



