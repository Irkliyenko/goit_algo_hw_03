import argparse
import turtle


def parse_args():
    parser = argparse.ArgumentParser(
        description="Draw Kohh Snowflake with specified order")
    parser.add_argument('-o', '--order', type=int, required=True,
                        help='Specify order fro Kokh snowflake')
    parser.add_argument('-s', '--size', type=int,
                        default=300, help="Specify segment's size")
    return parser.parse_args()


def koch_curve(t, order, size):
    # Base case: if order is 0, just draw a straight line
    if order == 0:
        t.forward(size)
    else:
        # If the order is greater than 0, split the line into segments and apply the Koch curve pattern
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            # Turn the turtle by the specified angle
            t.left(angle)


def main():
    # Parse and extract arguments
    args = parse_args()
    order = args.order
    size = args.size

    # Set up the turtle module
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()  # Create a turtle object to draw with
    t.speed(0)   # Set the turtle's speed to the fastest (no animation)
    t.penup()
    t.goto(-size / 2, 0)
    t.pendown()

    # Draw three sides of the Koch Snowflake
    for _ in range(3):
        koch_curve(t, order, size)  # Draw one side of the snowflake
        t.right(120)                # Rotate the turtle to start the next side

    window.mainloop()


if __name__ == "__main__":
    main()
