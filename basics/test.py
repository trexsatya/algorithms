def simple(limit, wts, vals):
    cumulated = []
    maximum = 0
    for i, weight in enumerate(wts):
        tmp = []
        for c in cumulated:
            if weight + c[0] <= limit:
                tmp.append([weight + c[0], vals[i] + c[1]])
                maximum = max(maximum, vals[i] + c[1])
        if weight <= limit:
            tmp.append([weight, vals[i]])
            maximum = max(maximum, vals[i])
        cumulated.extend(tmp)

    return maximum

weights = [2, 3,  4,  6]
values  = [9, 14, 16, 30]

res = simple(10, weights, values)
print(res)
