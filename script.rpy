# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define res = Character("Resenfor", color= "#0084ff")
define third = Character("Third", color = "#FF0000")

image ailis = "ailis.png"


#renpy.dynamic("episode")
define episode = 1



transform testPos:
    xalign 0.0
    yalign 0.0

# The game starts here.

label start():
    if episode == 1:
        scene image "background1.png"
        res "Resenfor smells really bad"
    elif episode == 2:
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

        menu testScene: 
            "Test1"
            "A1":
                "continue"
            "A2":
                "exit"
                third "Asss exit 1"
                third "Asss exit 2"
                return

        third "continue successful"

        # This ends the game.

    return


label startEP2():
    $ episode = 2
    "Loading Episode 2"
    return