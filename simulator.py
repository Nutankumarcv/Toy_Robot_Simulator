from robot import Robot

class ToyRobotSimulator:
    def __init__(self):
        self.robot = Robot()

    def execute_command(self, command):
        if command.startswith('PLACE'):
            params = command.split(' ')[1].split(',')
            x, y, direction = int(params[0]), int(params[1]), params[2]
            return self.robot.place(x, y, direction)
        elif command == 'MOVE':
            return self.robot.move()
        elif command == 'LEFT':
            return self.robot.left()
        elif command == 'RIGHT':
            return self.robot.right()
        elif command == 'REPORT':
            return self.robot.report()
        else:
            return False