label homeroom_scene:
    scene black with dissolve
    show homeroom1 with dissolve:
        xpos 0 ypos 0 zoom 1.5
        linear 10 zoom 1.0
    pause(3)
    teacher "Ok class, that was the bell."
    show homeroom1 with dissolve:
        center_image_zoom_out

    show teacher2 zorder 1 at right
    teacher "Please be seated!"
    hide teacher2 with dissolve
    hide homeroom1 with dissolve
    
    show homeroom2 with dissolve:
        center_image_zoom_out
    
    show teacher2 reversed at left with slowdissolve
    teacher "Now class, we have a new student joining us today! \nCan we have a warm Neon Park Middle School welcome salute for Logan Peabody?"

    show group onlayer overlay at zoom_bottom_right
    students "(low murmurings) Hi Logan..."
    hide group
    hide homeroom2 with dissolve

    show homeroom3 with dissolve
    show teacher2 zorder 1 at right with dissolve
    teacher "Very nice class."

    show homeroom3 with dissolve: 
        center_image_zoom_out
    teacher "Logan, come up and introduce yourself. " 
    hide teacher2
    hide homeroom3 with dissolve

    show logan_normal1 zorder 1 at right with dissolve:
        zoom 0.8
    logan "uh... hi......my name is Logan....uhm...yeah... "
    window hide
    show homeroom4 zorder 0 with dissolve

    show bully laugh at left with dissolve
    bully "(snorts and snickers)" with vpunch
    hide logan_normal1 with dissolve
    show logan dizzy2 at right:
        zoom 0.8
    window hide
    pause(2)
    hide bully normal with dissolve
    hide logan dizzy2 with dissolve
    hide homeroom4 with dissolve
    
    show homeroom5 with dissolve
    show logan dizzy3 zorder 1 at right with dissolve:
        zoom 0.8
    teacher "That's very nice dear... maybe we will work on \nour oratory skills a bit more."
    teacher "Please take the open seat in front of Hex."
    hide logan dizzy3 with dissolve
    hide homeroom5 with dissolve

    show homeroom6 with dissolve
    bully "Hey class noob. Nice haircut."
    "Mrs Smith turns her attention to the blackboard"
    hide homeroom6 with dissolve

    show homeroom7 with dissolve:
        center_image_zoom_out
    pause(2)
    teacher "Now class, we are going to start with reviewing what \nwe did in the last class, the Pythagorean theorem."
    hide homeroom7 with dissolve

    show ear flick1 with dissolve
    "While Mrs. Smith isn't looking, Hex gets out of his seat \nand flicks Logan's ear." with vpunch
    logan "....!!!!!!"
    pause(1)
    hide ear flick1 with dissolve

    show ear flick2 with dissolve
    "Logan sat quietly until the end of class..."
    pause(2)
    hide ear flick2 with dissolve
    
    show homeroom8 with dissolve
    teacher "Ok class, next week..."
    hide homeroom8 with dissolve

    show homeroom8 with dissolve:
        center_image_zoom_out
    "The teacher starts droning on about weekly events in homeroom"
    show logan normal at right with dissolve:
        zoom 0.8
    "Logan zones out and starts drawing on his tablet."
    hide logan normal with dissolve
    return