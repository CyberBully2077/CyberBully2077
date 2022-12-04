label homeroom_scene:
    play sound "audio/sound_fx/homeroom/start.mp3"
    scene homeroom_splash with dissolve
    "Logan finds his homeroom class and waits for the bell to ring...."
    
    scene black with dissolve
    show homeroom1 with dissolve:
        kenburns1
    pause(3)
    play sound "audio/sound_fx/misc/bell.mp3"
    "The bell rings..." with vpunch
    teacher "Ok class, that was the bell."
    show homeroom1 with dissolve:
        center_image_zoom_out

    show smith_normal1 zorder 1 at right:
        teacher_zoom_right
    teacher "Please be seated!"
    hide smith_normal1 with dissolve
    hide homeroom1 with dissolve
    
    show homeroom2 with dissolve:
        center_image_zoom_out
    
    show smith_normal1 with slowdissolve:
        teacher_zoom_left
    teacher "Now class, we have a new student joining us today! \nCan we have a warm Neon Park Middle School welcome salute for Logan Peabody?"
    show group1 onlayer overlay at group_zoom_right
    
    students "(low murmurings) Hi Logan..."
    hide homeroom2 with dissolve
    hide smith_normal1 with dissolve

    show homeroom3 with dissolve
    show smith_normal1 with dissolve:
        teacher_zoom_right
    teacher "Very nice class."

    show homeroom3 with dissolve: 
        center_image_zoom_out
    teacher "Logan, come up and introduce yourself. " 
    hide smith_normal1 with dissolve
    hide homeroom3 with dissolve

    show logan_normal1 zorder 1 at right with dissolve:
        char_zoom_right
    logan "uh... hi......my name is Logan....uhm...yeah... "
    window hide
    show homeroom4 zorder 0 with dissolve:
        center_image_zoom_out

    show bully_laughing1 with dissolve:
        char_zoom_left
    bully "(snorts and snickers)" with vpunch
    hide logan_normal1 with dissolve
    show logan_dizzy1 at right:
        char_zoom_right
    window hide
    pause(2)
    hide bully_laughing1 with dissolve
    hide logan_dizzy1 with dissolve
    hide homeroom4 with dissolve
    
    show homeroom5 with dissolve
    show logan_dizzy2 with dissolve:
        char_zoom_right
    teacher "That's very nice dear... maybe we will work on \nour oratory skills a bit more."
    teacher "Please take the open seat in front of Hex."
    hide logan_dizzy2 with dissolve
    hide homeroom5 with dissolve

    show homeroom6 with dissolve:
        center_image_zoom_out
    bully "Hey class noob. Nice haircut."
    "Mrs Smith turns her attention to the blackboard."
    hide homeroom6 with dissolve

    show ear_flick1 with dissolve:
        center_image_zoom_out
    pause(2)
    show teacher2_normal1 with dissolve:
        teacher_zoom_left
    teacher "Now class, we are going to start with reviewing what \nwe did in the last class, the Pythagorean theorem."
    hide ear_flick1 with dissolve
    hide teacher2_normal1 with slowdissolve

    show ear_flick2 with dissolve:
        center_image_zoom_out
    play sound "audio/sound_fx/homeroom/earflick.mp3"    
    "While Mrs. Smith isn't looking, Hex gets out of his seat \nand flicks Logan's ear." with vpunch
    logan "....!!!!!!"
    pause(1)
    hide ear_flick2 with dissolve

    show ear_flick3 with dissolve:
        center_image_zoom_out
    "Logan tries to ignore Hex and sits quietly until the end of class..."
    pause(2)
    hide ear_flick3 with dissolve
    
    show homeroom8 with dissolve
    show teacher2_normal3 with dissolve:
        teacher_zoom_right
    teacher "Ok class, next week..."
    hide homeroom8 with dissolve
    hide teacher2_normal3 with dissolve

    show homeroom9 with dissolve:
        center_image_zoom_out
    "The teacher starts droning on about weekly events in homeroom."
    hide homeroom9 with dissolve
    show logan_normal3 with dissolve:
        kenburns2
    "Logan zones out and starts drawing on his tablet.\nHe is thinking about the rest of the day he has in front him."
    pause(5)
    return