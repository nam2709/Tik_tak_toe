from random import randint
import numpy as np1

WIDTH = 28
HEIGHT = 28
MARGIN = 2
rownum = 20
colnum = 20

# array is simply a list of lists.
grid = []
for row in range(rownum):
    grid.append([])
    for column in range(colnum):
        grid[row].append(0)  # Append a cell

import numpy as np
print (np.matrix(grid))


def playnvn():
  while True:
      x=int(input())
      y=int(input())
      grid[x][y] = 2
      print (np.matrix(grid))
      # ngang 
      if grid[x][y] == grid[x][y+1] and grid[x][y] == grid[x][y+2] and grid[x][y] == grid[x][y+3]:
          print("win")
          break
      elif grid[x][y] == grid[x][y+1] and grid[x][y] == grid[x][y+2] and grid[x][y] == grid[x][y-1]:
          print("win")
          break
      elif grid[x][y] == grid[x][y+1] and grid[x][y] == grid[x][y-2] and grid[x][y] == grid[x][y-1]:
          print("win")
          break
      elif grid[x][y] == grid[x][y-1] and grid[x][y] == grid[x][y-2] and grid[x][y] == grid[x][y-3]:
          print("win")
          break
      # doc
      elif grid[x][y] == grid[x+1][y] and grid[x][y] == grid[x+2][y] and grid[x][y] == grid[x+3][y]:
          print("win")
          break
      elif grid[x][y] == grid[x+1][y] and grid[x][y] == grid[x+2][y] and grid[x][y] == grid[x-1][y]:
          print("win")
          break
      elif grid[x][y] == grid[x+1][y] and grid[x][y] == grid[x-2][y] and grid[x][y] == grid[x-1][y]:
          print("win")
          break
      elif grid[x][y] == grid[x-1][y] and grid[x][y] == grid[x-2][y] and grid[x][y] == grid[x-3][y]:
          print("win")
          break
      # cheo xuong
      elif grid[x][y] == grid[x+1][y+1] and grid[x][y] == grid[x+2][y+2] and grid[x][y] == grid[x+3][y+3]:
          print("win")
          break
      elif grid[x][y] == grid[x+1][y+1] and grid[x][y] == grid[x+2][y+2] and grid[x][y] == grid[x-1][y-1]:
          print("win")
          break
      elif grid[x][y] == grid[x+1][y+1] and grid[x][y] == grid[x-2][y-2] and grid[x][y] == grid[x-1][y-1]:
          print("win")
          break
      elif grid[x][y] == grid[x-1][y-1] and grid[x][y] == grid[x-2][y-2] and grid[x][y] == grid[x-3][y-3]:
          print("win")
          break
      # cheo len
      elif grid[x][y] == grid[x-1][y+1] and grid[x][y] == grid[x-2][y+2] and grid[x][y] == grid[x-3][y+3]:
          print("win")
          break
      elif grid[x][y] == grid[x-1][y+1] and grid[x][y] == grid[x-2][y+2] and grid[x][y] == grid[x+1][y-1]:
          print("win")
          break
      elif grid[x][y] == grid[x-1][y+1] and grid[x][y] == grid[x+2][y-2] and grid[x][y] == grid[x+1][y-1]:
          print("win")
          break
      elif grid[x][y] == grid[x+1][y-1] and grid[x][y] == grid[x+2][y-2] and grid[x][y] == grid[x+3][y-3]:
          print("win")
          break
      a=int(input())
      b=int(input())
      grid[a][b] = 3
      print (np.matrix(grid))
    # ngang 
      if grid[a][b] == grid[a][b+1] and grid[a][b] == grid[a][b+2] and grid[a][b] == grid[a][b+3]:
          print("win")
          break
      elif grid[a][b] == grid[a][b+1] and grid[a][b] == grid[a][b+2] and grid[a][b] == grid[a][b-1]:
          print("win")
          break
      elif grid[a][b] == grid[a][b+1] and grid[a][b] == grid[a][b-2] and grid[a][b] == grid[a][b-1]:
          print("win")
          break
      elif grid[a][b] == grid[a][b-1] and grid[a][b] == grid[a][b-2] and grid[a][b] == grid[a][b-3]:
          print("win")
          break
    # doc
      elif grid[a][b] == grid[a+1][b] and grid[a][b] == grid[a+2][b] and grid[a][b] == grid[a+3][b]:
          print("win")
          break
      elif grid[a][b] == grid[a+1][b] and grid[a][b] == grid[a+2][b] and grid[a][b] == grid[a-1][b]:
          print("win")
          break
      elif grid[a][b] == grid[a+1][b] and grid[a][b] == grid[a-2][b] and grid[a][b] == grid[a-1][b]:
          print("win")
          break
      elif grid[a][b] == grid[a-1][b] and grid[a][b] == grid[a-2][b] and grid[a][b] == grid[a-3][b]:
          print("win")
          break
    # cheo xuong
      elif grid[a][b] == grid[a+1][b+1] and grid[a][b] == grid[a+2][b+2] and grid[a][b] == grid[a+3][b+3]:
          print("win")
          break
      elif grid[a][b] == grid[a+1][b+1] and grid[a][b] == grid[a+2][b+2] and grid[a][b] == grid[a-1][b-1]:
          print("win")
          break
      elif grid[a][b] == grid[a+1][b+1] and grid[a][b] == grid[a-2][b-2] and grid[a][b] == grid[a-1][b-1]:
          print("win")
          break
      elif grid[a][b] == grid[a-1][b-1] and grid[a][b] == grid[a-2][b-2] and grid[a][b] == grid[a-3][b-3]:
          print("win")
          break
    # cheo len
      elif grid[a][b] == grid[a-1][b+1] and grid[a][b] == grid[a-2][b+2] and grid[a][b] == grid[a-3][b+3]:
          print("win")
          break
      elif grid[a][b] == grid[a-1][b+1] and grid[a][b] == grid[a-2][b+2] and grid[a][b] == grid[a+1][b-1]:
          print("win")
          break
      elif grid[a][b] == grid[a-1][b+1] and grid[a][b] == grid[a+2][b-2] and grid[a][b] == grid[a+1][b-1]:
          print("win")
          break
      elif grid[a][b] == grid[a+1][b-1] and grid[a][b] == grid[a+2][b-2] and grid[a][b] == grid[a+3][b-3]:
          print("win")
          break

def playnvm():
  while True:
      x=int(input())
      y=int(input())
      grid[x][y] = 2
      print (np.matrix(grid))


      if x == x and y == y and grid[x][y] != grid[x][y-1]:
       i = randint(-1,1)
       j = randint(-1,1)
       a = x + i
       b = y + j
       grid[a][b] = 3
       print (np.matrix(grid))
      if x == x and y == y and grid[x][y] == grid[x][y-1] and grid[x][y-2] != 3:
       a = x 
       b = y + 1
       grid[a][b] = 3
       print (np.matrix(grid))
      if x == x and y == y and grid[x][y] == grid[x][y-1] and grid[x][y-2] == 3:
       a = x + 1
       b = y - 2
       grid[a][b] = 3
       print (np.matrix(grid))
      if x == x and y == y and grid[x][y] != grid[x][y-1]:
       i = randint(-1,1)
       j = randint(-1,1)
       a = x + i
       b = y + j
       grid[a][b] = 3
       print (np.matrix(grid))




      # ngang 
      if grid[x][y] == grid[x][y+1] and grid[x][y] == grid[x][y+2] and grid[x][y] == grid[x][y+3]:
          print("win")
          break
      elif grid[x][y] == grid[x][y+1] and grid[x][y] == grid[x][y+2] and grid[x][y] == grid[x][y-1]:
          print("win")
          break
      elif grid[x][y] == grid[x][y+1] and grid[x][y] == grid[x][y-2] and grid[x][y] == grid[x][y-1]:
          print("win")
          break
      elif grid[x][y] == grid[x][y-1] and grid[x][y] == grid[x][y-2] and grid[x][y] == grid[x][y-3]:
          print("win")
          break
      # doc
      elif grid[x][y] == grid[x+1][y] and grid[x][y] == grid[x+2][y] and grid[x][y] == grid[x+3][y]:
          print("win")
          break
      elif grid[x][y] == grid[x+1][y] and grid[x][y] == grid[x+2][y] and grid[x][y] == grid[x-1][y]:
          print("win")
          break
      elif grid[x][y] == grid[x+1][y] and grid[x][y] == grid[x-2][y] and grid[x][y] == grid[x-1][y]:
          print("win")
          break
      elif grid[x][y] == grid[x-1][y] and grid[x][y] == grid[x-2][y] and grid[x][y] == grid[x-3][y]:
          print("win")
          break
      # cheo xuong
      elif grid[x][y] == grid[x+1][y+1] and grid[x][y] == grid[x+2][y+2] and grid[x][y] == grid[x+3][y+3]:
          print("win")
          break
      elif grid[x][y] == grid[x+1][y+1] and grid[x][y] == grid[x+2][y+2] and grid[x][y] == grid[x-1][y-1]:
          print("win")
          break
      elif grid[x][y] == grid[x+1][y+1] and grid[x][y] == grid[x-2][y-2] and grid[x][y] == grid[x-1][y-1]:
          print("win")
          break
      elif grid[x][y] == grid[x-1][y-1] and grid[x][y] == grid[x-2][y-2] and grid[x][y] == grid[x-3][y-3]:
          print("win")
          break
      # cheo len
      elif grid[x][y] == grid[x-1][y+1] and grid[x][y] == grid[x-2][y+2] and grid[x][y] == grid[x-3][y+3]:
          print("win")
          break
      elif grid[x][y] == grid[x-1][y+1] and grid[x][y] == grid[x-2][y+2] and grid[x][y] == grid[x+1][y-1]:
          print("win")
          break
      elif grid[x][y] == grid[x-1][y+1] and grid[x][y] == grid[x+2][y-2] and grid[x][y] == grid[x+1][y-1]:
          print("win")
          break
      elif grid[x][y] == grid[x+1][y-1] and grid[x][y] == grid[x+2][y-2] and grid[x][y] == grid[x+3][y-3]:
          print("win")
          break
      
    # ngang 
      if grid[a][b] == grid[a][b+1] and grid[a][b] == grid[a][b+2] and grid[a][b] == grid[a][b+3]:
          print("win")
          break
      elif grid[a][b] == grid[a][b+1] and grid[a][b] == grid[a][b+2] and grid[a][b] == grid[a][b-1]:
          print("win")
          break
      elif grid[a][b] == grid[a][b+1] and grid[a][b] == grid[a][b-2] and grid[a][b] == grid[a][b-1]:
          print("win")
          break
      elif grid[a][b] == grid[a][b-1] and grid[a][b] == grid[a][b-2] and grid[a][b] == grid[a][b-3]:
          print("win")
          break
    # doc
      elif grid[a][b] == grid[a+1][b] and grid[a][b] == grid[a+2][b] and grid[a][b] == grid[a+3][b]:
          print("win")
          break
      elif grid[a][b] == grid[a+1][b] and grid[a][b] == grid[a+2][b] and grid[a][b] == grid[a-1][b]:
          print("win")
          break
      elif grid[a][b] == grid[a+1][b] and grid[a][b] == grid[a-2][b] and grid[a][b] == grid[a-1][b]:
          print("win")
          break
      elif grid[a][b] == grid[a-1][b] and grid[a][b] == grid[a-2][b] and grid[a][b] == grid[a-3][b]:
          print("win")
          break
    # cheo xuong
      elif grid[a][b] == grid[a+1][b+1] and grid[a][b] == grid[a+2][b+2] and grid[a][b] == grid[a+3][b+3]:
          print("win")
          break
      elif grid[a][b] == grid[a+1][b+1] and grid[a][b] == grid[a+2][b+2] and grid[a][b] == grid[a-1][b-1]:
          print("win")
          break
      elif grid[a][b] == grid[a+1][b+1] and grid[a][b] == grid[a-2][b-2] and grid[a][b] == grid[a-1][b-1]:
          print("win")
          break
      elif grid[a][b] == grid[a-1][b-1] and grid[a][b] == grid[a-2][b-2] and grid[a][b] == grid[a-3][b-3]:
          print("win")
          break
    # cheo len
      elif grid[a][b] == grid[a-1][b+1] and grid[a][b] == grid[a-2][b+2] and grid[a][b] == grid[a-3][b+3]:
          print("win")
          break
      elif grid[a][b] == grid[a-1][b+1] and grid[a][b] == grid[a-2][b+2] and grid[a][b] == grid[a+1][b-1]:
          print("win")
          break
      elif grid[a][b] == grid[a-1][b+1] and grid[a][b] == grid[a+2][b-2] and grid[a][b] == grid[a+1][b-1]:
          print("win")
          break
      elif grid[a][b] == grid[a+1][b-1] and grid[a][b] == grid[a+2][b-2] and grid[a][b] == grid[a+3][b-3]:
          print("win")
          break

playnvn()