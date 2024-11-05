# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define res = Character("Resenfor", color= "#0084ff")
define third = Character("Third", color = "#FF0000")

image ailis = "ailis.png"

transform testPos:
    xalign 0.0
    yalign 0.0

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene image "background1.png"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show ailis at center

    # These display lines of dialogue.

    res "Dad is that you?"

    third "You thats right son."

    # This ends the game.

    return
