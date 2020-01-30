# PythonFinalProject - Untitled Triangle Game
Final project for CS30 built in Python in Processing.

This is a top-down shooter game where you play as a triangle. That's it. Don't die. Oh, and yes, I really named the game "Untitled Triangle Game".

Current version : 1.0.1.0.0
Please visit "https://github.com/thinkingwithrice/PythonFinalProject" to view versions / commits.
NOTE : REQUIRES "POSTFX" AND "MINIM" LIBRARY!

Update Log :
[2:16 PM, Jan. 30th, 2020] Update 1.0.1.1.0 :
Added pointer that if enemies are present, it will point towards the general area of the enemies, fixed some bugs, 
improved code and game, (difficulty risen), and cleaned up / re-worked some code.

[2:51 AM, Jan. 30th, 2020] Update 1.0.1.0.0 (Release) :
Added many assets, enemy waves, shop, upgrades, points, UI, menu, and many more. This is the first release of the game.

[2:25 PM, Jan. 23rd, 2020] Update 1.0.0.9.1 (Small Changes) :
Changed up some code, fixed enemy-to-player attacking, and changed enemy hit colour.

[3:25 PM, Jan. 22nd, 2020] Update 1.0.0.9 :
Added enemy repulsion from each other, bullet hit animation, and cleaned up / reworked some code.

[10:27 PM, Jan. 20th, 2020] Update 1.0.0.8 :
Added bullet "physics" where if camera moves, the bullet will be correctly drawn on the screen, ie. move camera left, bullet will be moving right, bullet "dies" when it hits enemy
and lowers the specific enemy's health, bullet auto "dies" when travelling, fixed "movingCam" variable to properly register if the camera is moving, and cleaned up / fixed some code.

[3:25 PM, Jan. 20th, 2020] Update 1.0.0.7 :
Added bullet shooting, (Unfinished).

[1:19 PM, Jan. 20th, 2020] Update 1.0.0.6 :
Added more to the weapon class, rendered weapon, and working on bullet class. Improved camera by easing the same amount as player, created important variables, and cleaned up code.

[11:22 PM, Jan. 19th, 2020] Update 1.0.0.5 :
Small update which changes and adds a few things. Dash animation / post processing changed, creating weapon class (nothing inside right now), changed dash to harm enemies if dashed
through, added enemy death, changed player movement easing, and a few smaller changes / cleaning.

[6:31 PM, Jan. 19th, 2020] Update 1.0.0.4 :
Improved camera, added enemy render and follow (constant speed towards player), added temp. health to player, added enemy hitting player and losing health, created a temp. gamestate
(if player dies, gamestate = 0, meaning game has ended), and changed a few values / cleaned up code.

[1:55 AM, Jan. 19th, 2020] Update 1.0.0.3 :
Added a camera which only moves when player is attempting to move beyond deadzone, imporved dash, changed blur requirements (only blurs when dash moves camera), added basic functions
to enemy class (enemy responding to camera movement), and cleaned up code.

[10:51 PM, Jan. 18th, 2020] Update 1.0.0.2 :
Added easing speed, basic dash with cooldown, post processing, cleaned up code, and re-made movement.

[3:24 PM, Jan. 17th, 2020] Update 1.0.0.1 :
Added barebones rendering engine, movement, and cleaned up code.

[2:25 PM, Jan 16th, 2020] Update 1.0.0.0 :
Added barebones key detection.
