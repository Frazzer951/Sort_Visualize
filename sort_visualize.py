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


def selection_sort():
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


def merge(start, mid, end):
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
                index -= 1
            array[start] = value
            update()
            start += 1
            mid += 1
            start2 += 1


def merge_sort(left=0, right=len(array) - 1):
    if left < right:
        mid = left + (right - left) // 2
        merge_sort(left, mid)
        merge_sort(mid + 1, right)
        merge(left, mid, right)


def bubble_sort():
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                update()


def heapify(n, i):
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
        heapify(n, largest)


def heap_sort():
    n = len(array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)
    for i in range(n - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        update()
        heapify(i, 0)


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
    update()
    sleep(1)

    # Uncomment the lines for the sorting algorithm you want to use
    # threading.Thread(target=selection_sort, daemon=True).start()
    # threading.Thread(target=merge_sort, daemon=True).start()
    # threading.Thread(target=bubble_sort, daemon=True).start()
    threading.Thread(target=heap_sort, daemon=True).start()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == "__main__":
    main()
