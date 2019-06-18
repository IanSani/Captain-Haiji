# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image bg = "bg2.jpg"
image elle = "girl.png"
image haiji = "supesule.png"

define h = Character("Captain Haiji")
define i = Character("Welcome Superhero in training")
define e = Character("Lady Elle")
# The game starts here.

label start:
    play music "theme.mp3"
    scene bg
    with Fade(0.9, 0.0, 0.9)
    show elle at left
    with Fade(0.9, 0.0, 0.9)
    show haiji at right
    with Fade(0.7, 0.0, 0.7)
    i"Today we are going to try save Manners-land. Are you ready?"
    menu:
        "Yes!!":
            jump yes
        "Louder YES!!!":
            jump yes

    label yes:
    i"Choose your hero!"
    menu:
        "Captain Haiji":
            jump captainHaiji
        "Lady Elle":
            jump superElle
    label captainHaiji:
        h"Hey there!! Ready to save the world!!"
        h"What do we say to mummy when she buys us a new toy?"
        menu:
            "Thank you mummy!!":
                jump sayThankYou
            "Just start playing with the toy":
                jump walkAway
        label sayThankYou:
            h"Excellent kiddo, one step closer to saving the world"
            h"I want something from daddy, what do i do?"
            menu:
                "Say Please!!":
                    jump sayPlease
                "Cry and shout till he gives you what you want":
                    jump screamShout
            label sayPlease:
                h"Super!!! You are the best side-kick"
                h"I want to go over at the neighbour's for a birthday,what should i tell an adult?"
                menu:
                    "Ask Mummy for permission":
                        jump askPermission
                    "Attend the birthday anyway":
                        jump attendBirthday
                label askPermission:
                    h"Perfect!!!!Go have fun "
                    h"Is it right to knock closed doors before entering?"
                    menu:
                        "Knock the door,then enter":
                            jump knockDoor
                        "Just enter cause i can":
                            jump enterDoor
                    label knockDoor:
                        h"SUPER! you are amazing at this"
                        h"You just sneezed, what is the right thing to do?"
                        menu:
                            "Say Excuse Me":
                                jump excuseMe
                            "Continue with what you were doing":
                                jump ignore
                        label excuseMe:
                            h"BOOM!! You are officially a superhero"
                            return
                        label ignore:
                            h"OOH!! OOH!! No becoming a superhero today."
                        return
                    label enterDoor:
                        h"Ooops!!You dont want to be a villan,do you?"
                label attendBirthday:
                    h"Ooops!! You are going to be in real trouble"
                    return
            label screamShout:
                h"Oh No!! Daddy isn't happy with us"
                return
        label walkAway:
            h"OOPS!! Mummy just took away the toy"
            h"What should we do now?"
            menu:
                "Tell mummy sorry and say thank you for the toy":
                    jump sorryMummy
                "Just shrug and complain that mummy is always a meanie":
                    jump complain
            label sorryMummy:
                h"PERFECT!!!! Mummy just gave you your toy back,the world is safe once again"
                h"You just stepped on your classmates leg, what do you say to him?"
                menu:
                    "Tell him sorry":
                        jump saySorry
                    "Ignore him":
                        jump ignore
                label saySorry:
                    h"PERFECT!! You are the best "
                    h"Is it right to knock closed doors before entering?"
                    menu:
                        "Yes, knock then enter":
                            jump knockDoor1
                        "Just enter cause you can":
                            jump enterDoor
                    label knockDoor1:
                        h"SUPER! you are amazing at this"
                        h"BOOM!!! You are now a superhero"
                    label enterDoor1:
                        h"OOPS!! Sorry, sidekick you are not"
                        h"Try next time"
                        return
                # return
            label complain:
                h"Ooops!! You just got a whooping"
                h"You have failed to become a hero, try again later"
                return


    label superElle:
        e"Hey there!! Ready to save the world!!"
        e"What do we say to mummy when she buys us a new toy?"
        menu:
            "Thank you mummy!!":
                jump sayThankYou1
            "Just start playing with the toy":
                jump walkAway1
        label sayThankYou1:
            e"Excellent kiddo, one step closer to saving the world"
            e"I want something from daddy, what do i do?"
            menu:
                "Say Please!!":
                    jump sayPlease1
                "Cry and shout till he gives you what you want":
                    jump screamShout1
            label sayPlease1:
                e"Super!!! You are the best side-kick"
                e"I want to go over at the neighbour's for a birthday,what should i tell an adult?"
                menu:
                    "Ask Mummy for permission":
                        jump askPermission1
                    "Attend the birthday anyway":
                        jump attendBirthday1
                label askPermission1:
                    e"Perfect!!!!Go have fun "
                    e"Is it right to knock closed doors before entering?"
                    menu:
                        "Knock the door,then enter":
                            jump knockDoor2
                        "Just enter cause i can":
                            jump enterDoor2
                    label knockDoor2:
                        e"SUPER! you are amazing at this"
                        e"You just sneezed, what is the right thing to do?"
                        menu:
                            "Say Excuse Me":
                                jump excuseMe1
                            "Continue with what you were doing":
                                jump ignore1
                        label excuseMe1:
                            e"BOOM!! You are officially a superhero"
                            return
                        label ignore1:
                            e"OOH!! OOH!! No becoming a superhero today."
                        return
                    label enterDoor2:
                        e"Ooops!!You dont want to be a villan,do you?"
                label attendBirthday1:
                    e"Ooops!! You are going to be in real trouble"
                    return
            label screamShout1:
                e"Oh No!! Daddy isn't happy with us"
                return
        label walkAway1:
            e"OOPS!! Mummy just took away the toy"
            e"What should we do now?"
            menu:
                "Tell mummy sorry and say thank you for the toy":
                    jump sorryMummy1
                "Just shrug and complain that mummy is always a meanie":
                    jump complain1
            label sorryMummy1:
                e"PERFECT!!!! Mummy just gave you your toy back,the world is safe once again"
                e"You just stepped on your classmates leg, what do you say to him?"
                menu:
                    "Tell him sorry":
                        jump saySorry1
                    "Ignore him":
                        jump ignore1
                label saySorry1:
                    e"PERFECT!! You are the best "
                    e"Is it right to knock closed doors before entering?"
                    menu:
                        "Yes, knock then enter":
                            jump knockDoor3
                        "Just enter cause you can":
                            jump enterDoor3
                    label knockDoor3:
                        e"SUPER! you are amazing at this"
                        e"BOOM!!! You are now a superhero"
                    label enterDoor3:
                        e"OOPS!! Sorry, sidekick you are not"
                        e"Try next time"
                        return
                return
            label complain1:
                e"Ooops!! You just got a whooping"
                e"You have failed to become a hero, try again later"
                return
