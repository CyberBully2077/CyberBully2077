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
