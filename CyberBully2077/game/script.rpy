# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene homeroom

    e "Home room scene aha"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # This ends the game.

    scene gym

    e "Gym class ehe"

    scene bathroom

    e "We don't have a bathroom yet oho"

    scene cafeteria

    e "Such a fancy cafeteria teehee"

    scene artroom

    e "I like to call myself an artiste"

    scene bus_stop

    e "In the neighborhood where the wild ones are"

    return
