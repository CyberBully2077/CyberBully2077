# Resource page starts here.
label resources_scene:
    show resources with fade
    "You are not alone! Being bullied is a common event. \nClick the buttons to find help."
    screen vbox_test():
        vbox:
            xalign 0.1
            yalign 0.5
            spacing 20
            frame:
                xpadding 40
                ypadding 20
                xalign 0.5
                yalign 0.5                
                text "{a=https://www.stompoutbullying.org/how-to-deal-with-bullies}Dealing with Bullies{/a}"
            frame:
                xpadding 40
                ypadding 20
                xalign 0.5
                yalign 0.5
                text "{a=https://pacerteensagainstbullying.org/take-action/}Take Action!{/a}"
            frame:
                xpadding 40
                ypadding 20
                xalign 0.5
                yalign 0.5
                text "{a=https://www.stopbullying.gov/cyberbullying/how-to-deal-with-haters}Haters{/a}"

    $ renpy.show_screen("vbox_test")                
    $ renpy.pause()

menu resources_menu:
    "Choose an action."

    "Show Credits":
        hide resources
        $ renpy.hide_screen("vbox_test")
        call credit
    "Quit":
        return
