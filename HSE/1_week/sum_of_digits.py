numb = int(input())

iter = 3
sum = 0
while (iter > 0):
  dig = numb % 10
  numb = numb // 10
  sum = sum + dig
  iter = iter - 1
print(sum)
