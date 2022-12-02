label lunchroom_scene:
    scene black with dissolve
    show cafeteria_splash with dissolve
    "Logan heads to the cafeteria for lunch."
    hide cafeteria_splash
    show cafeteria1:
        kenburns1
    with fade
    
    logan "(Looks around nervously)"
    logan "Why is everyone staring at me?"
    hide cafeteria1
    show cafeteria2:
        center_image_zoom_out
    with fade

    show group3 with vpunch:
        group_zoom_right
    "The students start laughing and pointing at Logan." with vpunch
    hide cafeteria2
    hide group3
    with fade
    
    show bully_laughing1:
        char_zoom_right
    hide logan_panic1
    show logan_panic3:
        char_zoom_left
    bully "HAHA HE HEEHUU" with vpunch
    hide bully_laughing1
    
    show henchman1_laughing1:
        char_zoom_right
    hide logan_panic3
    show logan_dizzy3:
        char_zoom_left
    sidekick1 "HAHA" with vpunch
    hide henchman1_laughing1
   
    show henchman2_normal3:
        char_zoom_right
    hide logan_dizzy3
    show logan_dizzy2:
        char_zoom_left
    sidekick2 "HAHA" with vpunch
    hide henchman2_normal3
    hide logan_dizzy2
   
    show logan_sitting6:
        kenburns2
    "Logan sits down at a table and checks his phone."
    hide logan_sitting6
    show cafeteria3:
        center_image_zoom_out
    with fade
    logan "What the... Why is that photo on FlipFlop?!"
    show logan_upset1 with dissolve:
        char_zoom_left

    logan "Hex...!"

    # jump to next scene here
    return

label lunchroom_scene_alt:
    scene black with dissolve
    show cafeteria_splash with dissolve
    "Logan heads to the cafeteria for lunch."
    hide cafeteria_splash
    show cafeteria1
    with fade
    
    "Logan enters through the double doors and he quickly scans the room."
    show bully_normal1:
        char_zoom_right
    "Hex watches Logan from the side of the room."
    
    hide cafeteria1
    hide bully_normal1
    show cafeteria5
    with fade
    "Logan walks over to the line and gets a tray of food and then looks around\nthe room for a table."
    "Logan walks towards an empty table near the back of the cafeteria."
    hide cafeteria5
    show logan_tray:
        char_zoom_right
    with fade

    "As Logan passes by, Hex sticks his foot out in front of Logan\nwithout him noticing."
    hide logan_tray
    show cafeteria6
    with fade
    with vpunch
    logan "Ow!"
    hide cafeteria6
    show cafeteria7
    with fade
    "Logan falls and his face collides with his food tray on the ground."
    hide cafeteria7
    show cafeteria8:
        kenburns1
    show group3:
        group_zoom_right
    students "(Laughing)"
    hide cafeteria8
    hide group3
    show cafeteria10
    with fade

    menu lunchroom_options:
        "Choose an option"

        "Shove Hex":
            hide cafeteria8
            show cafeteria9:
                center_image_zoom_out
            with fade
            
            logan "What's your problem man!" with vpunch
            show lunchlady1:
                teacher_zoom_left
            "Doris the lunch lady walks over to see what is going in."
            bully "Wha... me?! Why did you push me?"
            hide cafeteria9
            hide lunchlady1
            show cafeteria11
            with fade
            
            lunchlady "Ok, that's enough you two!"
            hide cafeteria11
            show cafeteria12
            with fade
            "Hex whispers into Logan's ear."
            bully "You're dead. Just you wait."

        "Logan cleans himself up and ignores Hex":
            show cafeteria9:
                center_image_zoom_out
            logan "Grr.... Why did you do that?!"
            "Logan finds a spot in the back of the cafeteria and sits alone until his \nnext class."
    return    