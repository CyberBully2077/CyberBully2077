label schoolyard_scene:

scene schoolyard_splash with fade
"After art class, Logan went to the schoolyard."
hide art_splash
show black

show schoolyard1 with fade
"Hex pulls Logan's painting out of his bag."
bully "Hey Logan..."

hide schoolyard1
show schoolyard2 with fade
"Logan is sitting. He looks up." 
logan "Huh?"

bully "Hehe"
hide schoolyard2
show ripping_painting:
    kenburns2
with fade
"Hex noisily rips Logan's artwork." with hpunch

hide ripping_painting
show schoolyard3:
    center_image_zoom_out
show logan_angry1 zorder 1:
    char_zoom_left
with fade
logan "What the hell!!"
"Logan shouts and stands up."

hide schoolyard3
hide logan_angry1
show schoolyard4
with fade

bully "Oops!"
hide schoolyard4
show schoolyard5
with fade

"Hex shoves Logan to the ground." with vpunch
hide schoolyard5
show schoolyard6
with fade

menu schoolyard_menu:
    "Choose an action."

    "Fight Hex":
        call schoolyard_a
    
    "Run away":
        call schoolyard_b

    "Special move!":
        call nannite_swarm    
return

label schoolyard_a:
    hide schoolyard6
    show logan_angry2:
        char_zoom_left
    logan "Aaaaaah!"
    show schoolyard7:
        kenburns1
    with fade
    "Logan rage screams and throws a punch at Hex." with vpunch
    hide logan_angry2
    hide schoolyard7
    show schoolyard8:
        kenburns1
    with fade
    "Hex sidesteps Logan and drops an elbow between Logan's \nshoulder blades sending him into the ground." with vpunch
    show logan_upset6 zorder 1:
        char_zoom_left
    logan "Owww..."
    hide schoolyard8
    show schoolyard9:
        center_image_zoom_out
    with fade
    bully "Haha!"
    "Hex holds him down with his foot."
    bully "Say you're sorry Loogie!"
    hide schoolyard9
    hide logan_upset6
    show schoolyard10:
        center_image_zoom_out
    with fade
    
    show henchman2_normal1:
        char_zoom_right
    sidekick2 "Nice one Hex. You get that Strix?"

    show henchman1_smartphone:
        char_zoom_left
    sidekick1 "Yeah! Hahaha!"

    "Strix is streaming to FlipFlop on his phone."
    return

label schoolyard_b:
    "Logan tries to run out of the schoolyard."
    hide schoolyard6
    show bully_laughing2:
        char_zoom_left
    show logan_running:
        char_zoom_right
    with fade
    bully "Where are you going Loogie?"
    hide logan_running
    hide bully_laughing2
    show schoolyard11 
    with fade
    "Hex runs after Logan and grabs his shirt from behind, yanking him to\nthe ground." with vpunch

    show bully_shrugging2:
        char_zoom_right
    bully "I told you to stop!"
    hide schoolyard11
    show logan_sitting6:
        char_zoom_left
    with fade
    logan "Erp..."
    
    hide bully_shrugging2
    hide logan_sitting6
    show schoolyard12
    with fade
    "Hex lunges at Logan and knocks him to the ground." with hpunch
   
    hide schoolyard12
    show schoolyard13
    with fade
    bully "Stop hitting yourself, Loogie."

    hide schoolyard13
    show schoolyard14:
        center_image_zoom_out
    with fade
    "Hex and his sidekicks take turns hitting and kicking Logan while he \nis on the ground." with vpunch

    show henchman2_normal1:
        char_zoom_left
    sidekick2 "ah, man this is so dope. Hahahaha!" with hpunch
    
    return

label nannite_swarm:
    hide schoolyard6
    show schoolyard15
    with fade
    "Logan, still dizzy from the fall, slowly gets up from the ground."

    hide schoolyard15
    show schoolyard16
    with fade
    "He dusts himself off and then lunges past Hex and his goons." with hpunch
    
    hide schoolyard16
    show logan_spraycan:
        char_zoom_left
    with fade
    logan "Eat this!"
    "Logan sprays Hex with immobilizing nannites."

    show bully_spraycan:
        char_zoom_right
    bully "My face!" with vpunch
    hide logan_spraycan
    hide bully_spraycan
    show schoolyard17:
        kenburns1
    with fade
    bully "AHHHHHHH!"
    hide schoolyard17
    show bully_ground:
        kenburns2
    "Hex falls to the ground stiff." with vpunch
    
    hide bully_ground
    show schoolyard18
    with fade
    "Strix and Brink try to catch Hex and they all end up in a pile." with hpunch
    hide schoolyard18
    show logan_running:
        kenburns2
    "Logan sprints home."

    return    

# no longer using the random generator
label idk2:

    python:
        import random
        num = random.randint(1,10)
        if (num % 2 == 0):
            renpy.jump('schoolyard_a')
        elif (num == 5):
            renpy.jump('special')    
        else:
            renpy.jump('schoolyard_b')
    return        