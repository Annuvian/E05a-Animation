"""
This simple animation example shows how to move an item with the mouse, and
handle mouse clicks.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.move_mouse
"""
#imports the arcade module
import arcade
# Sets width and height of the game screen.
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
# Sets the title of the game screen.
SCREEN_TITLE = "Move Mouse Example"

# Defines the Ball object
class Ball:
    def __init__(self, position_x, position_y, radius, color):

        # Take the parameters of the init function above, and create instance variables out of them.
        # Sets the x position
        self.position_x = position_x
        # Sets the y position
        self.position_y = position_y
        # Sets the radius
        self.radius = radius
        # Sets the color
        self.color = color

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        # Sets the game background
        arcade.set_background_color(arcade.color.ASH_GREY)

        # Create our ball
        self.ball = Ball(50, 50, 15, arcade.color.AUBURN)

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        self.ball.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects. Happens approximately 60 times per second."""
        # Moves the ball to the mouse x position
        self.ball.position_x = x
        # Moves the ball to the mouse y position
        self.ball.position_y = y

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        """
        # Displays text when a button is pressed telling which button is clicked.
        print(f"You clicked button number: {button}")
        # If the left mouse button is clicked, the ball color changes to black
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.ball.color = arcade.color.BLACK

    def on_mouse_release(self, x, y, button, modifiers):
        """
        Called when a user releases a mouse button.
        """
        # If the left mouse button is released, it changes the color of the ball to auburn.
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.ball.color = arcade.color.AUBURN

# This is what runs the game, it opens the window and runs the arcade module.
def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()