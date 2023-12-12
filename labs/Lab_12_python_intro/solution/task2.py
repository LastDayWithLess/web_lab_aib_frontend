N = int(input())
numbers = list(map(int, input().split()))

medians_sum = 0
sorted_numbers = []

for i in range(N):
    sorted_numbers.append(numbers[i])
    sorted_numbers.sort()
    median_index = (i + 1) // 2
    
    if (i + 1) % 2 == 0:
        median = sorted_numbers[median_index - 1]
    else:
        median = sorted_numbers[median_index]
    
    medians_sum += median

print(int(medians_sum))
