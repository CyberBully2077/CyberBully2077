label art_class_scene:
    scene artroom with fade
    show art_teacher at left
    art_teacher "Good day class!"
    art_teacher "Today we will be using some older art tools of the past: \na paintbrush and paper!\nIsnt that exciting?"

    show group onlayer overlay at zoom_bottom_right
    students "Yes..."
    hide group

    art_teacher "Okay everyone! Start by..."
    "The teacher proceeds to give instructions on how to use paint with a brush."
    hide teacher

    show logan at left
    "Logan focuses on his drawing."

    show sidekick1 at right
    sidekick1 "Hey Logan, that is a cool painting!"
    logan "Thanks! I love drawing on my tablet, so I was not surprised that I really liked the old ways too."
    logan "What did you make?"
    sidekick1 "Yeah, check it out!"
    hide sidekick1
    hide logan

    show bad_painting at center
    "Strix shows Logan the details of his painting to keep Logan occupied."
    hide bad_painting

    show logan at left
    show bully at right

    "Tom sneaks up on Logan and steals his painting while he is distracted."
    play sound "bell.mp3"
    "The bell rings..." with vpunch

    hide bully
    show sidekick1 at right
    sidekick1 "Thanks for that chat. Smell you later!"
    hide sidekick1

    logan "Later!"
    "Logan turns towards his desk and realizes that his painting is gone."
    logan "They got me again... Tartar sauce..."

    if tell_no_one is False:
        jump schoolyard_scene
    else:
        jump after_school_scene

    