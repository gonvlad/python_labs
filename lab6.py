import random
from builtins import enumerate
from pprint import pprint
from time import time
import json


def bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True

    return nums


def selection_sort(nums):
    for i in range(len(nums)):
        lowest_value_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]

    return nums


def insertion_sort(nums):
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = item_to_insert

    return nums


def heapify(nums, heap_size, root_index):
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2
    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child
    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child
    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        heapify(nums, heap_size, largest)


def heap_sort(nums):
    n = len(nums)
    for i in range(n, -1, -1):
        heapify(nums, n, i)
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)

    return nums


def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0
    left_list_length, right_list_length = len(left_list), len(right_list)
    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1
    return sorted_list


def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])
    return merge(left_list, right_list)


def partition(nums, low, high):
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1
        j -= 1
        while nums[j] > pivot:
            j -= 1
        if i >= j:
            return j
        nums[i], nums[j] = nums[j], nums[i]


def quick_sort(nums):
    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)

    return nums

algorithms_func = [bubble_sort, selection_sort, insertion_sort, heap_sort, merge_sort, quick_sort, sorted]
sizes = [100, 1000, 3000, 5000, 7000, 10000, 20000, 50000]
results = [[0] * len(sizes) for _ in range(len(algorithms_func))]

def check(algorithm, size: int) -> float:
    time_work = []
    for _ in range(10):
        time_start = time()
        algorithm([random.randrange(1001) for _ in range(size)])
        time_work.append(time() - time_start)
    return sum(time_work) / len(time_work)


for y, func in enumerate(algorithms_func):
    for x, size in enumerate(sizes):
        results[y][x] = check(func, size)
        print(f'func №{y} size {size} COMPLETED | time = {results[y][x]}')


with open('results.json', 'w') as f:
    json.dump(results, f)


with open('results.json') as f:
    results = json.load(f)

import chart_studio
import chart_studio.plotly as py
import plotly.graph_objects as go

USERNAME = 'gonvlad'
API_KEY = 'oqdcqXmDWT1jKXfBEi8s'

chart_studio.tools.set_credentials_file(username=USERNAME, api_key=API_KEY)

sizes = [100, 1000, 3000, 5000, 7000, 10000, 20000, 50000]

data = []
for r in results:
    data.append(go.Scatter(x=sizes, y=r))

py.plot(data, filename='basic-line', auto_open=True)
