label gym_scene:
    scene black with dissolve
    show gym_splash with fade
    "After homeroom, Logan made his way through the hallways of Neon Park \nMiddle School."

    hide gym_splash with dissolve
    show gym1_bg with dissolve
    show logan_normal3 with dissolve:
        char_zoom_left
    "Logan eventually found his way to the gymnasium."
    hide gym1_bg with dissolve
    hide logan_normal3 with dissolve

    show gym4 with dissolve:
        center_image_zoom_out
    show logan_sitting1 with dissolve:
        char_zoom_left
    "Logan sat alone in the back\nand waited for his next class to begin...."
    hide logan_sitting1 with dissolve
    hide gym4 with dissolve

    show gym5 with dissolve
    "Hex walks into the gynamnasium and sits down behind Logan\nwhen he isn't looking."
    "Hex reaches into Logan's pocket and steals his unlocked phone."
    "Hex copies all the content to his own phone and then hides it from view."

    show logan_sitting3 with dissolve:
        char_zoom_left
    show bully_sitting1 with dissolve:
        char_zoom_right
    "More students start making their way into the gymnasium."
    "After a few moments, Logan reaches for his phone in his back pocket."
    hide gym5 with dissolve
    hide logan_sitting3 with dissolve
    hide  bully_sitting1 with dissolve

    show gym1 with dissolve:
        center_image_zoom_out
    show logan_sitting6 with dissolve:
        char_zoom_left
    show bully_normal1 with dissolve:
        char_zoom_right
    logan "I can't find my phone!"
    logan "Hey! Has anyone seen my phone!?"
    hide logan_sitting6 with dissolve

    show logan_sitting2 with dissolve:
        char_zoom_left
    show bully_normal1 with dissolve:
        char_zoom_right
    bully "Yeah man, I saw someone take it."
    bully "Listen, I feel bad about flicking your ear in homeroom."
    hide bully_normal1 with dissolve
    hide logan_sitting2 with dissolve

    show logan_sitting3 with dissolve:
        char_zoom_left
    show bully_normal8 with dissolve:
        char_zoom_right
    bully "I know the guy that took it. I can get it back for you."
    bully "Meet me after class in the locker room."

    logan "Uh.., ok, thanks!"

    hide logan_sitting3 with dissolve
    hide bully_normal8 with dissolve
    "Logan waited until the end of gym class and then walked into the boys\nlocker room to meet Hex."
    return