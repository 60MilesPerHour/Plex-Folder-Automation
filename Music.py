# Lines 2 - 4 are essential
import os
import sys
import time

print("this is your current directory right now", os.getcwd()) # Not needed but is useful

os.chdir(input("Input desired Music location: ")) # Change Directory to where the magic will happen :)
print(os.getcwd())

M = input("Would you like to start artist creation?: ")
# Should be pretty self explanatory below but ill try to comment the confusing stuff
if M == "yes":
    print("Enter Number Artists: ") # Number of folders your gonna make
    b = input()
    ArtistAmount = int(b)

    for i in range(ArtistAmount):
        os.mkdir(str(input("Artists Name: "))) # Create a folder in the directory you specified earlier with the Artists name
        print(i)

elif M == "no":
    X = input("Would you like to do Album creation instead?: ") # Create a folder in the directory you specified earlier
    if X == "yes":
        print("Enter Album Amount") # Number of folders your gonna make
        c = input()
        AlbumAmount = int(c)

        for i in range(AlbumAmount):
            AlbumToMake = 'Album - ' # you have to add 'Album - Album Name' every time you make a new media file system for plex so i just automated out the Album - part...
            A = str(input("Enter Album Name: ")) # Enter Album name, be as accurate as you can (CPY & PSTE) because plex will have a hard time if you don't
            Album = AlbumToMake + A
            os.mkdir(Album)
            print(i)
    
    else:
        print("Why did you tell me to run this script then?") # Eh, just added some comedy cause if you reach this point during execution then there was no point of even running the code to begin with...
        print("------")
        time.sleep(2)
        print("You really are a confusing human") # Comedy?
        sys.exit() # Exit
else:
    sys.exit() # Exit
