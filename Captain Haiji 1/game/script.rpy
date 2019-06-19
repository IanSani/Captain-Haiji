# Declare character used by this game.
# name of the character.

image bg = "bg2.jpg"
image bgx = "bgx.png"
image elle = "girl.png"
image haiji = "supesule.png"
image bg2 = "backdrop1.jpg"
image bg3 = "iii.jpg"
image bg4 = "v.jpg"
image bg5 = "vii.jpg"
image bg6 = "viii.jpg"
image bg7 = "x.jpg"
image bg8 = "ii.jpg"
image intromovie = Movie(play="intromovie.ogv", mask="intromovie.ogv")


define h = Character ('Captain Haiji')

# The game starts here.

label start:
    $ renpy.movie_cutscene("intromovie.ogv")
    play music "theme.mp3"

    scene bgx
    with Fade(0.9, 0.0, 0.9)
    show elle at left
    with Fade(0.9, 0.0, 0.9)
    show haiji at right
    with Fade(0.7, 0.0, 0.7)

    h"Lets know a little about hygine"

    h"Great idea, lets goo"
    scene bg7
    with Fade(0.9, 0.0, 0.9)
    show haiji at right with moveinbottom

    h"Good hygine, Good health"

    h "Do you know to maintain good hygine you must also maintain cleanness?"
    scene bg2
    with Fade(0.9, 0.0, 0.9)

    menu:
        "Yes":
            jump iKnow

            label iKnow:

            h"Great i think we can be friends since we both value our hygine"


        "No":
            jump iDontknow


            label iDontknow:

            h"Sorry! if you don't know it means you doesn't value hygine!"
    scene bg3
    with Fade(0.9, 0.0, 0.9)
    show haiji at right with moveinleft
    menu:

        "Do you have interest in knowing little about hygine?":
                                        jump yesIdo

                                        label yesIdo:
                                            scene bg5
                                            hide haiji
                                            show haiji at left with moveintop

                                            h"well to maintain good hygine be clean, eat clean staffs, and wash hands after visiting washrooms"


        "You good, and not interested":
                                        jump iDont
                                        label iDont:

                                        h"I guess i have to stick to my hygine principle, that means we can't agree, i am sorry!"




    scene bg4
    hide haiji
    show haiji at center with moveintop
    h"What do you do first thing in the morning when you wake up"
    menu:

        "Drink warm water?":

            jump warmWater
            label warmWater:

            h"Great it cleans the stomach and keeps you ready for breakfast"

        "Take soda?":
            jump takeSoda


            label takeSoda:

            h"Oops it will just add gas to your stomach and excess sugar to body!"

    scene bg7
    with Fade(0.9, 0.0, 0.9)
    show haiji at right with moveinbottom

    h"What do you do before sleeping?"
    menu:

        "Brush your teeth?":

                        jump brushTeeth
                        label brushTeeth:

                        h"Thats great for your teeth to be strong and it also prevents infections"
        "Just relax and sleep":
                        jump justSleep


                        show haiji at right with moveinbottom
                        label justSleep:

                        h"Really, i think your teeth are in danger!"
    scene bg6
    with Fade(0.9, 0.0, 0.9)
    show haiji at center with moveinright


    # This ends the game.

    return
