import time
import random


def adventure():
    """Runs one session of interactive fiction

    Well, it's "fiction," depending on the pill color chosen...

    arguments: no arguments (prompted text doesn't count as an argument)
    results: no results     (printing doesn't count as a result)
    """
    # change to 0.0 for testing or speed runs,
    # ... or larger for dramatic effect!
    delay = 5.0
    draw = 0.5

    username = input("What do we call you, oh mighty Adventurer?... ")
    print()
    print("\n\n\n")

    print("                 \||/")
    print("                |  @___oo")
    print("      /\  /\   / (__,,,,|")
    print("     ) /^\) ^\/ _)")
    print("     )   /^\/   _)")
    print("     )   _ /  / _)")
    print(" /\  )/\/ ||  | )_)")
    print("<  >      |(,,) )__)")
    print(" ||      /    \)___)\ ")
    print(" | \____(      )___) )___")
    print("  \______(_______;;; __;;;")
    print()
    print()
    print("Welcome,", username, "to Dungeons and Dragons")
    print("In this adventure you will venture forth to find the Sword of a a Thousand Thruths and save the village from great peril")
    print()
    
    heroclass = input("What is your class? [Warrior/Rogue/Mage]...").lower()
    if heroclass == "warrior":
        time.sleep(delay)
        print("\nOh might Warrior, let your sword and shield bring you great victory!")
    elif heroclass == "rogue":
        time.sleep(delay)
        print("\nFighting from the shadows, eh? Sneaky little.....")
    elif heroclass == "mage":
        time.sleep(delay)
        print("\nFight fire with fire! (or perhaps ice?)")

    print()
    print("We start our adventure in the Neverwinter Woods\n\n")
    print("It's early in the evening and the sun is starting to set")
    print("You need to get out of the forest before it's fully dark, \nbut you hear a scream from your right, a couple of hundred yards away")
       
    time.sleep(delay)

    print("\nWhat do you do?")
    print("1: Check it out")
    print("2: Yell to the stranger")
    print("3: Keep Running")

    choice_stranger = input("Choose an option:...").lower()

    if choice_stranger == "1":
        print("\nYou dismount your horse and start walking into the darker part of the forest")
        time.sleep(delay)
        choice_lantern = input("do you take out a lantern? [yes/no]...").lower()
        if choice_lantern == "yes":
            print("\nYou grab your lantern and continue forward")
            time.sleep(delay)
            print("\nAfter about a three minute walk you find a mauled, lifeless, body on the forest floor")
            print("After a quick investigation it looks like a wolf did this")
            time.sleep(delay)
            choice_take_body = input("Do you take the body back with you? [yes/no]...").lower()
            if choice_take_body == "yes":
                time.sleep(delay)
                print("\nYou pick up the pieces of the body, and start making your way back to your horse")
                print("Once you are back at your horse, you mount the body, or what's left of it on the back of your saddle\nand you start moving towards Neverwinter")
            time.sleep(delay)
            print("You leave the body behind, nature will find its way")
            print("Arriving at your horse you hear the wolves howling behind you, you mount up quick and give your steed the spurrs\n\nOnwards to Neverwinter!")    
        else:
            print("It's quickly becoming darker and darker")
            time.sleep(delay)
            print("\nAfter about 50 yards, you decide to leave the victim, and try to find you're way back to your horse")
            time.sleep(delay)
            print("It takes you a while, but finally you find your horse,\ntho you hear more and more unnerving sounds behind you")
            time.sleep(delay)
            print("You jump on your trusty steed, and make haste towards Neverwinter")
    elif choice_stranger == "2":
        time.sleep(delay)
        print("\nYou start yelling into the dark, but only wolf howls seem to respond")
        print("After around 2 minutes you yelling without any human response you feel it's time to venture forward to Neverwinter")
    else:
        time.sleep(delay)
        print("\nYou are not feeling very adventures and give your horse the spurrs, let's keep moving forward")
    print("\n\nYour steed is in a very good mood, and brings you ever closer to your goal\n\n\n")
    time.sleep(7.5)        

    print("    |>>>                                                      |>>> ")
    time.sleep(draw)
    print("    |                     |>>>          |>>>                  |")
    time.sleep(draw)
    print("    *                     |             |                     *")
    time.sleep(draw)
    print("   / \                    *             *                    / \ ")
    time.sleep(draw)
    print("  /___\                 _/ \           / \_                 /___\ ")
    time.sleep(draw)
    print("  [   ]                |/   \_________/   \|                [   ]")
    time.sleep(draw)
    print("  [ I ]                /     \       /     \                [ I ]")
    time.sleep(draw)
    print("  [   ]_ _ _          /       \     /       \          _ _ _[   ]")
    time.sleep(draw)
    print("  [   ] U U |        {#########}   {#########}        | U U [   ]")
    time.sleep(draw)
    print("  [   ]====/          \=======/     \=======/          \====[   ]")
    time.sleep(draw)
    print("  [   ]    |           |   I |_ _ _ _| I   |           |    [   ]")
    time.sleep(draw)
    print("  [___]    |_ _ _ _ _ _|     | U U U |     |_ _ _ _ _ _|    [___]")
    time.sleep(draw)
    print("  \===/  I | U U U U U |     |=======|     | U U U U U | I  \===/")
    time.sleep(draw)
    print("   \=/     |===========| I   | + W + |   I |===========|     \=/")
    time.sleep(draw)
    print("    |  I   |           |     |_______|     |           |   I  |")
    time.sleep(draw)
    print("    |      |           |     |||||||||     |           |      |")
    time.sleep(draw)
    print("    |      |           |   I ||vvvvv|| I   |           |      |")
    time.sleep(draw)
    print("_-_-|______|-----------|_____||     ||_____|-----------|______|-_-_")
    time.sleep(draw)
    print("   /________\         /______||     ||______\         /________\ ")
    time.sleep(draw)
    print("  |__________|-------|________\_____/________|-------|__________|")
    print("\n\n              WELCOME TO NEVERWINTER\n\n")

    time.sleep(delay)

    print("you arrive at the portcullis, but it's closed for the night what do you do?")
    print("1: You give a firm knock on the door and let the guard you know", username, "is here")
    print("2: You try to climb the portcullis")
    print("3: You travel along the wall, looking for another entrance")
    print("4: You wait untill morning, then someone sure will open the gate, right?")
    
    choice_portcullis = input("Choose your option:...").lower()
    time.sleep(delay)
    if choice_portcullis == "1":
        print("\n\nThe guard responds and ask you what you are doing here")
        print("and after a brief conversation he let's you into town")
    elif choice_portcullis == "2":
        print("\n\nYou gather your strenght and start climbing the structure")
        print("you roll your D20 to see if you are actually strong enough")
        time.sleep(delay)
        D20 = random.choice([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
        print("You rolled..................", D20,"!!!!")
        time.sleep(5.0)
        if D20 >= 10:
            print("\nyou are strong enough and you climb over the wall")
        elif D20 == 1:
            print("\nStrength, what is that, you fall down and take 5HP damage")
        elif D20 == 20:
            print("\nVery nible, you climb over the wall, and salute the guards on top")        
        else: 
            print("\nYou lack a little strength for this, and you fall to the ground!")    
    elif choice_portcullis == "3":
        time.sleep(delay)
        print("\n\nYou start traveling around the wall until you find a small entrance, after a little squeezing you enter town")
    else:
        time.sleep(delay)
        print("\n\nYou tug in for the night, and wait till morning")
    print()
    print()
    print()
    print("TO BE CONTINUED")               