##################################################################
# Import raylibpy and ball
import raylibpy as r
import ball

##################################################################
# Instantiate the ball
ball = ball.Ball()

# Window and variables setup
def main():
    ##################################################################
    # Window variables
    screenWidth = 720
    screenHeight = 480
    # Ball variables
    ball.x = screenWidth / 2
    ball.y = screenHeight / 2
    ball.radius = 20
    ball.speed_x = 300
    ball.speed_y = 300
    ##################################################################
    # Set target FPS to 60
    r.set_target_fps(60)
    # Initialize window
    r.init_window(screenWidth, screenHeight, "BouncyBall")

##################################################################
# GAME LOOP
def gameLoop():
    while r.window_should_close() == False:
        ##################################################################
        # UPDATE GAME
        dt = r.get_frame_time()
        ball.update(dt)
        # Print the ball's current position on console for debug
        print(f"({ball.x}, {ball.y})")
        ##################################################################
        # DRAW GAME
        r.begin_drawing()
        # Draw the backgrounds
        r.clear_background(r.BLACK)
        # Draw the ball
        ball.draw(ball.x, ball.y - ball.radius / 2, ball.radius, r.BLUE)
        # Draw the FPS on screen for debug
        r.draw_fps(10, 10)
        # End drawing
        r.end_drawing()
    # Close the window
    r.close_window()

if __name__ == '__main__':
    main()
    gameLoop()
