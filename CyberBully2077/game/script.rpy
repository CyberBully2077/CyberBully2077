#login authentication splashscreen code.

image splash = "login.png"

# Python code for login/signup functionality
init python in loginManager:
    import hashlib
    import os
    def getcredpath():
        # This is if we want to save the creds in the local app data folder
        compLocalStroage = os.getenv("LOCALAPPDATA")
        # Right now storing the creds inside the game folder
        credpath = renpy.config.gamedir+"\CyberBully2077\cred"
        credpath = credpath.replace("\\",'/')
        path = credpath+"\credentials.txt"
        # Checks if file exist
        if os.path.exists(path):
            return credpath
        else:
        #if path dosnt exist it will make it
            if not os.path.exists(credpath):
                os.makedirs(credpath)
            uName = "Admin"
            conf_pwd = "admin"
            enc = conf_pwd.encode()
            hash1 = hashlib.md5(enc).hexdigest()
            # if we want to hash the username too
            enc2 = uName.encode()
            hash2 = hashlib.md5(enc2).hexdigest()
            # add the default admin username and password
            with open(credpath+"\credentials.txt", "w") as f:
                f.write("Admin" + ":")
                f.write(hash1+"\n")
            f.close()
        return credpath

    def signup(email,pwd,conf_pwd):
        # gets the creds path then checks the pwd are the same
        credpath = getcredpath()
        if conf_pwd == pwd:
            # generate hash for password and stores it in file 
            enc = conf_pwd.encode()
            hash1 = hashlib.md5(enc).hexdigest()
            with open(credpath+"\credentials.txt", "a") as f:
                f.write(email + ":")
                f.write(hash1+"\n")
            f.close()
            return True
        else:
            return False
    def login(email,pwd):
        #get path then goes though the lines of the file and checks if user name and password is stored
        credpath = getcredpath()
        auth = pwd.encode()
        auth_hash = hashlib.md5(auth).hexdigest()
        uDict ={}
        with open(credpath+"\credentials.txt", "r") as f:
            for line in f:
                stored_email, stored_pwd = line.strip().split(":")
                uDict.update({stored_email:stored_pwd})
        f.close()
        #if email == stored_email and auth_hash == stored_pwd:
        for i in uDict.keys():
            if email == i:
                if auth_hash == uDict.get(i):
                    renpy.input("Logged in Successfully press enter to continue!")
                    renpy.full_restart()
                    return True
                else:
                    return False

default lgm = False
label splashscreen:
    scene black
    with Pause(1)

    play sound "loginSound.mp3"
    
    show splash #with dissolve
    $ count = 0 
    $ signup = False
    $ lgm = True
    menu signup_login:
        "Signup":
            jump mysignup
        "Login":
            jump myLogin
    $ lgm = False
    label myLogin:
    $ email = renpy.input("Enter email: ")
    $ pwd = renpy.input("Enter password: ")
    if not loginManager.login(email,pwd) :
        jump failedLogin
                    
    label failedLogin:
        $ count += 1
        $ remain = 3 - count
        if count > 2:
            jump invalid
        "Invalid user name or password, contact administration for authorization."                   
        "You have [remain] chances left!"
        jump myLogin

    label invalid:
    python:
        renpy.quit()

    label mysignup:
    $ email = renpy.input("Enter email address: ")
    $ pwd = renpy.input("Enter password: ")
    $ conf_pwd = renpy.input("Confirm password: ")
    if loginManager.signup(email,pwd,conf_pwd):
        "Successfully created user redirecting to login"
    else:
        "Passwords are not the same try again"
        jump mysignup
    jump myLogin
# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define logan = Character("Logan Peabody")
define teacher = Character("Mrs. Smith")
define students = Character("Students")
define bully = Character("Tom")
define sidekick1 = Character("Ice")
define sidekick2 = Character("Jay")

transform midright:
    xalign 0.7
define e = Character("Eileen")
image crawl = Movie(play = "CyberBullyCrawl.webm", loops = 1)
define slowdissolve = Dissolve(0.5)

transform midright2:
    xalign 0.8


# The game starts here.
label start:
    stop music
    scene crawl
    with slowdissolve
    pause 18.0
    window show

    image black = "black.jpg"
    scene bg black
   
    show black
    with slowdissolve

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene homeroom with fade

    show teacher
    teacher "Now class, we have a new student joining us today! Can we have a warm CyberOaks welcome salute for Logan Peabody?"

    show students
    students "(low murmurings) Hi Logan..."
    hide students

    show teacher
    teacher "Very nice class. Logan, come up and introduce yourself. "      # Sarcastic Expression
    hide teacher

    show logan at right

    logan "uh... hi......my name is Logan....uhm...yeah... "

    show bully at left

    bully "(snorts and snickers)"

    show logan embarrased at right       # Requires logan embarassed.png  in images directory

    hide logan
    hide bully
    show teacher at right
    teacher "That’s very nice dear... maybe we will work on our oratory skills a bit more"

    hide teacher
    show bully at left
    bully "REEEEEEEE"

    "<bully's name> flicks Logan's ear." with vpunch
    
    show logan at right

    hide bully
    hide logan

    teacher "Ok class, next week..."
    hide teacher

    "The teacher starts droning on about weekly events in homeroom"

    show logan at right
    "Logan zones out and starts drawing on his tablet."
    hide logan

    scene gym with fade

    show logan at left
    show bully at right
    "Tom sits next to Logan and steals his unlocked phone."
    "He copies all the content to his own phone."

    logan "I can't find my phone!"

    logan "Hey! Has anyone seen my phone!?"

    bully "Yeah man, I saw someone take it. Listen, I feel bad about flicking your ear in homeroom."
    bully "I know the guy that took it, I will get it back for you. Meet me after class in the bathroom."

    logan "Uh.., ok, thanks!"

    hide logan
    hide bully
    scene bathroom with fade

    show logan at left
    logan "Hey Tom, you got my phone back!"

    show bully at right

    bully "(laughs) Yeah, check it out!"
    "Tom shows screen of Logan's personal pictures"
    bully " Dork!"

    logan "Give me that!"

    bully "Oops!"

    "Tom drops Logan's phone into the toilet and runs off." with vpunch

    hide bully
    bully "HAHAHU HU HEE HEE!"

    $ tell_no_one = True
    menu bathroom_menu:
        "Choose an action:"

        "Retrieve the phone and tell no one.":
            $ tell_no_one = True
        
        "Retrieve the phone and tell the homeroom teacher.":
            $ tell_no_one = False
    
    logan "(What a jerk...)"
    logan "(Thank God the toilet was empty!)"

    "Logan washes and dries his phone."
    hide logan

    if tell_no_one:
        jump lunchroom_scene
    else:

        "Logan storms out of the bathroom and runs to homeroom"
        scene homeroom with fade

        show logan at right
        show teacher at left
        logan "Mrs. Smith?"
        teacher "Yes...uh.. Logan! What can I do for you?"
        logan "I have an issue with Tom. He seems to be picking on me."
        teacher "Oh, nonsense - you just arrived here honey! I don't think anyone would have any problems with you yet!"
        logan "He stole my phone and dropped it in the toilet!"
        teacher "I see you have your phone and it is working, is it not?"
        logan "Yes, but..."
        play sound "bell.mp3"
        "The bell rings..." with vpunch
        teacher "Ooh! Lunchtime! You better hurry so you are not late!"
        hide teacher
        logan "(Sighs)"
        jump lunchroom_scene_alt
    
    return

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
    logan "Tom...!"

    # jump to next scene here
    
    return

label lunchroom_scene_alt:
    scene cafeteria with fade
    
    show logan at left
    "Logan walks to a table holding his food tray."

    show bully sinister at right
    "Tom see Logan and sticks his foot out in front of Logan without him noticing."

    with vpunch
    logan hurt "Ow!"

    "Logan falls and his face collides with his food tray on the ground."

    students "(Laughing)" with vpunch

    menu lunchroom_options:
        "Choose an option"

        "Logan punches Tom":
            logan "Take this you fart smelling bully!" with vpunch
            # TODO

        "Logan cleans himself up and ignores Tom":
            logan "Grr...."
            # TODO

    return