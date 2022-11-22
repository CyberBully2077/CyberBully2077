label after_school_scene:
    scene bus_stop with fade

    show bully at left
    "Tom pulls Logan's painting out of his bag."
    bully "Hey Logan..."

    show logan at right
    logan "Huh?"

    # TODO Play ripping paper sound effect
    "Tom rips Logan's painting before his very eyes." with vpunch

    logan "Why are you doing this to me?!"

    "Tom shoves logan to the ground." with vpunch

    bully "Oops."

    menu after_school_menu:
        "Choose an action."

        "Fight Tom":
            call after_school_a
        
        "Run away":
            call after_school_b
    return

label after_school_a:
    logan "Aaaaaah!"
    "Logan throws a punch at Tom." with vpunch
    "Tom easily dodges the flimsy punch and tackles him into the ground." with vpunch
    logan "Ow!"
    bully "Apologize to me and maybe I'll stop... Lohgie!"

    hide bully
    show sidekick2 at left
    sidekick2 "Nice one Tom. Are you recording this Strix?"
    hide sidekick2

    show sidekick1 at left
    sidekick1 "Yeah! Hahaha!"
    hide sidekick1

    "Strix is streaming to FlipFlop on his phone."
    return

label after_school_b:
    
    "Logan runs out of the bus."
    bully "Where are you going Lohgie?"

    "Tom stops Logan by grabbing his shirt and slams him into the ground." with vpunch

    bully "I told you to stop!"

    logan "Huff... huff..."

    bully "Stop hitting yourself, Lohgie."
    "Tom and his sidekicks take turns grabbing Logan's hands and making him punch himself."

    hide bully
    show sidekick2
    sidekick2 "I'm streaming this to FlipFlop right now. This is great hahahah!"

    
    return