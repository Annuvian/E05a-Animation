"""
This simple animation example shows how to move an item with the keyboard.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.move_keyboard
"""

import arcade
# Sets scren width and height
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
# Sets game title
SCREEN_TITLE = "Move Keyboard Example"
# Sets the movement speed of the ball
MOVEMENT_SPEED = 3

# Defines the Ball object
class Ball:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):

        # Take the parameters of the init function above, and create instance variables out of them.
        # Sets the x position
        self.position_x = position_x
        # Sets the y position
        self.position_y = position_y
        # Sets the change in x
        self.change_x = change_x
        # Sets the change in y
        self.change_y = change_y
        # Sets the radius
        self.radius = radius
        # Sets the color
        self.color = color

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)

    def update(self):
        # Move the ball
        # Sets the new y position equal to the previous value + the change in y
        self.position_y += self.change_y
        # Sets new x position equal to the previous value + the change in x
        self.position_x += self.change_x

        # See if the ball hit the edge of the screen. If so, change direction
        # Stops the ball from going off the left side of the screen
        if self.position_x < self.radius:
            self.position_x = self.radius
        # Stops the ball from going off the right side of the screen.
        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius
        # Stops the ball from going off the bottom of the screen.
        if self.position_y < self.radius:
            self.position_y = self.radius
        # Stops the ball from going off the top of the screen.
        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        # Sets the background color
        arcade.set_background_color(arcade.color.ASH_GREY)

        # Create our ball
        self.ball = Ball(50, 50, 0, 0, 15, arcade.color.AUBURN)

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        self.ball.draw()

    def update(self, delta_time):
        self.ball.update()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        # ball moves left according to the movement speed when the left arrow key is pressed.
        if key == arcade.key.LEFT:
            self.ball.change_x = -MOVEMENT_SPEED
        # ball moves right according to the movement speed when the right arrow key is pressed.
        elif key == arcade.key.RIGHT:
            self.ball.change_x = MOVEMENT_SPEED
        # ball moves up according to the movement speed when the up arrow key is pressed.
        elif key == arcade.key.UP:
            self.ball.change_y = MOVEMENT_SPEED
        # ball moves down according to the movement speed when the down arrow key is pressed.
        elif key == arcade.key.DOWN:
            self.ball.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        # ball stops moving when key is released.
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.ball.change_x = 0
        # ball stops moving when key is released.
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.ball.change_y = 0

# Runs the game
def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()