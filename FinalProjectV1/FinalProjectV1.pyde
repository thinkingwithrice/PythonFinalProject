# Ideas for shapes ; circle, triangle, hexagon, rhombus

add_library('sound')
add_library('PostFX')

#--------------------------------------------------------------------------------------------

class player(object) :
    def __init__(self) :
        self.dirChar = 0
        self.xPosChar = 0
        self.yPosChar = 0
        self.xSpeedChar = 0
        self.ySpeedChar = 0
        self.maxSpeedChar = 5
        self.frictionChar = 1
        self.dashSpeedChar = 4
        self.dashCoolChar = 0

    def movement(self) :
        if keyList["W"] == True and self.ySpeedChar > self.maxSpeedChar * -1 :
            self.ySpeedChar -= 0.9
        if keyList["A"] == True and self.xSpeedChar > self.maxSpeedChar * -1 :
            self.xSpeedChar -= 0.9
        if keyList["S"] == True and self.ySpeedChar < self.maxSpeedChar :
            self.ySpeedChar += 0.9
        if keyList["D"] == True and self.xSpeedChar < self.maxSpeedChar :
            self.xSpeedChar += 0.9
    
        if keyList["Space"] == True and self.dashCoolChar == 0 :
            self.frictionChar = self.dashSpeedChar
            self.dashCoolChar = 120
            engine.blurPass = 10
        if self.frictionChar == self.dashSpeedChar and self.dashCoolChar < 114 :
            self.frictionChar = 1

        if keyList["W"] == False and keyList["S"] == False :
            self.ySpeedChar /= 1.13
        if keyList["A"] == False and keyList["D"] == False :
            self.xSpeedChar /= 1.13

        self.xPosChar += self.xSpeedChar * self.frictionChar
        self.yPosChar += self.ySpeedChar * self.frictionChar
    
    def update(self) :
        self.dirChar = atan2((self.yPosChar - mouseY), (self.xPosChar - mouseX))
        
        if self.dashCoolChar > 0 :
            self.dashCoolChar -= 1

    def render(self) :
        pushMatrix()
        translate(self.xPosChar, self.yPosChar)
        rotate(self.dirChar)
        square(-15, -15, 30)
        popMatrix()

#--------------------------------------------------------------------------------------------

class enemies(object) :
    def __init__(self) :
        return

#--------------------------------------------------------------------------------------------

class renderingEngine() :
    def __init__(self) :
        self.blurPass = 0
        
    def engineVars(self) :
        if self.blurPass > 0 :
            self.blurPass -= 1
    
    def updateObjects(self) :
        playerList[0].movement()
        
        playerList[0].update()
    
    def renderEnvironment(self) :
        background(200)
        
    def renderObjects(self) :
        playerList[0].render()
    
    def postProcessing(self) :
        fx.render().vignette(0.55, 0.55).rgbSplit(20).compose()
        fx.render().blur(self.blurPass, self.blurPass).compose()
        
#--------------------------------------------------------------------------------------------

keyList = {"W" : False, "A" : False, "S" : False, "D" : False, "Space" : False}
playerList = []
enemyList = []
engine = renderingEngine()

#--------------------------------------------------------------------------------------------

def setup() :
    global fx
    size(1000, 720, P2D)
    smooth(4)
    fx = PostFX(this)
    fx.preload(BloomPass)
    fx.preload(RGBSplitPass)

#--------------------------------------------------------------------------------------------

def draw() :
    if len(playerList) == 0 :
        playerList.append(player())
    
    print(playerList[0].dashCoolChar)
    engine.updateObjects()
    engine.renderEnvironment()
    engine.renderObjects()
    engine.postProcessing()
    engine.engineVars()

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
    if key == " " :
        keyList["Space"] = True

def keyReleased() :
    if key == "w" :
        keyList["W"] = False
    if key == "a" :
        keyList["A"] = False
    if key == "s" :
        keyList["S"] = False
    if key == "d" :
        keyList["D"] = False
    if key == " " :
        keyList["Space"] = False
