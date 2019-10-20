#list = [1,'Hello',3,'Hay boyz',5,'Hay girls',7,'Hay everyone',9]

#i = 0

#list2 = len(list) - 1

#while i <= list2:
 #   print(list[i])
 #   i = i + 1

from graph import *

x1 = 100; y1 = 100
x2 = 300; y2 = 200
N = 10
rectangle (x1, y1, x2, y2)
h = (x2 - x1) / (N + 1)
x = x1 + h
for i in range(N):
  line(x, y1, x, y2)
  x += h

run()
