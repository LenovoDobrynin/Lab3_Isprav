k = int(input('На сколько сдвигаем? '))
def left_move(a, k):
    while k:
        a = a[1:] + [a[0]]
        k -= 1
    return a
a = [1, 2, 3, 4, 5, 6]
print(a)
print("Влево на "+ str(k), left_move(a, k))