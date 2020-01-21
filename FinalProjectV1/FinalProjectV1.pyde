# Ideas for shapes ; circle, triangle, hexagon, rhombus

add_library('sound')
add_library('PostFX')

#--------------------------------------------------------------------------------------------

class player() :
    def __init__(self) :
        self.hPChar = 5
        self.hurtChar = 0
        self.hurtCoolChar = 60
        
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
            self.ySpeedChar /= 1.17
        if keyList["A"] == False and keyList["D"] == False :
            self.xSpeedChar /= 1.17
        
        if self.xPosChar < 350 :
            self.xPosChar = 350
        if self.xPosChar > 650 :
            self.xPosChar = 650

        if self.yPosChar < 260 :
            self.yPosChar = 260
        if self.yPosChar > 460 :
            self.yPosChar = 460
    
    def update(self) :    
        global gameState        
        if self.dashCoolChar > 0 :
            self.dashCoolChar -= 1
        if self.hurtCoolChar > 0 :
            self.hurtCoolChar -= 1
            
        if self.hurtChar == 1 and self.hurtCoolChar == 0 :
            self.hPChar -= 1
            self.hurtCoolChar = 60
        if playerList[0].hPChar < 1 :
            gameState = False

    def render(self) :
        pushMatrix()
        translate(self.xPosChar, self.yPosChar)
        rotate(self.dirChar)
        square(-15, -15, 30)
        popMatrix()

#--------------------------------------------------------------------------------------------

class enemy() :
    def __init__(self) :
        self.hPEne = 4
        self.hurtEne = 0
        self.hurtCoolEne = 60
        
        self.xPosEne = width / 2
        self.yPosEne = height / 2
        self.dirEne = 0
        self.speedEne = 4
        self.distX = 0
        self.distY = 0
        
    def movement(self) :
        self.dirEne = atan2((self.yPosEne + cameraList[0].yPosCam) - playerList[0].yPosChar, (self.xPosEne + cameraList[0].xPosCam) - playerList[0].xPosChar)
        self.distX = (cameraList[0].xPosCam - playerList[0].xPosChar) - self.xPosEne
        self.distY = (playerList[0].yPosChar - cameraList[0].yPosCam) - self.yPosEne
        
        if (playerList[0].xPosChar - cameraList[0].xPosCam) - self.xPosEne > 26 or (playerList[0].xPosChar - cameraList[0].xPosCam) - self.xPosEne < -26 :
            self.xPosEne += self.speedEne * cos(self.dirEne) * -1
        if (playerList[0].yPosChar - cameraList[0].yPosCam) - self.yPosEne > 26 or (playerList[0].yPosChar - cameraList[0].yPosCam) - self.yPosEne < -26:
            self.yPosEne += self.speedEne * sin(self.dirEne) * -1
    
    def hitbox(self) :
        if playerList[0].xPosChar - (self.xPosEne + cameraList[0].xPosCam) < 28 and playerList[0].xPosChar - (self.xPosEne + cameraList[0].xPosCam) > -28 and playerList[0].dashCoolChar < 100 :
            if playerList[0].yPosChar - (self.yPosEne + cameraList[0].yPosCam) < 28 and playerList[0].yPosChar - (self.yPosEne + cameraList[0].yPosCam) > -28 and playerList[0].dashCoolChar < 100 :
                engine.hitDetectTemp = 50
                playerList[0].hurtChar = 1
            else :
                engine.hitDetectTemp = 200
                playerList[0].hurtChar = 0
        else :
            engine.hitDetectTemp = 200
            playerList[0].hurtChar = 0
            
        if playerList[0].xPosChar - (self.xPosEne + cameraList[0].xPosCam) < 28 and playerList[0].xPosChar - (self.xPosEne + cameraList[0].xPosCam) > -28 and playerList[0].dashCoolChar > 90 and self.hurtCoolEne == 0 :
            if playerList[0].yPosChar - (self.yPosEne + cameraList[0].yPosCam) < 28 and playerList[0].yPosChar - (self.yPosEne + cameraList[0].yPosCam) > -28 and playerList[0].dashCoolChar > 90 and self.hurtCoolEne == 0 :
                self.hPEne -= 1
                self.hurtCoolEne = 60
    
    def update(self) :
        if self.hPEne < 1 :
            enemyList.remove(self)
        
        if self.hurtEne == 1 :
            self.hPEne -= 1
            
        if self.hurtCoolEne > 0 :
            self.hurtCoolEne -= 1

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
        self.movingXCam = 0
        self.movingYCam = 0
    
    def movement(self) :
        self.movingCam = 0
        self.movingXCam = 0
        self.movingYCam = 0
        
        if playerList[0].yPosChar == 260 and playerList[0].ySpeedChar < -0.01 :
            self.yPosCam -= playerList[0].ySpeedChar * playerList[0].frictionChar
            self.movingYCam = 1
        if playerList[0].xPosChar == 350 and playerList[0].xSpeedChar < -0.01 :
            self.xPosCam -= playerList[0].xSpeedChar * playerList[0].frictionChar
            self.movingXCam = 1
        if playerList[0].yPosChar == 460 and playerList[0].ySpeedChar > 0.01 :
            self.yPosCam -= playerList[0].ySpeedChar * playerList[0].frictionChar
            self.movingYCam = 1
        if playerList[0].xPosChar == 650 and playerList[0].xSpeedChar > 0.01 :
            self.xPosCam -= playerList[0].xSpeedChar * playerList[0].frictionChar
            self.movingXCam = 1

        if keyList["Space"] == True and playerList[0].dashCoolChar == 119 :
            engine.rgbPass = 100
            engine.blurPass = 15
        
        print(self.xPosCam, self.yPosCam, self.movingCam, playerList[0].xSpeedChar, playerList[0].ySpeedChar)

#--------------------------------------------------------------------------------------------

class weapon() :
    def __init__(self, weaponCool, weaponMaxCool, weaponDmg) :
        self.weaponState = 1
        self.weaponCool = weaponCool
        self.weaponMaxCool = weaponMaxCool
        self.weaponDmg = weaponDmg
        
    def movement(self) :
        self.weaponDir = playerList[0].dirChar
        self.xPosWeapon = playerList[0].xPosChar
        self.yPosWeapon = playerList[0].yPosChar
        self.xSpeedWeapon = playerList[0].xSpeedChar
        self.ySpeedWeapon = playerList[0].ySpeedChar
    
    def shooting(self) :
        if keyList["LeftMouse"] == True and self.weaponCool == 0 :
            bulletList.append(bullet(self.weaponDir))
            self.weaponCool = self.weaponMaxCool
    
    def update(self) :
        if self.weaponCool > 0 :
            self.weaponCool -= 1
    
    def render(self) :
        pushMatrix()
        translate(self.xPosWeapon, self.yPosWeapon)
        rotate(self.weaponDir)
        rect(0, 2, -28, -4)
        popMatrix()
    
    def update(self) :
        if self.weaponCool > 0 :
            self.weaponCool -= 1

#--------------------------------------------------------------------------------------------
            
class bullet() :
    def __init__(self, dirBullet) :
        self.dirBullet = dirBullet
        self.xPosBullet = playerList[0].xPosChar
        self.yPosBullet = playerList[0].yPosChar
        self.speedBullet = 10
        self.bulletAliveTime = 180
        
    def movement(self) :
        if cameraList[0].movingXCam == 1 :
            self.xPosBullet -= playerList[0].xSpeedChar
        if cameraList[0].movingYCam == 1 :
            self.yPosBullet -= playerList[0].ySpeedChar
        
        self.xPosBullet += (self.speedBullet * cos(self.dirBullet) * -1)
        self.yPosBullet += (self.speedBullet * sin(self.dirBullet) * -1)
        
    def hitReg(self) :
        for e in enemyList :
            if e.xPosEne - 15 < self.xPosBullet - cameraList[0].xPosCam and e.xPosEne + 15 > self.xPosBullet - cameraList[0].xPosCam :
                if e.yPosEne - 15 < self.yPosBullet - cameraList[0].yPosCam and e.yPosEne + 15 > self.yPosBullet - cameraList[0].yPosCam:
                    e.hPEne -= 1
                    self.bulletAliveTime = 0
    
    def update(self) :
        if self.xPosBullet > width or self.xPosBullet < 0 or self.yPosBullet > height or self.yPosBullet < 0 :
            bulletList.remove(self)
        if self.bulletAliveTime > 0 :
            self.bulletAliveTime -= 1
        else :
            bulletList.remove(self)
    
    def render(self) :
        pushMatrix()
        
        translate(self.xPosBullet, self.yPosBullet)
        rotate(self.dirBullet)
        translate(-30, 0)
        
        ellipse(0, 0, 5, 5)
        popMatrix()

#--------------------------------------------------------------------------------------------

class renderingEngine() :
    def __init__(self) :
        self.blurPass = 0
        self.rgbPass = 25
        self.hitDetectTemp = 200
        
    def engineVars(self) :
        if self.blurPass > 0 :
            self.blurPass -= 1
        if self.rgbPass > 25 :
            self.rgbPass -= 1
    
    def updateObjects(self) :
        if gameState == True :
            playerList[0].movement()
            playerList[0].update()
            
            temp.movement()
            temp.shooting()
            temp.update()
            
            cameraList[0].movement()
            
            for e in enemyList :
                e.movement()
                e.hitbox()
                e.update()
            for b in bulletList :
                b.movement()
                b.hitReg()
                b.update()
    
    def renderEnvironment(self) :
        background(self.hitDetectTemp)
        
    def renderObjects(self) :
        global temp
        if gameState == True :
            for b in bulletList :
                b.render()
            temp.render()
            playerList[0].render()
            
            for e in enemyList :
                e.render()
    
    def postProcessing(self) :
        # fx.render().vignette(0.55, 0.55).rgbSplit(self.rgbPass).compose()
        # fx.render().blur(self.blurPass, self.blurPass).compose()
        return
        
#--------------------------------------------------------------------------------------------

keyList = {"W" : False, "A" : False, "S" : False, "D" : False, "Space" : False, "LeftMouse" : False}
playerList = []
weaponList = []
bulletList = []
enemyList = []
cameraList = []
engine = renderingEngine()
gameState = True

#--------------------------------------------------------------------------------------------

def setup() :
    global fx, temp
    size(1000, 720, P2D)
    smooth(4)
    
    fx = PostFX(this)
    fx.preload(BloomPass)
    fx.preload(RGBSplitPass)
    fx.preload(VignettePass)
    playerList.append(player())
    enemyList.append(enemy())
    temp = weapon(1, 30, 1)
    temp2 = weapon(1, 2, 1)
    

#--------------------------------------------------------------------------------------------

def draw() :
    global temp
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

def mousePressed() :
    if mouseButton == LEFT :
        keyList["LeftMouse"] = True

def mouseReleased() :
    if mouseButton == LEFT :
        keyList["LeftMouse"] = False
