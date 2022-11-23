label lunchroom_scene:
    scene cafeteria with fade

    show logan nervous at left
    logan "(Looks around nervously)"
    logan "Why is everyone staring at me?"

    show students at right
    "The students start laughing and point at Logan" with vpunch

    show bully at right
    show sidekick1 at midright
    show sidekick2 at midright2
    bully "HAHA HE HEEHUU" with vpunch
    sidekick1 "HAHA" with vpunch
    sidekick2 "HAHA" with vpunch

    hide bully
    hide sidekick1
    hide sidekick2
    "Logan sits down at a table and checks his phone."
    logan "What the... Why is that photo on FlipFlop?!"
    logan "Hex...!"

    # jump to next scene here
    return

label lunchroom_scene_alt:
    scene cafeteria with fade
    
    show logan at left
    "Logan walks to a table holding his food tray."

    show bully sinister at right
    "Hex see Logan and sticks his foot out in front of Logan without him noticing."

    with vpunch
    logan "Ow!"

    "Logan falls and his face collides with his food tray on the ground."

    students "(Laughing)" with vpunch

    menu lunchroom_options:
        "Choose an option"

        "Shove Hex":
            logan "What's your problem man!" with vpunch
            bully "Wha... me?! Why did you push me?"
            lunchlady "Ok, that's enough you two!"
            "Hex whispers into Logan's ear."
            bully "You're dead. Just you wait."


        "Logan cleans himself up and ignores Hex":
            logan "Grr...."
    
    return    