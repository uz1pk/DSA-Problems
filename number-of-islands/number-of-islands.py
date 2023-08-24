from ast import List


def numIslands(grid: List[List[str]]) -> int:
    """
    Time: O(m * n) where m is the number of rows and n is the number of columns
    Space: O(1) since we are modifying the input grid in place
    """

    def dfs(x, y):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != "1":
            return
        grid[x][y] = "-1"
        dfs(x + 1, y)
        dfs(x, y + 1)
        dfs(x - 1, y)
        dfs(x, y - 1)

    total = 0
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col == "1":
                dfs(i, j)
                total += 1

    return total
