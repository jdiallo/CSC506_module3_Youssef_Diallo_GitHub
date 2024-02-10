# CSC 506
# Critical thinking 3
# Upload to Github

import random
import time

def generate_random_list(size):
  """Generates a list of random integers of the specified size."""
  return [random.randint(0, 1000) for _ in range(size)]

def benchmark_sort(sort_func, data):
  """Measures the execution time of a sorting function on the given data."""
  start_time = time.time()
  sort_func(data)
  end_time = time.time()
  return end_time - start_time

def bubble_sort(data):
  """Implementation of bubble sort algorithm."""
  swapped = True
  while swapped:
    swapped = False
    for i in range(len(data) - 1):
      if data[i] > data[i + 1]:
        data[i], data[i + 1] = data[i + 1], data[i]
        swapped = True

def selection_sort(data):
  """Implementation of selection sort algorithm."""
  for i in range(len(data)):
    min_index = i
    for j in range(i + 1, len(data)):
      if data[j] < data[min_index]:
        min_index = j
    data[i], data[min_index] = data[min_index], data[i]

def merge_sort(data):
  """Implementation of merge sort algorithm."""
  if len(data) <= 1:
    return data
  mid = len(data) // 2
  left = merge_sort(data[:mid])
  right = merge_sort(data[mid:])
  return merge(left, right)

def merge(left, right):
  """Merges two sorted lists."""
  merged = []
  i = j = 0
  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      merged.append(left[i])
      i += 1
    else:
      merged.append(right[j])
      j += 1
  merged += left[i:]
  merged += right[j:]
  return merged

# Generate random data
data = generate_random_list(500)

# Benchmark different sorting algorithms
algorithms = {
  "Bubble Sort": bubble_sort,
  "Selection Sort": selection_sort,
  "Merge Sort": merge_sort,
  # Add other sorting algorithms here
}

results = {}
for name, sort_func in algorithms.items():
  time_taken = benchmark_sort(sort_func, data.copy())
  results[name] = time_taken

# Print results
print("Sorting Algorithm | Execution Time (s)")
for name, time_taken in results.items():
  print(f"{name:<17} | {time_taken:.4f}")

# Compare execution speeds
fastest_name, fastest_time = min(results.items(), key=lambda item: item[1])
for name, time_taken in results.items():
  if name != fastest_name:
    time_diff = time_taken - fastest_time
    print(f"{name} is {time_diff:.4f} seconds slower than {fastest_name}")
