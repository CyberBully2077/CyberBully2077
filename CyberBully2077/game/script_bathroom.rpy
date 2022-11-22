label bathroom_scene:
    scene bathroom with fade

    show logan at left
    logan "Hey Tom, you got my phone back!"

    show bully at right

    bully "(laughs) Yeah, check it out!"
    "Tom shows screen of Logan's personal pictures"
    bully " Dork!"

    logan "Give me that!"

    bully "Oops!"

    "Tom drops Logan's phone into the toilet and runs off." with vpunch

    hide bully
    bully "HAHAHU HU HEE HEE!"

    $ tell_no_one = True
    menu bathroom_menu:
        "Choose an action:"

        "Retrieve the phone and tell no one.":
            $ tell_no_one = True
        
        "Retrieve the phone and tell the homeroom teacher.":
            $ tell_no_one = False
    
    logan "(What a jerk...)"
    logan "(Thank God the toilet was empty!)"

    "Logan washes and dries his phone."
    hide logan

    if tell_no_one:
        jump lunchroom_scene
    else:

        "Logan storms out of the bathroom and runs to homeroom"
        scene homeroom with fade

        show logan at right
        show teacher2 at left
        logan "Mrs. Smith?"
        teacher "Yes...uh.. Logan! What can I do for you?"
        logan "I have an issue with Tom. He seems to be picking on me."
        teacher "Oh, nonsense - you just arrived here honey! I don't think anyone would have any problems with you yet!"
        logan "He stole my phone and dropped it in the toilet!"
        teacher "I see you have your phone and it is working, is it not?"
        logan "Yes, but..."
        play sound "bell.mp3"
        "The bell rings..." with vpunch
        teacher "Ooh! Lunchtime! You better hurry so you are not late!"
        hide teacher2
        logan "(Sighs)"
        jump lunchroom_scene_alt