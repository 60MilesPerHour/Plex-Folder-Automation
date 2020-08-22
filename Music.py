import os
import sys
import time

print("this is your current directory right now", os.getcwd())

os.chdir(input("Input desired Music location: "))
print(os.getcwd())

M = input("Would you like to start artist creation?: ")
if M == "yes":
    print("Enter Number Artists: ")
    b = input()
    ArtistAmount = int(b)

    for i in range(ArtistAmount):
        os.mkdir(str(input("Artists Name: ")))
        print(i)

elif M == "no":
    X = input("Would you like to do Album creation instead?: ")
    if X == "yes":
        print("Enter Album Amount")
        c = input()
        AlbumAmount = int(c)

        for i in range(AlbumAmount):
            AlbumToMake = 'Album - '
            A = str(input("Enter Album Name: "))
            Album = AlbumToMake + A
            os.mkdir(Album)
            print(i)
    
    else:
        print("Why did you tell me to run this script then?")
        print("------")
        time.sleep(2)
        print("You really are a confusing human") 
        sys.exit()
else:
    sys.exit