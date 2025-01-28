from typing import List


class Solution:

    def findMaxFish(self, grid: List[List[int]]) -> int:

        # Depth-first search function to explore the grid and count fish

        def dfs(i: int, j: int) -> int:

            fish_count = grid[i][j]  # Number of fish at the current location

            grid[i][j] = 0  # Mark the current location as visited by setting it to 0

            # Explore all four adjacent cells (up, down, left, right)

            for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:

                x, y = i + dx, j + dy

                # Check if the new position is within the grid bounds and has fish

                if 0 <= x < m and 0 <= y < n and grid[x][y]:

                    fish_count += dfs(x, y)  # Add fish from the neighboring cell

            return fish_count


        m, n = len(grid), len(grid[0])  # Get the dimensions of the grid

        max_fish = 0  # Initialize the maximum fish count

        # Iterate over all cells in the grid

        for i in range(m):

            for j in range(n):

                # If the current cell has fish, perform DFS from here

                if grid[i][j]:

                    max_fish = max(max_fish, dfs(i, j))  # Update the maximum fish count

        return max_fish  # Return the maximum number of fish that can be found in one group