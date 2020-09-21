def quick(li):
    if len(li) <= 1:
        return li
    else:
        left = [i for i in li if i < li[0]]
        right = [i for i in li if i > li[0]]
        return quick(left) + [i for i in li if i == li[0]] + quick(right)

print(quick([1,2,5,3]))


def mp(li):
    n = len(li)
    for i in range(n):
        for j in range(i, n):
            if li[i] > li[j]:
                li[i], li[j] = li[j], li[i]
    return li

print(mp([1,2,5,3,7,0]))
