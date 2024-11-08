##################################################################
# Import raylibpy and ball
import raylibpy as r
import ball
##################################################################
# Instantiate the ball
ball = ball.Ball()
# Entry point
def main():
    ##################################################################
    # Window variables
    screenWidth = 720
    screenHeight = 480
    # Ball variables
    ball.x = screenWidth / 2
    ball.y = screenHeight / 2
    ball.radius = 20
    ball.speed_x = 15
    ball.speed_y = 15
    ##################################################################
    # Set target FPS to 60
    r.set_target_fps(60)
    # Initialize window
    r.init_window(screenWidth, screenHeight, "BouncyBall")
    ##################################################################
    # GAME LOOP
    while r.window_should_close() == False:
        ##################################################################
        # UPDATE GAME
        ball.update()
        # Print the ball's current position on console for debug
        print(f"({ball.x}, {ball.y})")
        ##################################################################
        # DRAW GAME
        r.begin_drawing()
        # Draw the backgrounds
        r.clear_background(r.BLACK)
        # Draw the ball
        ball.draw(ball.x, ball.y - ball.radius / 2, ball.radius, r.YELLOW)
        # Draw the FPS on screen for debug
        r.draw_fps(10, 10)
        # End drawing
        r.end_drawing()
    ##################################################################
    # Close the window
    r.close_window()
        
if __name__ == '__main__':
    main()
