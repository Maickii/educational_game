# educational_game

https://maickii.github.io/educational_game/

This repository is used to host the website for our educational game. It mainly hosts hmtl files and other assets for the website.

Collaborators please follow these steps to get started.


1) `git clone https://github.com/Maickii/educational_game.git`. step one will download all the files in the repo. All the files will be in a directory called `educational_game/`. Now change directory to that folder.
2) look around! `ls` through the directories and see whats around. You can also see the commit history. this is done by `git log`. with `git log` you will see the commits that has been made so far. if you want to see the actual changes of those commits you can do `hash=<hash number for the commit>; git diff $hash^ $hash`. if you just want to look at the most recent commit you can do `git diff HEAD^`.
3) to make changes simply start by modifying whatever files you need to modify. Say I wanted to upload my profile pciture. i simply copy the the picture into the assets folder. like so: `cp /home/michael/michael_s_profile.jpg assets/`. now do a `git status`. you should see the file you copied over in red. do a `git add <file>` to add the file. to see that you added the file correctly do a `git status` and the file should appear in green this time. you should always do a git add right before you commit changes, which brings us to the the next step. 
4) `git commit -m "<some meaningful commit message>"`. this will commit the file you added. if you get an error among the lines of "Please tell me who you are" just run the commands it prompts you to run. once you done that try commiting the files again.
5) Once you commit your file you should now see the new update with `git log`. 
6) all the changes up to now have been done locally. to upload to github with the new commits you can do `git push origin master`. it will ask for your github credentials. after that it should be uploaded to github. STAY AWAY FROM `GIT PUSH ORIGIN MASTER --FORCE`!
