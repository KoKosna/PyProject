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
def bucket_sort(arr,minEl,maxEl):
    range = maxElement - minElement
    
print("Выбирите метод сортировки: пузырьковый-1, гномий-2, блочный-3, пирамидальный-4")
ans = input()
li = [int(i) for i in input('Введите числа через пробел').split()]
if ans == '1':
    puz_sort(li)
elif ans == '2':
    gnome_sort(li)
print(li[:])

