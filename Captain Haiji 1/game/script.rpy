define h = Character("Captain Haiji")


# The game starts here.

label start:

    h"Lets know a little about hygine"


    h"Good hygine, Good health"

    h "Do you know to maintain good hygine you must also maintain cleanness?"

    menu:
        "Yes":
            jump iKnow

        "No":
            jump iDontknow

    label iKnow:

        h"Great i think we can be friends since we both value our hygine"

    label iDontknow:

        h"Sorry! if you don't know it means you doesn't value hygine!"

    menu:

        "Do you have interest in knowing little about hygine?":
                                        jump yesIdo

        "You good, and not interested":
                                        jump iDont

    label yesIdo:

        h"well to maintain good hygine be clean, eat clean staffs, and wash hands after visiting washrooms"

    label iDont:

       h"I guess i have to stick to my hygine principle, that means we can't agree, i am sorry!"


    h"What do you do first thing in the morning when you wake up"
    menu:

        "Drink warm water?":

            jump warmWater
        "Take soda?":
            jump takeSoda

    label warmWater:

        h"Great it cleans the stomach and keeps you ready for breakfast"

    label takeSoda:

       h"Oops it will just add gas to your stomach and excess sugar to body!"



    h"What do you do before sleeping?"
    menu:

        "Brush your teeth?":

                        jump brushTeeth
        "Just relax and sleep":
                        jump justSleep

    label brushTeeth:

        h"Thats great for your teeth to be strong and it also prevents infections"

    label justSleep:

        h"Really, i think your teeth are in danger!  "



    # This ends the game.

    return
