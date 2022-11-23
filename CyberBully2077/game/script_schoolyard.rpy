label schoolyard_scene:

scene schoolyard with fade

show bully at right
"Hex pulls Logan's painting out of his bag."
bully "Hey Logan..."

show logan at left
"Logan is sitting, looks up" 
logan "Huh?"

bully "Hehe"
"Noisely rips Logan's artwork" with hpunch

logan "What the hell!!"
"Logan shouts and stands up"

bully "oops"
"Shoves Logan to the ground" with vpunch

menu schoolyard_menu:
    "Choose an action."

    "Fight Hex":
        call schoolyard_a
    
    "Run away":
        call schoolyard_b

    "I don't know!":
        call idk2    
return

label schoolyard_a:
    logan "Aaaaaah!"
    "Logan rage screams and throws a punch at Hex." with vpunch
    "Hex sidesteps Logan and drops an elbow between Logan's \nshoulder blades sending him into the ground." with vpunch
    logan "Owww..."
    bully "Haha"
    "Hex holds him down with his foot"
    bully "Say your sorry Loogie!"
    
    show sidekick2 at left
    sidekick2 "Nice one Hex, you get that Strix?"
    hide sidekick2

    show sidekick1 at left
    sidekick1 "Yeah! Hahaha!"
    hide sidekick1

    "Strix is streaming to FlipFlop on his phone."
    return

label schoolyard_b:
    
    "Logan runs out of the schoolyard."
    bully "Where are you going Loogie?"

    "Hex runs after Logan and grabs his shirt \nfrom behind, yanking him to\nthe ground." with vpunch

    bully "I told you to stop!"

    logan "erp..."
    "Logan is choked and crashes to ground" with hpunch

    bully "Stop hitting yourself, Loogie."
    "Hex and his sidekicks take turns hitting Logan \nwith his own hands and backpack." with vpunch

    hide bully
    show sidekick2
    sidekick2 "ah, man this is so dope. Hahahaha!"
    
    return

label special:

    "Logan lunges past Hex and his goons and yells"
    logan "Eat this!"
    "Logan sprays Hex with immobilizing nannites"
    bully "erpp..."
    "Hex falls to the ground stiff" with vpunch
    "Strix and Brink try to catch Hex and the all end up in a pile" with hpunch
    sidekick1 "oof"
    sidekick2 "oww"
    "Logan sprints home."

    return    

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