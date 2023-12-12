def count_paths(n, m):
    if n <= 0 or m <= 0:
        return 0
    if n == 1 and m == 1:
        return 1
    return count_paths(n - 2, m - 1) + count_paths(n - 1, m - 2)

n = int(input())
m = int(input())

result = count_paths(n, m)
print(result)
