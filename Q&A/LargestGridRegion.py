
# DFS: Connected Cell in a Grid

# Given an n x m matrix, find and print the number of cells in the largest region in the matrix. Note that 
# there may be more than one region in the matrix.
# https://www.hackerrank.com/challenges/ctci-connected-cell-in-a-grid

def get_biggest_region(grid):
  def bfs(grid, x, y):
    queue = [[x,y]]
    start, end = 0, 1
    
    while (start < end):
      for pos in xrange(start, end):
        curPos = queue[pos]
        for i in xrange(-1,2):
          for j in xrange(-1, 2):
            aX, aY = curPos[0] + i, curPos[1] + j

            if [aX, aY] not in queue and -1 < aY < len(grid) and -1 < aX < len(grid[0]) and grid[aY][aX]:
              queue.append([aX, aY])
              grid[aY][aX] = 0
      start = end
      end = len(queue)
      
    return len(queue)
  
  maxReg = 0
  
  for y in xrange(len(grid)):
    for x in xrange(len(grid[0])):
      if grid[y][x]:
        maxReg = max(maxReg, bfs(grid, x, y))
  
  return maxReg
      
n = int(raw_input().strip())
m = int(raw_input().strip())
grid = []
for grid_i in xrange(n):
    grid_temp = map(int, raw_input().strip().split(' '))
    grid.append(grid_temp)
print get_biggest_region(grid)