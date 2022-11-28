label art_class_scene:
    scene art_splash with fade
    "After lunch, Logan made his way to art class."
    hide art_splash
    
    show black
    show teacher1_normal1:
        teacher_zoom_left
    with fade
    art_teacher "Good day class!"
    hide teacher1_normal1
    show art1:
        center_image_zoom_out
    with fade
    art_teacher "Today we will be using some older art tools of the past."
    show teacher1_normal2:
        teacher_zoom_left
    art_teacher "A paintbrush and paper!\nIsnt that exciting?"

    show group4 with dissolve:
        group_zoom_right
    students "Yes..."
    hide group4
    hide teacher1_normal2 

    show teacher1_normal3:
        teacher_zoom_left
    show group1 onlayer overlay at group_zoom_right
    art_teacher "Okay everyone! Start by..."
    show group1 onlayer overlay at group_zoom_right
    "The teacher proceeds to give instructions on how to use paint\nwith a brush."
    hide teacher1_normal3
    hide art1

    show logan_painting:
        kenburns1
    with fade
    "Logan focuses on his drawing."
    show henchman1_normal1:
        char_zoom_left
    sidekick1 "Hey Logan, that is a cool painting!"
    hide logan_painting
    hide henchman1_normal1
    show art2
    with fade

    logan "Thanks! I love drawing on my tablet, so I was not surprised that I\nreally liked the old ways too."
    hide art2
    show logan_painting2
    with fade
    logan "Hey Strix, what did you make?"
    sidekick1 "Yeah, check it out!"
    hide logan_painting2
    show art3:
        kenburns1
    "Strix shows Logan the details of his painting to keep Logan occupied."
    hide art3
    show art4
    with fade

    "Hex sneaks up behind Logan when his back is turned......"
    hide art4
    show art6
    with fade
    "Hex steals Logan's painting and runs off with it."
    hide art6
    show art7
    with fade
    play sound "audio/sound_fx/misc/bell.mp3"
    "The bell rings..." with vpunch

    hide art7
    show art5
    sidekick1 "Thanks for that chat."
    hide art5
    show henchman1_laughing1:
        char_zoom_left
    show logan_normal2:
        char_zoom_right
    with fade
    logan "Later!"
    hide henchman1_laughing1
    hide logan_normal2
    show logan_panic1:
        kenburns2
    with fade
    "Logan turns towards his desk and realizes that his painting is gone."
    show art8
    
    logan "They got me again... Tartar sauce..."

    if tell_no_one:
        jump after_school_scene
    else:
        jump schoolyard_scene

    