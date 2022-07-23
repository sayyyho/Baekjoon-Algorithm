import sys

input = sys.stdin.readline

n, m = map(int, input().split())
num_arr = list(map(int, input().split()))
inter_sum_arr = [0]
index = 0
for num in num_arr:
  inter_sum_arr.append(inter_sum_arr[index]+num) 
  index += 1
  
for _ in range(m):
  i, j = map(int, input().split())
  print(inter_sum_arr[j] - inter_sum_arr[i-1])