import tkinter as tk

class ToyRobotGUI:
    def __init__(self, simulator):
        self.simulator = simulator

        self.root = tk.Tk()
        self.root.title("Toy Robot Simulator")

        self.create_widgets()

        self.root.mainloop()

    def create_widgets(self):
        # Enter Command
        instruction_label = tk.Label(self.root, text="Enter Command:")
        instruction_label.pack(side=tk.TOP)

        self.entry = tk.Entry(self.root, width=40)
        self.entry.pack(side=tk.TOP)

        # Execute Command
        execute_button = tk.Button(self.root, text="Execute", command=self.handle_command)
        execute_button.pack(side=tk.TOP)

        place_frame = tk.Frame(self.root)
        place_frame.pack(side=tk.TOP)

        # place x
        place_x_label = tk.Label(place_frame, text="X:")
        place_x_label.pack(side=tk.LEFT)
        self.place_x_entry = tk.Entry(place_frame, width=5)
        self.place_x_entry.pack(side=tk.LEFT)

        # place y
        place_y_label = tk.Label(place_frame, text="Y:")
        place_y_label.pack(side=tk.LEFT)
        self.place_y_entry = tk.Entry(place_frame, width=5)
        self.place_y_entry.pack(side=tk.LEFT)

        # Direction
        place_direction_label = tk.Label(place_frame, text="Direction:")
        place_direction_label.pack(side=tk.LEFT)
        self.place_direction_var = tk.StringVar(self.root)
        self.place_direction_var.set("NORTH")  # Default direction
        place_direction_dropdown = tk.OptionMenu(place_frame, self.place_direction_var, "NORTH", "SOUTH", "EAST", "WEST")
        place_direction_dropdown.pack(side=tk.LEFT)

        # PLACE
        place_button = tk.Button(place_frame, text="PLACE", command=self.handle_place)
        place_button.pack(side=tk.LEFT)

        self.output_label = tk.Label(self.root, text="")
        self.output_label.pack()

        self.canvas = tk.Canvas(self.root, width=250, height=250)
        self.canvas.pack()

        self.update_grid()

    def handle_place(self):
        x = int(self.place_x_entry.get())
        y = int(self.place_y_entry.get())
        direction = self.place_direction_var.get()
        command = f"PLACE {x},{y},{direction}"
        result = self.simulator.execute_command(command)
        if result:
            self.output_label.config(text=result)
        self.update_grid()

    def handle_command(self):
        command = self.entry.get().upper().strip()
        self.entry.delete(0, tk.END)
        result = self.simulator.execute_command(command)
        if result:
            self.output_label.config(text=result)
        self.update_grid()

    def update_grid(self):
        self.canvas.delete("all")

        # Draw tabletop grid
        for i in range(5):
            for j in range(5):
                self.canvas.create_rectangle(i * 50, j * 50, (i + 1) * 50, (j + 1) * 50, outline="black")

        # # Draw vertical split line
        # self.canvas.create_line(1, 0, 1, 260, fill="red", width=4)

        # Draw position indicators
        for i in range(5):
            for j in range(5):
                self.canvas.create_text(i * 50 + 25, j * 50 + 25, text=f"{i},{4-j}")

        # Draw direction legends in the corners
        direction_legends = {'NORTH': ('↑', 'NORTH'), 'SOUTH': ('↓', 'SOUTH'), 'EAST': ('→', 'EAST'), 'WEST': ('←', 'WEST')}
        for direction, (legend, name) in direction_legends.items():
            self.canvas.create_text((direction_legends[direction][0] == '→' and 225) or
                                    (direction_legends[direction][0] == '←' and 25) or 120,
                                    (direction_legends[direction][0] == '↑' and 10) or
                                    (direction_legends[direction][0] == '↓' and 240) or 140,
                                    text=f"{legend} ({name})")

        # Draw robot
        if self.simulator.robot.is_placed:
            robot_x = self.simulator.robot.x
            robot_y = 4 - self.simulator.robot.y  # Invert y coordinate to match grid orientation
            self.canvas.create_oval(robot_x * 50 + 10, robot_y * 50 + 10, (robot_x + 1) * 50 - 10,
                                    (robot_y + 1) * 50 - 10, fill="red")
