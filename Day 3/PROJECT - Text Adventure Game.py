#TREASURE ISLAND TEXT ADVENTURE GAME

print("Welcome to Treasure Island!")
print("Your mission is to find the raft to escape from this place.\n")

print("You wake up on the beach, dizzy and in shock. Looking around you, you see nothing of use...\n")

one = input("Where do you want to go? BEACH, JUNGLE or STAY?\n").lower()
if one == "beach":
    print("You decide to walk along the beach. You go on and on, not realising you start going in circles... Eventually you die of exhaustion and starvation.\nGAME OVER")
    quit()
elif one == "stay":
    print("You decide to stay put. However, you wait hours upon hours, days upon days... Nothing happens and you eventually die.\nGAME OVER")
    quit()
elif one == "jungle":
    print("You decide to go into the jungle, towards the middle of the island...")
    print("After walking for what seems like forever, you suddenly hear twigs snapping...")
    print("You freeze. In front of you... Appears a huge boar! It huffs and snorts in anger... Then charges at you!")
    two = input("You decide to: FIGHT or RUN?\n").lower()

    if two == "fight":
        print("Really? You decide to try to fight a huge, adult male boar? You soon find that was a very bad decision...")
        print("The boar tramples on you and leaves you with huge and numerous gashes. You succumb soon after from your wounds.\nGAME OVER")
        quit()
    elif two == "run":
        print("You sensibly choose to run from the very strong and very dangerous animal...")
        print("You quickly climb a tree and wait. The boar eventually loses interest and goes away. Phew!")
        print("You keep walking and finally reach the centre of the island. You are surprised to see a shed!")
        print("The shed doesn't have any windows, and the door is locked. Looking around you, there is a big rock and a rusty key.")
        three = input("What do you decide to use? KEY or ROCK?\n").lower()
        if three == "key":
            print("You try the key, but it is so rusty it gets stuck in the keyhole. You exert more force, but... The key snaps! Ooops...\nGAME OVER")
            quit()
        elif three == "rock":
            print("You hit the door with the rock. After some minutes, the door finally breaks open!")
            print("Inside you find the raft. Well done, now you can escape from this island!\nCONGRATULATIONS!")
            quit()
        else:
                print("Please only type one of the keywords. Be careful of wrong spellings!")
    else:
        print("Please only type one of the keywords. Be careful of wrong spellings!")
else:
    print("Please only type one of the keywords. Be careful of wrong spellings!")
