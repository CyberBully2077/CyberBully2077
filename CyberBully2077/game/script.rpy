# Python code for login/signup functionality
# call splashscreen

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define logan = Character("Logan Peabody")
define art_teacher = Character("Mr. VanStay")
define teacher = Character("Mrs. Smith")
define lunchlady = Character("Doris")
define students = Character("Students")
define bully = Character("Hex")
define sidekick1 = Character("Strix")
define sidekick2 = Character("Brink")

# transforms
transform midright:
    xalign 0.7

transform midright2:
    left

transform center_image_zoom_out:
    xpos 0.5 ypos 0.5 xanchor 0.5 yanchor 0.5 zoom 0.8

# teachers zoom out on right and left side of screen
transform teacher_zoom_right:
    zoom 0.4
    xalign 1.0 yalign 1.0

transform teacher_zoom_left:
    xzoom -1.0
    zoom 0.4
    xalign 0 yalign 1.0

# students zoom out on right and left side of screen
transform char_zoom_right:
    zoom 0.3
    xalign 1.0 yalign 1.0

transform char_zoom_left:
    xzoom -1.0
    zoom 0.3
    xalign 0 yalign 1.0

# group zoom out
transform group_zoom_right:
    zoom 0.7
    xalign 1.0 yalign 1.0

transform group_zoom_left:
    xzoom -1.0
    zoom 0.7
    xalign 1.0 yalign 1.0
    
define slowdissolve = Dissolve(0.5)

transform kenburns1:
    subpixel True
    truecenter
    zoom 1.5 #adjust as required for initial zoom level 
    ease 3.0 zoom 1

transform kenburns2:
    subpixel True
    truecenter
    zoom .75 #adjust as required for initial zoom level 
    ease 3.0 zoom .25


# The game starts here.
label start:

    #call opening_crawl

    call homeroom_scene

    call gym_scene
    
    call bathroom_scene

    call art_class_scene

    call resources_scene
    
    return

label opening_crawl:
    scene crawl
    with slowdissolve
    pause 18.0
    
    scene bg black
    show black
    with slowdissolve
    return
