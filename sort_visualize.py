import pygame
import random
from time import sleep
import threading
from colour import Color


pygame.init()
WIDTH = 1000
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

SLEEP_TIME = 0.01
array = [x for x in range(0, 200)]
height_value = int(HEIGHT / max(array))
width = WIDTH / len(array)
start_x = 0
start_y = HEIGHT - max(array) * height_value

colors = list(Color("red").range_to(Color("blue"), len(array)))

colors = [
    (int(255 * color.red), int(255 * color.green), int(255 * color.blue))
    for color in colors
]


def selection_sort(array):
    sorted_index = 0
    while sorted_index < len(array) - 1:
        min_index = sorted_index
        for i in range(sorted_index, len(array)):
            if array[i] < array[min_index]:
                min_index = i
        array[sorted_index], array[min_index] = (
            array[min_index],
            array[sorted_index],
        )
        sorted_index += 1
        update()


def merge(array, start, mid, end):
    start2 = mid + 1
    if array[mid] <= array[start2]:
        return
    while start <= mid and start2 <= end:
        if array[start] <= array[start2]:
            start += 1
        else:
            value = array[start2]
            index = start2

            while index != start:
                array[index] = array[index - 1]
                update()
                index -= 1
            array[start] = value
            update()
            start += 1
            mid += 1
            start2 += 1


def merge_sort(array, left=0, right=len(array) - 1):
    if left < right:
        mid = left + (right - left) // 2
        merge_sort(array, left, mid)
        merge_sort(array, mid + 1, right)
        merge(array, left, mid, right)


def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                update()


def heapify(array, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and array[largest] < array[left]:
        largest = left
    if right < n and array[largest] < array[right]:
        largest = right

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        update()
        heapify(array, n, largest)


def heap_sort(array):
    n = len(array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)
    for i in range(n - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        update()
        heapify(array, i, 0)


def comb_sort(array):
    length = len(array)
    _gap = length
    shrink = 1.3
    sorted = False
    while not sorted:
        _gap /= shrink
        gap = int(_gap)
        if gap <= 1:
            sorted = True
            gap = 1
        for i in range(length - gap):
            sm = gap + i
            if array[i] > array[sm]:
                array[i], array[sm] = array[sm], array[i]
                update()
                sorted = False


def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            update()
            j -= 1
        array[j + 1] = key
        update()


def shell_sort(array):
    gap = len(array) // 2
    while gap > 0:
        i = 0
        j = gap
        while j < len(array):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
                update()
            i += 1
            j += 1

            k = i
            while k - gap > -1:
                if array[k - gap] > array[k]:
                    array[k - gap], array[k] = array[k], array[k - gap]
                    update()
                k -= 1
        gap //= 2


def update():
    screen.fill((255, 255, 255))

    max_height = max(array) * height_value

    for i in range(len(array)):
        height = height_value + array[i] * height_value
        pygame.draw.rect(
            screen,
            colors[array[i] % len(colors)],
            pygame.Rect(
                start_x + i * width,
                start_y + max_height - height,
                width,
                height,
            ),
        )

    pygame.display.flip()
    sleep(SLEEP_TIME)


def main():
    random.shuffle(array)
    # array.reverse()
    update()
    sleep(1)

    # Uncomment the lines for the sorting algorithm you want to use
    # threading.Thread(target=bubble_sort, daemon=True, args=[array]).start()
    # threading.Thread(target=comb_sort, daemon=True, args=[array]).start()
    # threading.Thread(target=selection_sort, daemon=True, args=[array]).start()
    # threading.Thread(target=insertion_sort, daemon=True, args=[array]).start()
    # threading.Thread(target=heap_sort, daemon=True, args=[array]).start()
    threading.Thread(target=shell_sort, daemon=True, args=[array]).start()
    # threading.Thread(target=merge_sort, daemon=True, args=[array]).start()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == "__main__":
    main()
