label credit:
    show credits with fade
    $ renpy.pause(2)
    screen credits_screen:
        frame:
            background "credits.jpg"
            text "{cps=0.5}{color=#000}{size=+30}Credits{/size}{/color}{/cps}" xalign 0.3 yalign 0.3
        

    #this is better done by using a video of text being printed
    #to the book instead of trying to do it in renpy and then
    #simply playing the video instead.
        
        #pos (110,110) #with dissolve
        #xpos 10 ypos 10
        #with dissolve
    show screen credits_screen
    $ renpy.pause(2.0, hard=True)
    hide text with dissolve
    $ renpy.hide_screen("credits_screen")
    $ renpy.hide_screen("credit")

    return
