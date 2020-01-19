# Ideas for shapes ; circle, triangle, hexagon, rhombus

add_library('sound')
add_library('PostFX')

#--------------------------------------------------------------------------------------------

class player() :
    def __init__(self) :
        self.dirChar = 0
        self.xPosChar = width / 2
        self.yPosChar = height / 2
        self.xSpeedChar = 0
        self.ySpeedChar = 0
        self.maxSpeedChar = 5
        self.frictionChar = 1
        self.dashSpeedChar = 4
        self.dashCoolChar = 0

    def movement(self) :
        self.xPosChar += self.xSpeedChar * self.frictionChar
        self.yPosChar += self.ySpeedChar * self.frictionChar
        self.dirChar = atan2((self.yPosChar - mouseY), (self.xPosChar - mouseX))
        
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
            
        if self.frictionChar == self.dashSpeedChar and self.dashCoolChar < 114 :
            self.frictionChar = 1

        if keyList["W"] == False and keyList["S"] == False :
            self.ySpeedChar /= 1.16
        if keyList["A"] == False and keyList["D"] == False :
            self.xSpeedChar /= 1.16
        
        if self.xPosChar < 350 :
            self.xPosChar = 350
        if self.xPosChar > 650 :
            self.xPosChar = 650

        if self.yPosChar < 260 :
            self.yPosChar = 260
        if self.yPosChar > 460 :
            self.yPosChar = 460
    
    def update(self) :
        if self.dashCoolChar > 0 :
            self.dashCoolChar -= 1

    def render(self) :
        pushMatrix()
        translate(self.xPosChar, self.yPosChar)
        rotate(self.dirChar)
        square(-15, -15, 30)
        popMatrix()

#--------------------------------------------------------------------------------------------

class enemy() :
    def __init__(self) :
        self.xPosEne = 0
        self.yPosEne = 0
        self.dirEne = 0
    
    def movement(self) :
        self.dirEne = atan2(playerList[0].yPosChar, playerList[0].xPosChar)

    def render(self) :
        pushMatrix()
        translate(cameraList[0].xPosCam + self.xPosEne, cameraList[0].yPosCam + self.yPosEne)
        rotate(self.dirEne)
        square(-15, -15, 30)
        popMatrix()

#--------------------------------------------------------------------------------------------
        
class cameraPlayer() :
    def __init__(self) :
        self.xPosCam = 0
        self.yPosCam = 0
        self.movingCam = 0
    
    def movement(self) :
        self.movingCam = 0
        
        if keyList["W"] == True and playerList[0].yPosChar == 260 :
            self.yPosCam -= playerList[0].ySpeedChar * playerList[0].frictionChar
            self.movingCam = 1
        if keyList["A"] == True and playerList[0].xPosChar == 350 :
            self.xPosCam -= playerList[0].xSpeedChar * playerList[0].frictionChar
            self.movingCam = 1
        if keyList["S"] == True and playerList[0].yPosChar == 460 :
            self.yPosCam -= playerList[0].ySpeedChar * playerList[0].frictionChar
            self.movingCam = 1
        if keyList["D"] == True and playerList[0].xPosChar == 650 :
            self.xPosCam -= playerList[0].xSpeedChar * playerList[0].frictionChar
            self.movingCam = 1

        if keyList["Space"] == True and playerList[0].dashCoolChar == 119 and self.movingCam == 1 :
            engine.blurPass = 10
        
        print(playerList[0].dashCoolChar)

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
        cameraList[0].movement()
        
        enemyList[0].movement()
    
    def renderEnvironment(self) :
        background(200)
        
    def renderObjects(self) :
        playerList[0].render()
        enemyList[0].render()
    
    def postProcessing(self) :
        fx.render().vignette(0.55, 0.55).rgbSplit(25).compose()
        fx.render().blur(self.blurPass, self.blurPass).compose()
        
#--------------------------------------------------------------------------------------------

keyList = {"W" : False, "A" : False, "S" : False, "D" : False, "Space" : False}
playerList = []
enemyList = []
cameraList = []
engine = renderingEngine()

#--------------------------------------------------------------------------------------------

def setup() :
    global fx
    size(1000, 720, P2D)
    smooth(4)
    fx = PostFX(this)
    fx.preload(BloomPass)
    fx.preload(RGBSplitPass)
    enemyList.append(enemy())

#--------------------------------------------------------------------------------------------

def draw() :
    if len(playerList) == 0 :
        playerList.append(player())
    if len(cameraList) == 0 :
        cameraList.append(cameraPlayer())
    
    # print(playerList[0].dashCoolChar)
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
