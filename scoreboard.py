from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 15, 'normal')

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.upgrade_screen()

    def upgrade_screen(self):
        self.write(f"Score: {self.score}", move=True, align=ALIGNMENT, font=FONT)

    def upgrade_score(self):
        self.score += 1
        self.clear()
        self.goto(0, 270)
        self.upgrade_screen()

    def end_game(self):
        self.goto(0,0)
        self.color("red")
        self.write("GAME OVER", move=True, align=ALIGNMENT, font=FONT)