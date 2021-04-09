# Plex Music Folder Automation

If you have ever run a plex media server and had to store your songs and couldn’t get plex to correctly organize the files so you had to make all the folders by hand then you have found the right script. Plex music automation takes the hassle out of constant folder creation with hectic copy and pasting.

(this script is planned for upgrades very soon)


## Code Snippet

```
import os
import sys
import time

print("this is your current directory right now", os.getcwd()) # Not needed but is useful

os.chdir(input("Input desired Music location: ")) # Change Directory to where the magic will happen :)
print(os.getcwd())
```
