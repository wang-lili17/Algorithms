import heapq

numbers_list = []
n = int(input("enter the amount of numbers "))

for i in range(n):
    number = int(input(f"enter number {i+1}: "))
    numbers_list.append(number)

def heapsort(numbers_list):
  heapq.heapify(numbers_list)
  m=len(numbers_list)
  sorted_list = []
  for i in range(m):
    sorted_list.append((heapq.heappop(numbers_list)))
  return sorted_list

sorted_numbers=heapsort(numbers_list)
print(sorted_numbers)
