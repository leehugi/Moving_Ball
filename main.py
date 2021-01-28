from tkinter import *
import tools

def main():
    # initialize root window and canvas
    root = Tk()
    root.title("Moving Ball")
    root.resizable(False, False)
    canvas = Canvas(root, width=400, height=400, bg="black")
    canvas.pack()

    # create a ball list
    ball_list = []
    ball_list = tools.add_ball(ball_list, canvas)

    #-------- Menu bar --------
    menu_bar = Menu(root)
    # background
    background = Menu(menu_bar, tearoff=False)
    background.add_command(label="Black", command=lambda: tools.change_background_color("black", canvas, ball_list))
    background.add_command(label="White", command=lambda: tools.change_background_color("white", canvas, ball_list))
    menu_bar.add_cascade(label="Background", menu=background)
    # speed
    speed = Menu(menu_bar, tearoff=False)
    speed.add_command(label="Faster", command=lambda: tools.call_ball_func(ball_list, "speed", "faster"))
    speed.add_command(label="Slower", command=lambda: tools.call_ball_func(ball_list, "speed", "slower"))
    menu_bar.add_cascade(label="Speed", menu=speed)
    # size
    size = Menu(menu_bar, tearoff=False)
    size.add_command(label="Larger", command=lambda: tools.call_ball_func(ball_list, "size", "larger"))
    size.add_command(label="Smaller", command=lambda: tools.call_ball_func(ball_list, "size", "smaller"))
    menu_bar.add_cascade(label="Size", menu=size)
    # movement
    movement = Menu(menu_bar, tearoff=False)
    movement.add_command(label="Diagonal", command=lambda: tools.call_ball_func(ball_list, "movement", "diagonal"))
    movement.add_command(label="Horizontal", command=lambda: tools.call_ball_func(ball_list, "movement", "horizontal"))
    movement.add_command(label="Vertical", command=lambda: tools.call_ball_func(ball_list, "movement", "vertical"))
    movement.add_command(label="Inward Outward", command=lambda: tools.call_ball_func(ball_list, "movement",
                                                                                      "inward_outward"))
    menu_bar.add_cascade(label="Movement", menu=movement)
    # stop and play
    play = Menu(menu_bar, tearoff=False)
    play.add_command(label="Start", command=lambda: tools.call_ball_func(ball_list, "play", "start"))
    play.add_command(label="Stop", command=lambda: tools.call_ball_func(ball_list, "play", "stop"))
    menu_bar.add_cascade(label="Play", menu=play)
    # add balls
    add_balls = Menu(menu_bar, tearoff=False)
    add_balls.add_command(label="Add", command=lambda: tools.add_ball(ball_list, canvas))
    add_balls.add_command(label="Remove", command=lambda: tools.remove_ball(ball_list, canvas))
    menu_bar.add_cascade(label="Add Ball", menu=add_balls)

    root.config(menu=menu_bar)
    # ------- End Menu -------

    # moving the ball
    ball_list[0].move_diagonal()

    root.mainloop()


if __name__ == "__main__":
    main()
