add_library('sound')
add_library('PostFX')

class player(object) :
    def __init__(self) :
        self.xPosChar = 0
        self.yPosChar = 0
        self.xSpeedChar = 0
        self.ySpeedChar = 0
        self.speedMaxChar = 3

    def movement(self) :
        if keyList["W"] == True and self.ySpeedChar != self.speedMaxChar :
            self.ySpeedChar += 0.1
        
        if keyList["W"] == False and self.ySpeedChar >= 0 :
            self.ySpeedChar -= 0.1

        if keyList["S"] == True and self.ySpeedChar != self.speedMaxChar :
            self.ySpeedChar -= 0.1
        
        if keyList["S"] == False and self.ySpeedChar <= 0 :
            self.ySpeedChar += 0.1
            
        self.yPosChar += self.ySpeedChar
    def renderChar(self) :
        pushMatrix()
        translate(self.xPosChar, self.yPosChar)
        square(20, 20, 10)
        popMatrix()
        
#--------------------------------------------------------------------------------------------

keyList = {"W" : False, "A" : False, "S" : False, "D" : False}
playerList = []
enemyList = []

#--------------------------------------------------------------------------------------------

def setup() :
    size(1000, 720)

#--------------------------------------------------------------------------------------------

def draw() :
    if len(playerList) == 0 :
        print(keyList)
        playerList.append(player())
    
    for i in playerList :
        i.movement()
        i.renderChar()
    print(playerList[0].ySpeedChar)

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
