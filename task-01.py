import random
import time
import matplotlib.pyplot as plt

def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)

def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # Використовуємо середній елемент як pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)

def measure_execution_time(sort_function, arr, repetitions=5):
    times = []
    for _ in range(repetitions):
        arr_copy = arr.copy()
        start_time = time.time()
        sort_function(arr_copy)
        times.append(time.time() - start_time)
    return sum(times) / repetitions

sizes = [10_000, 50_000, 100_000, 500_000]
randomized_times = []
deterministic_times = []

for size in sizes:
    test_array = [random.randint(0, 10**6) for _ in range(size)]
    random_time = measure_execution_time(randomized_quick_sort, test_array)
    deterministic_time = measure_execution_time(deterministic_quick_sort, test_array)
    randomized_times.append(random_time)
    deterministic_times.append(deterministic_time)
    print(f"Розмір масиву: {size}")
    print(f"   Рандомізований QuickSort: {random_time:.4f} секунд")
    print(f"   Детермінований QuickSort: {deterministic_time:.4f} секунд")

plt.figure(figsize=(10, 6))
plt.plot(sizes, randomized_times, marker='o', label='Рандомізований QuickSort')
plt.plot(sizes, deterministic_times, marker='s', label='Детермінований QuickSort')
plt.xlabel('Розмір масиву')
plt.ylabel('Середній час виконання (секунди)')
plt.title('Порівняння ефективності QuickSort')
plt.legend()
plt.grid(True)
plt.show()
