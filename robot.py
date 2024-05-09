class Robot:
    def __init__(self):
        self.x = None
        self.y = None
        self.direction = None
        self.is_placed = False

    def place(self, x, y, direction):
        if self._is_valid_position(x, y) and self._is_valid_direction(direction):
            self.x = x
            self.y = y
            self.direction = direction
            self.is_placed = True
        else:
            return False

    def move(self):
        if not self.is_placed:
            return False

        if self.direction == 'NORTH' and self.y < 4:
            self.y += 1
        elif self.direction == 'SOUTH' and self.y > 0:
            self.y -= 1
        elif self.direction == 'EAST' and self.x < 4:
            self.x += 1
        elif self.direction == 'WEST' and self.x > 0:
            self.x -= 1
        return True

    def left(self):
        if not self.is_placed:
            return False

        directions = ['NORTH', 'EAST', 'SOUTH', 'WEST']
        current_index = directions.index(self.direction)
        self.direction = directions[(current_index - 1) % 4]
        return True

    def right(self):
        if not self.is_placed:
            return False

        directions = ['NORTH', 'WEST', 'SOUTH', 'EAST']
        current_index = directions.index(self.direction)
        self.direction = directions[(current_index + 1) % 4]
        return True

    def report(self):
        if self.is_placed:
            return f"Output: {self.x},{self.y},{self.direction}"
        else:
            return "Robot is not placed yet!"

    def _is_valid_position(self, x, y):
        return 0 <= x <= 4 and 0 <= y <= 4

    def _is_valid_direction(self, direction):
        return direction in ['NORTH', 'SOUTH', 'EAST', 'WEST']