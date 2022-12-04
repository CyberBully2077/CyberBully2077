label bathroom_scene:
    scene black with fade
    play sound "audio/sound_fx/bathroom/bath start.mp3"
    show bathroom_splash with fade
    pause(3)
    hide bathroom_splash with fade

    show bathroom1_bg
    "After the bell rang, Logan walked to the boys bathroom near the\ngymansium to look for hex"
    show logan_normal3:
        char_zoom_left
    show group2 zorder 1:
        group_zoom_right
    with fade
    
    "When Logan walked in, Hex and his sidekicks were near the back of\nthe bathroom by the stalls."
    pause(1)
    hide group2
    hide logan_normal3 
    hide bathroom1_bg
    with fade
    
    show bathroom1 with fade
    logan "Hey Hex, you got my phone back!"
    hide bathroom1 with fade

    show bathroom2 with fade:
        center_image_zoom_out

    show logan_talking2:
        char_zoom_left
    show bully_smartphone2:
        char_zoom_right
    with dissolve
    bully "(laughs) Yeah, check it out!"
    hide logan_talking2
    hide bully_smartphone2
    hide bathroom2
    with fade
    
    show bully_smartphone4 with dissolve:
        char_zoom_right
    show logan_angry1 with dissolve:
        char_zoom_left
    "Hex holds up the phone and shows Logan a screen of Logan's\npersonal pictures."
    show phone_and_hand with fade:
        kenburns2
    bully "Dork!"
    hide logan_angry1
    hide bully_smartphone4
    hide phone_and_hand
    with fade
    
    show bathroom6 with fade:
    logan "Give me that!" with hpunch
    hide bathroom6 with fade

    "Hex opens the bathroom stall and walks over to the toilet."
    show bathroom3 with dissolve
    bully "Oops!"
    hide bathroom3 with dissolve
    play sound "audio/sound_fx/bathroom/drop.mp3"
    "Hex drops Logan's phone into the toilet and runs out laughing with\nhis sidekicks." with vpunch
    show bathroom4 with dissolve
    bully "HAHAHU HU HEE HEE!"
    hide bathroom4 with dissolve

    show logan_smartphone3 with dissolve:
        char_zoom_right

    show logan_upset5 with dissolve:
        char_zoom_left
    $ tell_no_one = True
    menu bathroom_menu:
        "Choose an action"

        "Retrieve the phone and tell no one.":
            $ tell_no_one = True
        
        "Retrieve the phone and tell the homeroom teacher.":
            $ tell_no_one = False
    hide logan_smartphone3 with dissolve
    hide logan_upset5 with dissolve
    show bathroom5 with dissolve
    logan "(What a jerk...)"
    logan "(Thank God the toilet was empty!)"

    "Logan washes and dries his phone."
    hide logan

    if tell_no_one:
        jump lunchroom_scene
    else:

        "Logan storms out of the bathroom and runs to homeroom."
        scene homeroom
        show black
        with fade

        show homeroom10:
            center_image_zoom_out
        with fade
        "Logan walks into his homeroom class and sees Mrs. Smith\nstraightening up the room."
        show logan_normal1 with dissolve:
            char_zoom_right
        logan "Mrs. Smith?"
        teacher "Yes...uh.. Logan! What can I do for you?"
        logan "I have an issue with Hex. He seems to be picking on me."
        hide homeroom10
        show teacher2_normal1:
            teacher_zoom_left
        with fade
        
        teacher "Oh, nonsense - you just arrived here honey! I don't think anyone\nwould have any problems with you yet!"
        hide logan_normal1
        hide teacher2_normal1
        with fade

        show homeroom11 with fade
        logan "He stole my phone and dropped it in the toilet!"
        hide homeroom11
        show homeroom12
        with fade
        teacher "I see you have your phone and it is working, is it not?"
        logan "Yes, but..."
        play sound "audio/sound_fx/misc/bell.mp3"
        hide homeroom12

        "The bell rings..." with vpunch
        show homeroom13 with fade
        "Mrs. Smith cuts off Logan before he can tell her what happened."
        teacher "Ooh! Lunchtime! You better hurry so you are not late!"
        show logan_talking4:
            char_zoom_right
        hide teacher2_normal2
        hide homeroom13
        with fade
        logan "(Sighs)" with hpunch
        jump lunchroom_scene_alt