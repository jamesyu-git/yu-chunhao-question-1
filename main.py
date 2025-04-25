
def function(array):
    if len(array) < 2:
        return -1

    direction = 0

    for i in range(1, len(array)):
        if array[i] > array[i - 1]:
            if direction == -1:
                return i - 1
            direction = 1
        elif array[i] < array[i - 1]:
            if direction == 1:
                return i - 1
            direction = -1

    return -1

print(function([1, 2, 4, 8, 4, 2, 1]))
print(function([8, 6, 4, 3, 1]))
print(function([1, 2, 3, 4, 5]))
print(function([5, 5, 5, 5]))
print(function([5, 4, 3, 4, 5]))