N = 7 

ind = 0

lm = [7 - x  for x in range (0, N)]

for i in range(0,N-1):
  for j in range(0,N):
    print (lm[j], end=" ")
  print()
  lm.insert(0,lm[0]-1)
  lm.pop()