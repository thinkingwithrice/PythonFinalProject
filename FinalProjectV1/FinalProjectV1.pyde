# Ideas for shapes ; circle, triangle, hexagon, rhombus

add_library('sound')
add_library('PostFX')

class player(object) :
    def __init__(self) :
        self.xPosChar = 0
        self.yPosChar = 0
        self.speedChar = 3

    def movement(self) :
        if keyList["W"] == True :
            self.yPosChar -= self.speedChar
            
        if keyList["A"] == True :
            self.xPosChar -= self.speedChar
            
        if keyList["S"] == True :
            self.yPosChar += self.speedChar
            
        if keyList["D"] == True :
            self.xPosChar += self.speedChar
            
        
    
    def renderChar(self) :
        pushMatrix()
        translate(self.xPosChar, self.yPosChar)
        square(20, 200, 20)
        popMatrix()

class renderingEngine() :
    def __init__(self) :
        return
    
    def updateObjects(self) :
        playerList[0].movement()
        
    def renderObjects(self) :
        playerList[0].renderChar()
        
#--------------------------------------------------------------------------------------------

keyList = {"W" : False, "A" : False, "S" : False, "D" : False}
playerList = []
enemyList = []
engine = renderingEngine()

#--------------------------------------------------------------------------------------------

def setup() :
    size(1000, 720)

#--------------------------------------------------------------------------------------------

def draw() :
    if len(playerList) == 0 :
        print(keyList)
        playerList.append(player())
        
    engine.updateObjects()
    engine.renderObjects()
    
    


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
