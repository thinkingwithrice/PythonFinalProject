add_library('sound')
add_library('PostFX')

class 

#--------------------------------------------------------------------------------------------

keyList = {"W" : False, "A" : False, "S" : False, "D" : False}

#--------------------------------------------------------------------------------------------

def setup() :
    size(1000, 720)

#--------------------------------------------------------------------------------------------

def draw() :
    print(keyList)

#--------------------------------------------------------------------------------------------

def keyPressed() :
    if key == "w" :
        keyList["W"] = True
    if key == "a" :
        keyList["A"] = True
    if key == "s" :
        keyList["S"] = True
    if key == "d" :
        keyList["D"] = True

def keyReleased() :
    if key == "w" :
        keyList["W"] = False
    if key == "a" :
        keyList["A"] = False
    if key == "s" :
        keyList["S"] = False
    if key == "d" :
        keyList["D"] = False
