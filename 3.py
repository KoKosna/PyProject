def puz_sort(arr):
    # li = [5,2,7,4,0,9,8,6]
    n = 1
    while n < len(li):
        for i in range(len(li) - n):
            if li[i] > li[i + 1]:
                li[i], li[i + 1] = li[i + 1], li[i]
        n += 1
    return arr

def gnome_sort(arr):
    i = 1
    while i < len(arr):
         if not i or arr[i - 1] <= arr[i]:
            i += 1
         else:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1
    return arr

def bucket_sort(arr):
    largest = max(arr)
    length = len(arr)
    size = largest / length
    buckets = [[] for _ in range(length)]
    for i in range(length):
        j = int(arr[i] / size)
        if j != length:
            buckets[j].append(arr[i])
        else:
            buckets[length - 1].append(arr[i])
    for i in range(length):
        insertion_sort(buckets[i])
    result = []
    for i in range(length):
        result = result + buckets[i]
    return result

def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while (j >= 0 and temp < arr[j]):
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = temp

def heap_sort (arr):
    def sift_down (parent, limit):
        item = arr[parent]
        while True:
            child = (parent << 1) + 1
            if child >= limit:
                break
            if child + 1 < limit and arr[child] < arr[child + 1]:
                child += 1
            if item < arr[child]:
                arr[parent] = arr[child]
                parent = child
            else:
                break
        arr[parent] = item
    # Тело функции heap_sort
    length = len(arr)
    # Формирование первичной пирамиды
    for index in range((length >> 1) - 1, -1, -1):
        sift_down(index, length)
    # Окончательное упорядочение
    for index in range(length - 1, 0, -1):
        arr[0], arr[index] = arr[index], arr[0]
        sift_down(0, index)
    return arr

print("Выбирите метод сортировки: пузырьковый-1, гномий-2, блочный-3, пирамидальный-4")
ans = input()
li = [int(i) for i in input("Введите числа через пробел\n").split()]
if ans == '1':
    puz_sort(li)
elif ans == '2':
    gnome_sort(li)
elif ans == '3':
    li=bucket_sort(li)
elif ans == '4':
    heap_sort(li)
print(li[:])

