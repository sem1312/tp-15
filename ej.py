import py5
import random
import time

array = []
n = 50 
sorted_flag = False
algorithm = "bubble_sort"
delay = 0.1

def generate_array():
    global array, sorted_flag
    array = [random.randint(10, py5.height - 10) for _ in range(n)]
    sorted_flag = False

def setup():
    py5.size(600, 400)
    py5.background(255)
    generate_array()

def draw_array():
    bar_width = py5.width / n
    for i in range(n):
        py5.fill(100, 100, 255)
        py5.rect(i * bar_width, py5.height - array[i], bar_width - 2, array[i])

def bubble_sort_step():
    global sorted_flag
    sorted_flag = True
    for i in range(n - 1):
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
            sorted_flag = False
        draw_array()
        time.sleep(delay)
        py5.redraw()
    return sorted_flag

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            draw_array()
            time.sleep(delay)
            py5.redraw()
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def draw():
    py5.background(255)
    draw_array()
    if not sorted_flag and algorithm == "bubble_sort":
        sorted_flag = bubble_sort_step()
    elif not sorted_flag and algorithm == "quick_sort":
        quick_sort(array, 0, len(array) - 1)

def key_pressed():
    global algorithm, sorted_flag
    if py5.key == 'r':
        generate_array()
        sorted_flag = False
    elif py5.key == 'b':
        algorithm = "bubble_sort"
        sorted_flag = False
    elif py5.key == 'q':
        algorithm = "quick_sort"
        sorted_flag = False

py5.run_sketch()
