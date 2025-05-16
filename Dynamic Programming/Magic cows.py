def magic_cows(A,initial_cows):
  max_days=len(A)-1
  C=len(A[0])-1

  for cow in initial_cows:
    if cow <= C:
        A[0][cow] += 1

  for day in range(max_days):
    for i in range(C + 1):
      if i <= C / 2:
        if 2 * i <= C:
            A[day + 1][2 * i] += A[day][i]
      else:
            A[day + 1][i] += 2 * A[day][i]

  return A

def total_farms_on_day(A, day):
    print(sum(A[day]))

def farms_with_x_cow_on_day_n(A, n, x):
    return A[n][x] if 0 <= x < len(A[0]) else 0

initial_cows = [1, 1, 2, 3]
day=3
C=8
max_days=4
A= [[0 for _ in range(C + 1)] for _ in range(max_days + 1)]

A=magic_cows(A,initial_cows)
print(A)
for row in A:
    print(row)