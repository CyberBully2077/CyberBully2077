label after_school_scene:
    scene after_school_splash with fade
    "Later that afternoon..."
    
    hide after_school_splash
    show black
    play sound "audio/sound_fx/misc/busbrakes.mp3"
    show after_school1
    with fade
    "The bus pulls into Logan's stop. Hex and his sidekicks follow Logan\nas he leaves the bus."
    
    hide after_school1
    show after_school2
    with fade
    bully "Hey Logan..."

    hide after_school2
    show after_school3:
        center_image_zoom_out
    with fade
    "Hex pulls Logan's painting out of his bag."
    
    show logan_talking2:
        char_zoom_right
    logan "What do you want, Hex?"
    
    hide after_school3
    hide logan_talking2
    show ripping_painting:
        kenburns1      
    with fade
    play sound "audio/sound_fx/misc/paperrip.mp3" 
   
    "Hex rips Logan's painting before his very eyes." with vpunch

    hide ripping_painting
    show after_school4
    with fade
    logan "Hey!! Why did you do that?!"
    
    hide after_school4
    show bully_bandana3:
        char_zoom_left
    show logan_upset6:
        char_zoom_right
    with fade
    "Hex shoves Logan to the ground." with vpunch

    hide bully_bandana3
    hide logan_upset6
    show after_school5:
        kenburns1
    with fade
    bully "Oops."

    hide after_school5
    show after_school6
    with fade
    "Logan quickly gets up from the ground and runs towards his house."
    "Hex and his sidekicks follow closely behind...."
    
    hide after_school6
    show after_school7
    with fade

    menu after_school_menu:
        "Choose an action."

        "Fight Hex":
            call after_school_a
        
        "Run home":
            call after_school_b

        "Use special move!":
            call bandana   
    return

label after_school_a:
    hide after_school7
    show after_school8
    with fade
    bully "Hey, Logan! Sorry aboout your finger painting!"
    
    hide after_school8
    show after_school9
    with fade
    logan "Aaaaaah!"

    hide after_school9
    show after_school10:
        kenburns1
    "Logan throws a punch at Hex." with vpunch

    hide after_school10
    show after_school11:
        kenburns1
    with fade
    "Hex easily dodges the flimsy punch and tackles Logan to the ground." with vpunch

    hide after_school11
    show logan_upset6 zorder 1:
        char_zoom_right
    with fade
    logan "Ow!"
    show bully_bandana6:
        char_zoom_left
    "Hex begins punching and kicking Logan."
    bully "Apologize to me and maybe I'll stop... Lohgie!"

    hide bully_bandana6
    show after_school12:
        center_image_zoom_out
    show henchman2_normal1:
        char_zoom_left
    with fade
    sidekick2 "Nice one Hex. Are you recording this Strix?"

    hide logan_upset6
    show henchman1_smartphone:
        char_zoom_right
    with fade
    sidekick1 "Yeah! Hahaha!"

    "Strix is streaming to FlipFlop on his phone."
    return

label after_school_b:
    hide after_school7
    show after_school13
    with fade
    bully "Where are you going Lohgie?"

    hide after_school13
    show after_school14:
        kenburns1
    with fade
    "Hex stops Logan by grabbing his shirt and slams him into the ground." with vpunch
    bully "I told you to stop!"
    
    hide after_school14
    show after_school15:
        center_image_zoom_out
    show logan_sitting6:
        char_zoom_left
    with fade
    logan "Huff... huff..."

    hide after_school15
    hide logan_sitting6
    show after_school16:
        center_image_zoom_out
    with fade
    bully "Stop hitting yourself, Lohgie." with hpunch
    show bully_bandana4:
        char_zoom_left
    "Hex and his sidekicks take turns grabbing Logan's hands and making\nhim punch himself."

    show henchman1_smartphone:
        char_zoom_right
    with fade
    sidekick2 "I'm streaming this to FlipFlop right now. This is great hahahah!"
    
    return

label bandana:
    hide after_school7
    show after_school18
    with fade
    bully "Hey, Logan! Sorry aboout your finger painting!"
    
    hide after_school18
    show after_school19:
        kenburns1
    with fade
    "Logan lunges towards Hex and slides behind him."    
    
    hide after_school19
    show logan_lunge:
        kenburns2
    with fade
    logan "Take that!" with hpunch

    hide logan_lunge
    show after_school20:
        kenburns1
    with fade
    "Logan grabs Hex's bandana and pulls it over his eyes." with vpunch

    hide after_school20
    show after_school21
    with fade
    "Logan celebrates his momentary victory and then runs home."
    hide after_school21
    with fade
    return

label idk:

    python:
        import random
        num = random.randint(1,10)
        
        if (num % 2 == 0):
            renpy.jump('after_school_a')
        elif (num == 5):
            renpy.jump('bandana')
        else:
            renpy.jump('after_school_b')

    return