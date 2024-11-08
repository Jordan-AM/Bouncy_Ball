import raylibpy as r

# The Ball class
class Ball:
    def __init__(self):
        # Declare Ball's varibles
        self.x = 0
        self.y = 0
        self.radius = 0
        self.speed_x = 0
        self.speed_y = 0
    # Update the Ball's movement
    def update(self):
        if self.x + self.radius >= r.get_screen_width(): self.speed_x *= -1
        if self.x <= 0 + self.radius: self.speed_x *= -1
        if self.y + self.radius >= r.get_screen_height(): self.speed_y *= -1
        if self.y <= 0 + self.radius: self.speed_y *= -1
        self.x += self.speed_x
        self.y += self.speed_y
    # Draw the ball as a circle
    def draw(self, width, height, radius, color):
        r.draw_circle(width, height, radius, color)
