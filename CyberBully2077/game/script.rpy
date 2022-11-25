# Python code for login/signup functionality
call splashscreen
# Declare characters used by this game. The color argument colorizes the
# name of the character.
define logan = Character("Logan Peabody")
define teacher = Character("Mrs. Smith")
define students = Character("Students")
define bully = Character("Hex")
define sidekick1 = Character("Strix")
define sidekick2 = Character("Brink")
define lunchlady = Character("Doris")
define art_teacher = Character("Ms. VanStay")

define slowdissolve = Dissolve(0.5)

transform midright:
    xalign 0.7

transform midright2:
    left

transform zoom_bottom_left:
    zoom 0.75
    xalign 0.0 yalign 1.0

transform zoom_bottom_right:
    zoom 0.7
    xalign 1.0 yalign 1.0

transform center_image_zoom_out:
    xpos 0.5 ypos 0.5 xanchor 0.5 yanchor 0.5 zoom 0.8


# The game starts here.
label start:

    call opening_crawl

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
