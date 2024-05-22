from random import choice

class RandomWalk:
    """A class to generate random walks."""
    
    def __init__(self, num_points=16):
        """Initialize attributes of a walk."""
        self.num_points = num_points
        
        # All walks start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all the points in the walk."""
        rows = 4
        cols = 4

        # Initialize a 2D board with None values
        board = [[None for _ in range(cols)] for _ in range(rows)]
        
        # Starting position
        x, y = 0, 0
        board[x][y] = 0

        while len(self.x_values) < self.num_points:
            # Decide which direction to go and how far to go in that direction.
            x_direction = choice([1, -1])
            y_direction = choice([1, -1])

            new_x = x + x_direction
            new_y = y + y_direction

            # Reject moves that go out of bounds.
            if new_x < 0 or new_x >= rows or new_y < 0 or new_y >= cols:
                continue
            
            # Check if the new position is already visited
            if board[new_x][new_y] is not None:
                continue
            
            # Move to the new position
            x, y = new_x, new_y
            board[x][y] = len(self.x_values)
            
            self.x_values.append(x)
            self.y_values.append(y)

        return board

# Create an instance of RandomWalk and generate the walk
rw = RandomWalk(num_points=16)  # Limiting to 16 steps for a 4x4 grid
board = rw.fill_walk()

# Print the resulting board
for row in board:
    print(row)