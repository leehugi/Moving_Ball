import random

# --------------------------------------------------------------
# ------------------------- CLASS BALL -------------------------
# --------------------------------------------------------------
class Ball:
    def __init__(self, canvas, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.canvas = canvas
        self.x_speed = self.y_speed = 3
        self.speed = 1
        self.size = 1
        self.movement = "diagonal"
        # flag move to disable unnecessary movement calls
        self.flag_move = 1
        # flag size to switch between growing or shrinking
        self.size_flag = 1
        self.ball = canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill="white")
        self.canvas.move(self.ball, random.randint(20, 300), 110)

    def start_and_stop(self, action):
        """
        Stop or start movement for all balls
        :param action: stop or start the movement
        """
        if action == "start" and self.flag_move != 1:
            self.flag_move = 1
            if self.movement == "diagonal":
                self.canvas.after(50, self.move_diagonal)
            elif self.movement == "horizontal":
                self.canvas.after(50, self.move_horizontal)
            elif self.movement == "vertical":
                self.canvas.after(50, self.move_vertical)
            elif self.movement == "inward_outward":
                self.canvas.after(50, self.move_inward_outward)
        elif action == "stop":
            self.flag_move = 0

    def move_ball(self):
        """
        Function that moves the ball to new coordinates.
        If the ball hits the walls, change movement direction.
        """
        self.canvas.move(self.ball, (self.x_speed * self.speed), (self.y_speed * self.speed))
        (leftPos, topPos, rightPos, bottomPos) = self.canvas.coords(self.ball)
        if leftPos <= 0 or rightPos >= 400:
            self.x_speed = -self.x_speed
        if topPos <= 0 or bottomPos >= 400:
            self.y_speed = -self.y_speed

    def move_diagonal(self):
        """
        Moves the balls diagonally
        """
        if self.movement == "diagonal" and self.flag_move:
            self.move_ball()
            self.canvas.after(50, self.move_diagonal)

    def move_horizontal(self):
        """
        Moves the balls horizontally
        """
        if self.movement == "horizontal" and self.flag_move:
            self.move_ball()
            self.canvas.after(50, self.move_horizontal)

    def move_vertical(self):
        """
        Moves the balls vertically
        """
        if self.movement == "vertical" and self.flag_move:
            self.move_ball()
            self.canvas.after(50, self.move_vertical)

    def move_inward_outward(self):
        """
        Moves the balls in an "inward outward" direction.
        """
        leftPos, topPos, rightPos, bottomPos = self.canvas.coords(self.ball)
        if self.movement == "inward_outward" and self.flag_move:
            if self.size_flag:
                self.change_size("larger")
            elif not self.size_flag:
                self.change_size("smaller")
            # If the ball hits a wall, change inward to outward.
            if leftPos <= 0 or rightPos >= 400 or topPos <= 0 or bottomPos >= 400:
                self.size_flag = 0
            # If the ball size reaches 1, change outward to inward.
            elif self.size == 1:
                self.size_flag = 1
            self.canvas.after(50, self.move_inward_outward)

    def change_color(self, color):
        """
        Change the ball color
        :param color: black or white
        """
        if color == "black":
            self.canvas.itemconfig(self.ball, fill='white')
        else:
            self.canvas.itemconfig(self.ball, fill='black')

    def change_speed(self, action):
        """
        Changes the balls speed
        :param action: faster or slower
        """
        if action == "faster":
            self.speed += 1
        else:
            if self.speed > 1:
                self.speed -= 1

    def change_size(self, action):
        """
        Changes the ball size
        :param action: larger or smaller
        """
        leftPos, topPos, rightPos, bottomPos = self.canvas.coords(self.ball)
        if action == "larger":
            if leftPos > 0 and rightPos < 400 and topPos > 0 and bottomPos < 400:
                self.size += 1
                self.canvas.coords(self.ball, leftPos - 1, topPos - 1, rightPos + 1, bottomPos + 1)
        else:
            if self.size > 1:
                self.size -= 1
                self.canvas.coords(self.ball, leftPos + 1, topPos + 1, rightPos - 1, bottomPos - 1)

    def change_movement(self, action):
        """
        Changes the ball's movement type
        :param action: diagonal, vertical, horizontal or inward outward
        """
        if action == "diagonal" and self.movement != "diagonal":
            self.movement = "diagonal"
            self.x_speed = 3
            self.y_speed = 3
            self.canvas.after(50, self.move_diagonal)
        elif action == "horizontal" and self.movement != "horizontal":
            self.movement = "horizontal"
            self.x_speed = 3
            self.y_speed = 0
            self.canvas.after(50, self.move_horizontal)
        elif action == "vertical" and self.movement != "vertical":
            self.movement = "vertical"
            self.x_speed = 0
            self.y_speed = 3
            self.canvas.after(50, self.move_vertical)
        elif action == "inward_outward":
            self.movement = "inward_outward"
            self.canvas.after(50, self.move_inward_outward)

    def delete_ball(self):
        """
        Delete the ball from the canvas
        """
        self.movement = ""
        self.canvas.delete(self.ball)

# --------------------------- END ------------------------------

# --------------------------------------------------------------
# --------------------------- TOOLS ----------------------------
# --------------------------------------------------------------
def change_background_color(color, canvas, ball_list):
    """
    Change the background color
    :param color: black or white
    """
    if color == "black":
        canvas.configure(bg='black')
        for ball in ball_list:
            ball.change_color("black")
    else:
        canvas.configure(bg='white')
        for ball in ball_list:
            ball.change_color("white")

def add_ball(ball_list, canvas):
    """
    Adds a ball to the list
    """
    ball = Ball(canvas, 20, 20, 50, 50)
    ball_list.append(ball)
    if len(ball_list) > 1:
        ball_list[len(ball_list) - 1].speed = ball_list[0].speed
        # set the new ball movement to none.
        ball_list[len(ball_list) - 1].movement = ""
        # find the current movement type.
        movement_type = ball_list[0].movement
        # set the current movement type to the new ball.
        ball_list[len(ball_list) - 1].change_movement(movement_type)
    return ball_list

def call_ball_func(ball_list, func_name, action):
    """
    calls the function to be executed according to the user's action
    :param ball_list: list of the balls
    :param func_name: the function to be executed
    :param action: which action to preform at the function
    """
    for ball in ball_list:
        if func_name == "speed":
            ball.change_speed(action)
        elif func_name == "size":
            ball.change_size(action)
        elif func_name == "movement":
            ball.change_movement(action)
        elif func_name == "play":
            ball.start_and_stop(action)

def remove_ball(ball_list, canvas):
    """
    Remove the last ball
    """
    if len(ball_list) > 1:
        ball_list[len(ball_list) - 1].delete_ball()
        ball_list.pop()
