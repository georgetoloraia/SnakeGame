import turtle
import time
import random


class Main:
    def __init__(self):
        self.window = turtle.Screen() #es tamashis ,,charcho''
        self.window.title('Snake game')
        self.window.bgcolor("#DCDCDC") #fonis feris shercheva
        self.window.setup(width=600, height=600) 
        self.window.tracer(0)

    def head(self):
        head = turtle.Turtle()
        head.shape("square")
        head.color("white")
        head.penup()
        head.goto(0, 0)
        head.direction = "stop"
        return head

    def food(self):
        food = turtle.Turtle()
        colors = random.choice(['red', 'green', 'black'])
        shapes = random.choice(['square', 'triangle', 'circle'])
        food.speed(0)
        food.shape(shapes)
        food.color(colors)
        food.penup()
        food.goto(0, 100)
        return food

    def pen(self):
        pen = turtle.Turtle()
        pen.speed(0)
        pen.shape("square")
        pen.color("white")
        pen.penup()
        pen.hideturtle()
        pen.goto(0, 250)
        pen.write("Score : 0  High Score : 0", align="center",
                  font=("Arial", 24, "bold"))
        return pen

class Asign(Main):
    def __init__(self):
        super().__init__()
        self.head = self.head()
        self.food = self.food()
        self.segments = []

        self.window.listen()
        self.window.onkeypress(self.goup, "w")
        self.window.onkeypress(self.godown, "s")
        self.window.onkeypress(self.goleft, "a")
        self.window.onkeypress(self.goright, "d")

    def goup(self):
        if self.head.direction != "down":
            self.head.direction = "up"

    def godown(self):
        if self.head.direction != "up":
            self.head.direction = "down"

    def goleft(self):
        if self.head.direction != "right":
            self.head.direction = "left"

    def goright(self):
        if self.head.direction != "left":
            self.head.direction = "right"
 
    def move(self):
        if self.head.direction == "up":
            y = self.head.ycor()
            self.head.sety(y + 20)
        if self.head.direction == "down":
            y = self.head.ycor()
            self.head.sety(y - 20)
        if self.head.direction == "left":
            x = self.head.xcor()
            self.head.setx(x - 20)
        if self.head.direction == "right":
            x = self.head.xcor()
            self.head.setx(x + 20)

class Movement(Asign):
    def __init__(self):
        super().__init__()
        self.high_score = 0
        self.score = 0  
        self.pen = self.pen()  

        while True:
            self.window.update()
            delay = 0.1
            if (
                self.head.xcor() > 290 or self.head.xcor() < -290 or
                self.head.ycor() > 290 or self.head.ycor() < -290
            ):
                time.sleep(1)
                self.head.goto(0, 0)
                self.head.direction = "stop"
                colors = random.choice(['red', 'blue', 'green'])
                shapes = random.choice(['square', 'circle'])
                for segment in self.segments:
                    segment.goto(1000, 1000)
                self.segments.clear()
                self.score = 0  # Reset score here
                self.pen.clear()  # Clear the pen object
                self.pen.write("Score : {} High Score : {} ".format(
                    self.score, self.high_score), align="center", font=("Arial", 24, "bold"))
            if self.head.distance(self.food.pos()) < 20:
                x = random.randint(-270, 270)
                y = random.randint(-270, 270)
                self.food.goto(x, y)

                new_segment = turtle.Turtle()
                new_segment.speed(0)
                new_segment.shape("square")
                new_segment.color("orange")
                new_segment.penup()
                self.segments.append(new_segment)
                delay -= 0.001
                self.score += 10
                if self.score > self.high_score:
                    self.high_score = self.score
                self.pen.clear()  
                self.pen.write("Score : {} High Score : {} ".format(
                    self.score, self.high_score), align="center", font=("Arial", 24, "bold"))

            for index in range(len(self.segments)-1, 0, -1):
                x = self.segments[index-1].xcor()
                y = self.segments[index-1].ycor()
                self.segments[index].goto(x, y)
            if len(self.segments) > 0:
                x = self.head.xcor()
                y = self.head.ycor()
                self.segments[0].goto(x, y)
            self.move()

            for segment in self.segments:
                if segment.distance(self.head) < 20:
                    time.sleep(1)
                    self.head.goto(0, 0)
                    self.head.direction = "stop"
                    for segment in self.segments:
                        segment.goto(1000, 1000)
                    self.segments.clear()

                    self.score = 0  # Reset score here
                    delay = 0.1
                    self.pen.clear() 
                    self.pen.write("Score : {} High Score : {} ".format(
                        self.score, self.high_score), align="center", font=("Arial", 24, "bold"))
            time.sleep(delay)
        self.window.mainloop()
game = Movement()
