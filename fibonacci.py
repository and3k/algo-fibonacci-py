def fibonacci(n):
  f = [0,1]
  if n == 0:
    return 0
  if n == 1:
    return 1
  #print(2 - 1 + 2 - 2)
  for seq in range(2, n + 1):
    total = f[seq - 1] + f[seq - 2]
    f.append(total)
  return f[n]


