# Create scoreboard.py
# Create a scoreboard class 
    # Inherits from the turtle class 
    # scoreboard is a turtle that knows how to keep track of the score and how to display it 
    
    # Write method 
    # Clear method - to clear the writing everytime you update the score 

from turtle import Turtle
FONT = ("Courier New", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("PaleTurquoise")
        self.penup()
        self.setposition(-40, 260)
        self.hideturtle()
        # Run track_score to show initial score on constructor
        self.score = 0
        self.track_score()
        
    def track_score(self):
        self.write(f"Score: {self.score}", font=FONT)
        self.score += 1

    def clear_score(self):
        self.clear()
    
    def game_over(self):
        self.setposition(0,0)
        self.write("GAME OVER", align = "center", font=FONT,)
        