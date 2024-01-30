def memo(func):
    L = []
    def res(num):
        nonlocal L
        if num >= len(L):
            L = L + [-1] * (num + 1)
        if L[num] == -1:
            L[num] = func(num)
        return L[num]
    return res


def square(num):
    return num * num


memsquare = memo(square)
num = int(input())
print(memsquare(num))