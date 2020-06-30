from collections import deque

def numIslands(grid):
    """Take in a grid of 1s (land) and 0s (water) and return the number of islands."""
    def bfs(row, col):
        queue = deque(((row, col),))

        while len(queue):
            cur_row, cur_col = queue.popleft()

            if (cur_row >= 0 and cur_row < len(grid) and
                cur_col >= 0 and cur_col < len(grid[0]) and
                grid[cur_row][cur_col] == '1'):
                queue.extend(((cur_row, cur_col+1), (cur_row, cur_col-1), (cur_row+1, cur_col),
                              (cur_row-1, cur_col)))
                grid[cur_row][cur_col] = '0'
    count = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '1':
                bfs(row, col)
                count += 1
    return count

def timeToRot(grid):
    """
    Take in a grid of numbers, where 0 is an empty space, 1 is a fresh orange, and 2 is a rotten
    orange. Each minute, a rotten orange contaminates its 4-directional neighbors. Return the number
    of minutes until all oranges rot.
    """
    queue = deque()
    total_seconds = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 2:
                grid[row][col] = 1
                queue.append((row, col, 0))

    while len(queue):
        cur_row, cur_col, seconds = queue.popleft()

        if (cur_row >= 0 and cur_row < len(grid) and
            cur_col >= 0 and cur_col < len(grid[0]) and
            grid[cur_row][cur_col] == 1):
            queue.extend(((cur_row, cur_col+1, seconds+1), (cur_row, cur_col-1, seconds+1),
                          (cur_row+1, cur_col, seconds+1), (cur_row-1, cur_col, seconds+1)))
            grid[cur_row][cur_col] = 0
            total_seconds = max(total_seconds, seconds)

    for row in grid:
        if any(row):
            return -1
    return total_seconds

def courseOrder(numCourses, prerequisites):
    """Return a course schedule according to the prerequisites provided."""
    pass

def wordLadderLength(beginWord, endWord, wordList):
    """Return the length of the shortest word chain from beginWord to endWord, using words from wordList."""
    pass


if __name__ == '__main__':
    # numIslands Test Cases
    map1 = [
        [1, 1, 1, 1, 0],
        [1, 1, 0, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    assert numIslands(map1) == 1

    map2 = [
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 1]
    ]
    assert numIslands(map2) == 3

    # timeToRot Test Cases
    oranges1 = [
        [2,1,1],
        [1,1,0],
        [0,1,1]
    ]
    assert timeToRot(oranges1) == 4

    oranges2 = [
        [2,1,1],
        [0,1,1],
        [1,0,1]
    ]
    assert timeToRot(oranges2) == -1

    oranges3 = [
        [0,2]
    ]
    assert timeToRot(oranges3) == 0

    # courseOrder Test Cases
    courses1 = [ [1,0] ]
    assert courseOrder(2, courses1) == [0, 1]

    courses2 = [ [1,0], [2,0], [3,1], [3,2] ]
    possibleSchedules = [ [0, 1, 2, 3], [0, 2, 1, 3] ]
    assert courseOrder(4, courses2) in possibleSchedules

    # wordLadderLength Test Cases
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]

    assert wordLadderLength(beginWord, endWord, wordList) == 5
