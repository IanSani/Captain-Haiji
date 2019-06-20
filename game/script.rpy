# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image bg = "bg2.jpg"
image bgx = "bgx.png"
image elle = "girl.png"
image haiji = "supesule.png"
image sid = "sid.png"
image sid2 = "sid2.png"
image bg2 = "backdrop1.jpg"
image bg3 = "iii.jpg"
image bg4 = "v.jpg"
image bg5 = "vii.jpg"
image bg6 = "viii.jpg"
image bg7 = "x.jpg"
image bg8 = "ii.jpg"
image bg9 = "city1.jpg"
image bg10 = "city2.jpg"
image bg12 = "city4.jpg"
image bg13 = "city5.jpeg"
image bg14 = "city6.jpg"
image bg15 = "city7.jpg"
image bg16 = "cityfinal.png"
image intromovie = Movie(play="intromovie.ogv", mask="intromovie.ogv")

define h = Character("Captain Hajji")
define s = Character("Captain Sid")
define i = Character("")
define e = Character("Lady Elle")
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
    $ name = renpy.input(" Whats your name?")
    $ name = name.strip()
    i "Welcome [name]"
    i"Today is your first day in superhero school. Are you ready [name]?"
    menu:
        "YES!!":
            jump yes
        "LOUDER YES!!!":
            jump yes

    label yes:
        scene bg2
        with Fade(0.9, 0.0, 0.9)
    i"Choose your hero!"
    show elle at right with moveinleft
    show haiji at left with moveinleft
    menu:
        "Captain Hajji":
            jump captainHaiji
        "Lady Elle":
            jump superElle
    label captainHaiji:
        hide haiji
        hide elle
        scene bg3
        with Fade(0.9, 0.0, 0.9)
        show haiji at right with moveinleft
        h"Hi [name]! My name is Captain Hajji, i will be your supehero trainer"
        h"Lets make you a superhero"
        h"What do we say to mummy when she buys us a new toy?"
        menu:
            "Thank you mummy!!":
                jump sayThankYou
            "Just start playing with the toy":
                jump walkAway
        label sayThankYou:
            hide haiji
            show haiji at center with moveinbottom
            h"EXCELLENT!!!Good start [name]"
            scene bg4
            hide haiji
            show haiji at center with moveintop
            h"I want something from daddy, what do i do?"
            menu:
                "Say Please!!":
                    jump sayPlease
                "Cry and shout till he gives you what you want":
                    jump screamShout
            label sayPlease:
                h"SUPER!!! You are the best side-kick"
                scene bg5
                hide haiji
                show haiji at left with moveintop
                h"I want to go over at the neighbour's for a birthday,what should i do?"
                menu:
                    "Ask for permission before i go":
                        jump askPermission
                    "Attend the birthday anyway":
                        jump attendBirthday
                label askPermission:
                    h"YIPEEE!!!!Go have fun "
                    hide haiji
                    scene bg6
                    with Fade(0.9, 0.0, 0.9)
                    show haiji at center with moveinright
                    h"Is it right to knock closed doors before entering?"
                    menu:
                        "Knock the door,then enter":
                            jump knockDoor
                        "Just enter cause i can":
                            jump enterDoor
                    label knockDoor:
                        h"WOW!!! You are amazing at this"
                        hide haiji
                        scene bg7
                        with Fade(0.9, 0.0, 0.9)
                        show haiji at right with moveinbottom
                        h"You just sneezed, what is the right thing to do?"
                        menu:
                            "Say Excuse Me":
                                jump excuseMe
                            "Continue with what you were doing":
                                jump ignore
                        label excuseMe:
                            hide haiji
                            with Fade(0.9, 0.0, 0.9)
                            scene bg8 with hpunch
                            show haiji at center with moveinbottom
                            h"BOOM!! Welcome to the team Super [name]"
                            hide haiji
                            stop music fadeout 1.0
                            play sound "sound.mp3"
                            scene bg9 with hpunch
                            with Fade(0.9, 0.0, 0.9)
                            show haiji at center with moveinbottom
                            h"Ready for the next level Super [name]"
                            h"As a hero your first mission is to save earth from aliens are you ready?"
                            hide haiji
                            menu:
                                "Yes am ready":
                                    jump level2
                                "Let me rest and try again later":
                                    jump forfeit
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
                h"Lets give you another chance"
                h"Is it right to knock closed doors before entering?"
                menu:
                    "Yes, knock then enter":
                        jump knockDoor1
                    "Just enter cause you can":
                        jump enterDoor

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
                        hide haiji
                        stop music fadeout 1.0
                        play sound "sound.mp3"
                        scene bg9 with hpunch
                        with Fade(0.9, 0.0, 0.9)
                        show haiji at center with moveinbottom
                        h"Ready for the next level Super [name]"
                        h"As a hero your first mission is to save earth from aliens are you ready?"
                        menu:
                            "Yes am ready":
                                jump level2
                            "Let me rest and try again later":
                                jump forfeit
                    label enterDoor1:
                        h"OOPS!! Sorry, sidekick you are not"
                        h"Try next time"
                        return
            label complain:
                h"Ooops!! You just got a whooping"
                h"You have failed to become a hero, try again later"
                return


    label superElle:
        hide haiji
        hide elle
        scene bg3
        with Fade(0.9, 0.0, 0.9)
        show elle at right with moveinleft
        e"Hi [name]! My name is Captain Hajji, i will be your supehero trainer"
        e"Lets make you a superhero"
        e"What do we say to mummy when she buys us a new toy?"
        menu:
            "Thank you mummy!!":
                jump sayThankYou1
            "Just start playing with the toy":
                jump walkAway1
        label sayThankYou1:
            hide elle
            show elle at center with moveinbottom
            e"EXCELLENT!!!Good start [name]"
            scene bg4
            hide elle
            show elle at center with moveintop
            e"I want something from daddy, what do i do?"
            menu:
                "Say Please!!":
                    jump sayPlease1
                "Cry and shout till he gives you what you want":
                    jump screamShout1
            label sayPlease1:
                e"SUPER!!! You are the best side-kick"
                scene bg5
                hide elle
                show elle at left with moveintop
                e"I want to go over at the neighbour's for a birthday,what should i do?"
                menu:
                    "Ask for permission before i go":
                        jump askPermission1
                    "Attend the birthday anyway":
                        jump attendBirthday1
                label askPermission1:
                    e"YIPEEE!!!!Go have fun "
                    hide elle
                    scene bg6
                    with Fade(0.9, 0.0, 0.9)
                    show elle at center with moveinright
                    e"Is it right to knock closed doors before entering?"
                    menu:
                        "Knock the door,then enter":
                            jump knockDoor4
                        "Just enter cause i can":
                            jump enterDoor4
                    label knockDoor4:
                        e"WOW!!! You are amazing at this"
                        hide elle
                        scene bg7
                        with Fade(0.9, 0.0, 0.9)
                        show elle at right with moveinbottom
                        e"You just sneezed, what is the right thing to do?"
                        menu:
                            "Say Excuse Me":
                                jump excuseMe1
                            "Continue with what you were doing":
                                jump ignore1
                        label excuseMe1:
                            hide elle
                            with Fade(0.9, 0.0, 0.9)
                            scene bg8 with hpunch
                            # scene bg8 with hpunch
                            # scene bg8 with hpunch
                            show elle at center with moveinbottom
                            e"BOOM!! Welcome to the team Super [name]"
                            hide elle
                            stop music fadeout 1.0
                            play sound "sound.mp3"
                            scene bg9 with hpunch
                            with Fade(0.9, 0.0, 0.9)
                            show elle at center with moveinbottom
                            e"Ready for the next level Super [name]"
                            e"As a hero your first mission is to save earth from aliens are you ready?"
                            hide elle
                            menu:
                                "Yes am ready":
                                    jump level2
                                "Let me rest and try again later":
                                    jump forfeit
                        label ignore1:
                            e"OOH!! OOH!! No becoming a superhero today."
                        return
                    label enterDoor4:
                        e"Ooops!!You dont want to be a villan,do you?"
                label attendBirthday1:
                    e"Ooops!! You are going to be in real trouble"
                    return
            label screamShout1:
                e"Oh No!! Daddy isn't happy with us"
                e"Lets give you another chance"
                e"Is it right to knock closed doors before entering?"
                menu:
                    "Yes, knock then enter":
                        jump knockDoor2
                    "Just enter cause you can":
                        jump enterDoor1

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
                            jump knockDoor2
                        "Just enter cause you can":
                            jump enterDoor1
                    label knockDoor2:
                        e"SUPER! you are amazing at this"
                        e"BOOM!!! You are now a superhero"
                        hide elle
                        stop music fadeout 1.0
                        play sound "sound.mp3"
                        scene bg9 with hpunch
                        with Fade(0.9, 0.0, 0.9)
                        show elle at center with moveinbottom
                        e"Ready for the next level Super [name]"
                        e"As a hero your first mission is to save earth from aliens are you ready?"
                        hide elle
                        menu:
                            "Yes am ready":
                                jump level2
                            "Let me rest and try again later":
                                jump forfeit
                    label enterDoor2:
                        e"OOPS!! Sorry, sidekick you are not"
                        e"Try next time"
                        return
            label complain1:
                e"Ooops!! You just got a whooping"
                e"You have failed to become a hero, try again later"
                return


    label level2:
        i"Welcome super [name] todays mission is critical, the fate of the world is in your hands"
        i"Help Captain Sid save the world"
        show sid at center with moveinright:
            yalign 0.5
        s"Hey there Super [name] lets start with todays mission"
        hide sid
        scene bg10
        with Fade(0.9, 0.0, 0.9)
        show sid2 at center with moveinleft:
            yalign 0.5
        s"Do you know how to maintain good hygine?"
        menu:
            "Yes i do":
                jump ido
            "No i don't":
                jump idont

        label ido:
            s"COOL!! What an amazing superhero you are"
            hide sid
            scene bg12
            with Fade(0.9, 0.0, 0.9)
            show sid at center with moveinbottom:
                yalign 0.6
            s"What do you do first thing in the morning when you wake up"
            menu:
                "Brush your teeth":
                    jump brush
                "Do everything else apart from brushing your teeth":
                    jump dontbrush

        label idont:
            hide sid
            scene bg12
            with Fade(0.9, 0.0, 0.9)
            show sid at center with moveinbottom:
                yalign 0.6
            s"Ohh!! No!! Dont worry we'll learn that"
            s"What do you do first thing in the morning when you wake up"
            menu:
                "Brush your teeth":
                    jump brush
                "Do everything else apart from brushing your teeth":
                    jump dontbrush

        label brush:
            hide sid
            scene bg13
            with Fade(0.9, 0.0, 0.9)
            show sid2 at center with moveintop:
                yalign 0.6
            s"AMAZING!!! You seem to have got a hang on these superhero stuff"
            s"What should i do after using the toilet"
            menu:
                "Wash my hands":
                    jump wash
                "Wipe my hands on my clothes":
                    jump dontwash

        label dontbrush:
            hide sid
            scene bg12
            with Fade(0.9, 0.0, 0.9)
            show sid at center with moveinbottom:
                yalign 0.6
            s"Oh!! No!! Seems the town is being overrun by aliens, lets try save it again"
            s"What should i do after using the toilet"
            menu:
                "Wash my hands":
                    jump wash
                "Wipe my hands on my clothes":
                    jump dontwash

        label wash:
            hide sid
            scene bg13
            with Fade(0.9, 0.0, 0.9)
            show sid2 at left with moveinleft:
                yalign 0.6
            s"AMAZING!! Super [name] one more task and the town is saved"
            s"What should we do to fruits before washing them"
            menu:
                "Wash them":
                    jump eat
                "Just eat it, its a fruit":
                    jump donteat

        label dontwash:
            hide sid
            scene bg13
            with Fade(0.9, 0.0, 0.9)
            show sid2 at center with moveintop:
                yalign 0.6
            s"OH!! No your town has been overrun by aliens we just lost"
            s"Try again later"
            return

        label eat:
            hide sid
            scene bg16 with hpunch
            with Fade(0.9, 0.0, 0.9)
            show sid2 at center with moveintop:
                yalign 0.6
            s"YIPEEEEE!!!! We just beat the aliens congratulations"
            return

        label donteat:
            hide sid
            scene bg16
            with Fade(0.9, 0.0, 0.9)
            show sid2 at center with moveintop:
                yalign 0.6
            s"OH!! No your town has been overrun by aliens we just lost"
            s"Try again later"
            return
