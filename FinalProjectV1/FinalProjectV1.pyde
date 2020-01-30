# Ideas for shapes ; circle, triangle, hexagon, rhombus

add_library('minim')
add_library('PostFX')

#--------------------------------------------------------------------------------------------

class player() :
    def __init__(self) :
        self.hPMaxChar = 4
        self.hPChar = 4
        self.hurtChar = 0
        self.hurtCoolChar = 60
        self.points = 0
        
        self.colourR = 255
        self.colourG = 255
        self.colourB = 255
        
        self.dirChar = 0
        self.xPosChar = width / 2
        self.yPosChar = height / 2
        self.xSpeedChar = 0
        self.ySpeedChar = 0
        self.maxSpeedChar = 4
        self.frictionChar = 1
        self.dashSpeedChar = 4
        self.dashCoolChar = 0
        self.dashDmg = 1

    def movement(self) :
        self.xPosChar += self.xSpeedChar * self.frictionChar
        self.yPosChar += self.ySpeedChar * self.frictionChar
        self.dirChar = atan2((self.yPosChar - mouseY), (self.xPosChar - mouseX))
        
        if menus.inShop == False :
            if keyList["W"] == True and self.ySpeedChar > self.maxSpeedChar * -1 : # Up movement (W)
                self.ySpeedChar -= 0.9
            if keyList["A"] == True and self.xSpeedChar > self.maxSpeedChar * -1 : # Left movement (A)
                self.xSpeedChar -= 0.9
            if keyList["S"] == True and self.ySpeedChar < self.maxSpeedChar : # Down movement (S)
                self.ySpeedChar += 0.9
            if keyList["D"] == True and self.xSpeedChar < self.maxSpeedChar : # Right movement (D)
                self.xSpeedChar += 0.9
    
        if keyList["Space"] == True and self.dashCoolChar == 0 : # Dash (Space)
            self.frictionChar = self.dashSpeedChar
            self.dashCoolChar = 120
            
        if self.frictionChar == self.dashSpeedChar and self.dashCoolChar < 114 :
            self.frictionChar = 1

        if keyList["W"] == False and keyList["S"] == False : # Movement slowdown
            self.ySpeedChar /= 1.17
        if keyList["A"] == False and keyList["D"] == False :
            self.xSpeedChar /= 1.17
        
        if self.xPosChar < 350 : # Left / Right Camera Lock
            self.xPosChar = 350
        if self.xPosChar > 650 :
            self.xPosChar = 650

        if self.yPosChar < 260 : # Up / Down Camera Lock
            self.yPosChar = 260
        if self.yPosChar > 460 :
            self.yPosChar = 460
    
    def uI(self) :
        imageMode(CENTER)
        tint(255, 200)
        image(healthBarIn, width / 2, 30, (500 / self.hPMaxChar) * self.hPChar, 20)
        tint(255, 255)
        
        fill(255)
        textAlign(CENTER)
        text("HP : " + str(self.hPChar), width / 2, 80)
        text("Points : " + str(self.points), 200, 80)
        text("Wave : " + str(waves.waveNum), width - 200, 80)
        if menus.inShop == False :
            text("Enemies : " + str(len(enemyList)), width - 200, 120)
            if waves.waveAction == False :
                text("'E' to advance...", width - 200, 160)
        
        if self.hurtChar == 1 and self.hurtCoolChar == 0 :
            self.hPChar -= 1
            self.hurtCoolChar = 60
            hurtSoundChar.trigger()
        else :
            self.hurtChar = 0
        
        if self.hurtCoolChar > 50 :
            self.colourG = 210
            self.colourB = 210
    
    def update(self) :    
        global gameState        
        if self.dashCoolChar > 0 :
            self.dashCoolChar -= 1
        if self.hurtCoolChar > 0 :
            self.hurtCoolChar -= 1
        
        if self.colourG < 255 and self.colourB < 255 :
            self.colourG += 1
            self.colourB += 1
            
        if playerList[0].hPChar < 1 :
            deathSoundChar.trigger()
            gameState = False
            engine.death = True
            

    def render(self) :
        imageMode(CENTER)
        pushMatrix()
        fill(self.colourR, self.colourG, self.colourB)
        translate(self.xPosChar, self.yPosChar)
        rotate(self.dirChar + PI/-2)
        image(playerShape, 0, 0)
        popMatrix()

#--------------------------------------------------------------------------------------------

class enemy() :
    def __init__(self, speed) :
        self.hPEne = waves.waveNum * 1.03
        self.hurtEne = 0
        self.hurtCoolEne = 60
        self.shootCoolDown = 60
        self.canShoot = 0
        self.colourR = 255
        self.colourG = 255
        self.colourB = 255
        
        self.xPosEne = random(cameraList[0].xPosCam, cameraList[0].yPosCam + 1000)
        self.yPosEne = random(-75 - cameraList[0].yPosCam, -150 - cameraList[0].yPosCam)
        self.dirEne = 0
        self.speedEne = speed
        self.distX = 0
        self.distY = 0
        self.distEne = 0
        
    def movement(self) :
        self.dirEne = atan2((self.yPosEne + cameraList[0].yPosCam) - playerList[0].yPosChar, (self.xPosEne + cameraList[0].xPosCam) - playerList[0].xPosChar)
        self.distX = (cameraList[0].xPosCam - playerList[0].xPosChar) - self.xPosEne
        self.distY = (playerList[0].yPosChar - cameraList[0].yPosCam) - self.yPosEne
        
        if (playerList[0].xPosChar - cameraList[0].xPosCam) - self.xPosEne > 20 or (playerList[0].xPosChar - cameraList[0].xPosCam) - self.xPosEne < 20 * -1 :
            self.xPosEne += self.speedEne * cos(self.dirEne) * -1
        if (playerList[0].yPosChar - cameraList[0].yPosCam) - self.yPosEne > 20 or (playerList[0].yPosChar - cameraList[0].yPosCam) - self.yPosEne < 20 * -1:
            self.yPosEne += self.speedEne * sin(self.dirEne) * -1
            
        
        for e in enemyList :
            if dist(cameraList[0].xPosCam - self.xPosEne, cameraList[0].yPosCam - self.yPosEne, cameraList[0].xPosCam - e.xPosEne, cameraList[0].yPosCam - e.yPosEne) < 35 :
                if e != self :
                    self.xPosEne += 1
                else :
                    return
    
    def hitbox(self) :
        if dist(playerList[0].xPosChar, playerList[0].yPosChar, self.xPosEne + cameraList[0].xPosCam, self.yPosEne + cameraList[0].yPosCam) < 30 and playerList[0].dashCoolChar < 100 :
            playerList[0].hurtChar = 1
            
        if playerList[0].xPosChar - (self.xPosEne + cameraList[0].xPosCam) < 28 and playerList[0].xPosChar - (self.xPosEne + cameraList[0].xPosCam) > -28 and playerList[0].dashCoolChar > 100 and self.hurtCoolEne == 0 :
            if playerList[0].yPosChar - (self.yPosEne + cameraList[0].yPosCam) < 28 and playerList[0].yPosChar - (self.yPosEne + cameraList[0].yPosCam) > -28 and playerList[0].dashCoolChar > 100 and self.hurtCoolEne == 0 :
                self.hPEne -= playerList[0].dashDmg
                self.hurtCoolEne = 60
    
    def update(self) :
        if self.hPEne < 1 :
            playerList[0].points += 0.5
            enemyList.remove(self)
        
        if self.hurtEne == 1 :
            self.hPEne -= 1
            
        if self.hurtCoolEne > 0 :
            self.hurtCoolEne -= 1
        
        if self.colourG < 255 and self.colourB < 255 :
            self.colourG += 1
            self.colourB += 1
        
        if self.hurtCoolEne > 50 :
            self.colourG = 220
            self.colourB = 220
        
        if self.shootCoolDown > 0 :
            self.shootCoolDown -= 1

    def render(self) :
        pushMatrix()
        fill(self.colourR, self.colourG, self.colourB)
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

#--------------------------------------------------------------------------------------------

class weapon() :
    def __init__(self, weaponCool, weaponMaxCool, weaponDmg, bulletSpeed) :
        self.weaponCool = weaponCool
        self.weaponMaxCool = weaponMaxCool
        self.weaponDmg = weaponDmg
        self.bulletSpeed = bulletSpeed
        
    def movement(self) :
        self.weaponDir = playerList[0].dirChar
        self.xPosWeapon = playerList[0].xPosChar
        self.yPosWeapon = playerList[0].yPosChar
        self.xSpeedWeapon = playerList[0].xSpeedChar
        self.ySpeedWeapon = playerList[0].ySpeedChar
    
    def shooting(self) :
        if menus.inShop == False :
            if keyList["LeftMouse"] == True and self.weaponCool == 0 :
                bulletList.append(bullet(self.weaponDir, self.bulletSpeed, self.weaponDmg, self.xPosWeapon, self.yPosWeapon))
                shootSound.trigger()
                self.weaponCool = self.weaponMaxCool
    
    def update(self) :
        if self.weaponCool > 0 :
            self.weaponCool -= 1

#--------------------------------------------------------------------------------------------
            
class bullet() :
    def __init__(self, dirBullet, bulletSpeed, weaponDmg, xPos, yPos) :
        self.dirBullet = dirBullet
        self.xPosBullet = xPos
        self.yPosBullet = yPos
        self.speedBullet = bulletSpeed
        self.bulletAliveTime = 180
        self.dmgBullet = weaponDmg
        
    def movement(self) :
        if cameraList[0].movingXCam == 1 :
            self.xPosBullet -= playerList[0].xSpeedChar * playerList[0].frictionChar
        if cameraList[0].movingYCam == 1 :
            self.yPosBullet -= playerList[0].ySpeedChar * playerList[0].frictionChar
        
        self.xPosBullet += (self.speedBullet * cos(self.dirBullet) * -1)
        self.yPosBullet += (self.speedBullet * sin(self.dirBullet) * -1)
        
    def hitReg(self) :
        for e in enemyList :
            if e.xPosEne - 15 < self.xPosBullet - cameraList[0].xPosCam and e.xPosEne + 15 > self.xPosBullet - cameraList[0].xPosCam :
                if e.yPosEne - 15 < self.yPosBullet - cameraList[0].yPosCam and e.yPosEne + 15 > self.yPosBullet - cameraList[0].yPosCam and self.bulletAliveTime > 0 :
                    self.bulletAliveTime = 0
                    e.hPEne -= self.dmgBullet
                    e.colourG = 220
                    e.colourB = 220
                    hurtSoundEne.trigger()
                    
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

class waveSystem() :
    def __init__(self) :
        self.waveAction = False
        self.waveStart = False
        self.waveNum = 0
        self.speed = 1.3
    
    def waveStarting(self) :
        if keyList["E"] == True and self.waveAction == False and menus.inShop == 0 :
            self.speed += 0.2
            self.waveNum += 1
            menuSelect.trigger()
            self.waveSpawn()
    
    def waveSpawn(self) :
        for i in range(int(round(self.waveNum * 1.5))) :
            enemyList.append(enemy(self.speed))
    
    def update(self) :
        if len(enemyList) != 0 :
            self.waveAction = True
        else :
            self.waveAction = False

#--------------------------------------------------------------------------------------------

class menu() :
    def __init__(self) :
        self.menuNum = 1
        self.music = True
        self.musicCool = 30
        self.fX = True
        self.fXCool = 60
        self.inShop = False
        self.buyCool = 15
        self.enterShopCool = 30
    
    def render(self) :
        imageMode(CORNER)
        
        if self.menuNum == 1 :
            image(menuOne, 0, 0)
        if self.menuNum == 2 :
            image(menuTwo, 0, 0)
    def controls(self) :
        global gameState
        if keyList["LeftMouse"] == True and self.menuNum == 1 :
            if mouseX < width / 2 + 70 and mouseX > width / 2 - 70 :
                if mouseY < 239 + 30 and mouseY > 239 - 30 :
                    weap.weaponCool += 10
                    gameState = True
                    menuSelect.trigger()
        
        if keyList["LeftMouse"] == True and self.menuNum == 1 :
            if mouseX < width / 2 + 141 and mouseX > width / 2 - 141 :
                if mouseY < 414 + 30 and mouseY > 414 - 30 :
                    self.menuNum = 2
                    menuSelect.trigger()
                    
        if keyList["LeftMouse"] == True and self.musicCool == 0 and self.menuNum == 1 :
            if mouseX < width / 2 + 70 and mouseX > width / 2 - 70 :
                if mouseY < 587 + 30 and mouseY > 587 - 30 :
                    self.music = not self.music
                    self.musicCool = 30
                    menuSelect.trigger()
        
        if keyList["LeftMouse"] == True and self.fXCool == 0 and self.menuNum == 1 :
            if mouseX > 711 :
                if mouseY > 647 :
                    self.fX = not self.fX
                    self.fXCool = 60
                    menuSelect.trigger()
        
        if keyList["M"] == True and self.menuNum == 2 :
            self.menuNum = 1
            menuSelect.trigger()
    
    def shop(self) :
        if keyList["R"] == True and gameState == 1 and waves.waveAction == False and self.enterShopCool == 0 :
            self.enterShopCool = 30
            self.inShop = not self.inShop
            menuSelect.trigger()
        
        if self.inShop == True :
            image(menuThree, 0, 0)
            if keyList["1"] == True and self.buyCool == 0 and playerList[0].points >= 3 : #Upgrading mvt. speed.
                playerList[0].points -= 3
                playerList[0].maxSpeedChar += 0.2
                upgradeSound.trigger()
                self.buyCool = 15
            elif keyList["1"] == True and self.buyCool == 0 and playerList[0].points < 3 :
                declineSound.trigger()
                self.buyCool = 15
        
            if keyList["2"] == True and self.buyCool == 0 and playerList[0].points >= 4 and weap.weaponMaxCool > 4 : #Upgrading atk. speed.
                playerList[0].points -= 4
                weap.weaponMaxCool -= 2
                upgradeSound.trigger()
                self.buyCool = 15
            elif keyList["2"] == True and self.buyCool == 0 and playerList[0].points < 4 :
                declineSound.trigger()
                self.buyCool = 15
                
            if keyList["3"] == True and self.buyCool == 0 and playerList[0].points >= 4 : #Upgrading atk. dmg.
                playerList[0].points -= 4
                weap.weaponDmg += 1.5
                upgradeSound.trigger()
                self.buyCool = 15
            elif keyList["3"] == True and self.buyCool == 0 and playerList[0].points < 4 :
                declineSound.trigger()
                self.buyCool = 15
    
            if keyList["4"] == True and self.buyCool == 0 and playerList[0].points >= 4 : #Upgrading dash dmg.
                playerList[0].points -= 4
                playerList[0].dashDmg += 1.5
                upgradeSound.trigger()
                self.buyCool = 15
            elif keyList["4"] == True and self.buyCool == 0 and playerList[0].points < 4 :
                declineSound.trigger()
                self.buyCool = 15
            
            if keyList["5"] == True and self.buyCool == 0 and playerList[0].points >= 1 and playerList[0].hPChar < 4 : #Heal 1 HP.
                playerList[0].points -= 1
                playerList[0].hPChar += 1
                upgradeSound.trigger()
                self.buyCool = 15
            elif keyList["5"] == True and self.buyCool == 0 and playerList[0].points < 1 or keyList["5"] == True and self.buyCool == 0 and playerList[0].hPChar >= 4 :
                declineSound.trigger()
                self.buyCool = 15
    
    def musicPlay(self) :
        if gameState == False and engine.death == False :
            mainTheme.setGain(0)
        elif engine.death == True :
            mainTheme.setGain(-1000)
        else :
            mainTheme.setGain(-20)
            
        if self.music == True :
            mainTheme.play()
        else :
            mainTheme.pause()
        
        if mainTheme.position() == mainTheme.length() :
            mainTheme.rewind()

    def update(self) :
        if self.musicCool > 0 :
            self.musicCool -= 1
        if self.fXCool > 0 :
            self.fXCool -= 1
        if self.enterShopCool > 0 :
            self.enterShopCool -= 1
        if self.buyCool > 0 :
            self.buyCool -= 1

#--------------------------------------------------------------------------------------------

class renderingEngine() :
    def __init__(self) :
        global minim, healthBarIn
        self.blurPass = 0
        self.rgbPass = 25
        self.restart = 0
        self.death = False
        
    def engineVars(self) :
        if self.blurPass > 0 :
            self.blurPass -= 1
        if self.rgbPass > 25 :
            self.rgbPass -= 1
            
    def load(self) :
        return
    
    def updateObjects(self) :
        if gameState == True and self.death == False :
            playerList[0].movement()
            playerList[0].update()
            
            weap.movement()
            weap.shooting()
            weap.update()
            
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
        background(200)
        
    def renderObjects(self) :
        if gameState == True and self.death == False :
            waves.waveStarting()
            waves.update()
            
            for b in bulletList :
                b.render()
                
            playerList[0].render()
            
            for e in enemyList :
                e.render()
            
            menus.shop()
            
            playerList[0].uI()
            
        if gameState == False and self.death == False :
            menus.render()
            menus.controls()
            
        menus.update()
        menus.musicPlay()
    
    def deathScreen(self) :
        if self.death == True :
            image(menuFour, 0, 0)
            if keyList["LeftMouse"] == True :
                exit()
    
    def postProcessing(self) :
        imageMode(CORNER)
        if menus.fX == True :
            fx.render().vignette(0.55, 0.55).rgbSplit(self.rgbPass).compose()
            fx.render().blur(self.blurPass, self.blurPass).compose()
        else :
            fx.render().compose()

#--------------------------------------------------------------------------------------------

keyList = {"W" : False, "A" : False, "S" : False, "D" : False, "E" : False, "M" : False, "R" : False, "Space" : False, "LeftMouse" : False, "1" : False, "2" : False, "3" : False, "4" : False, "5" : False}
playerList = []
bulletList = []
enemyList = []
cameraList = []
menus = menu()
engine = renderingEngine()
waves = waveSystem()
gameState = False
minim = Minim(this)

#--------------------------------------------------------------------------------------------

def setup() :
    global fx, mainTheme, menuSelect, upgradeSound, declineSound, shootSound, hurtSoundEne, hurtSoundChar, deathSoundChar, healthBarIn, mV, menuOne, menuTwo, menuThree, menuFour, playerShape, weap
    size(1000, 720, P2D)
    smooth(4)
    
    mainTheme = minim.loadFile("assets\\sounds\\mainTheme16Bit.wav")
    menuSelect = minim.loadSample("assets\\sounds\\menuSelect.wav")
    upgradeSound = minim.loadSample("assets\\sounds\\upgradeSound.wav")
    declineSound = minim.loadSample("assets\\sounds\\declineSound.wav")
    shootSound = minim.loadSample("assets\\sounds\\shootSound.wav")
    hurtSoundEne = minim.loadSample("assets\\sounds\\hurtSoundEne.wav")
    hurtSoundChar = minim.loadSample("assets\\sounds\\hurtSoundChar.wav")
    deathSoundChar = minim.loadSample("assets\\sounds\\deathSoundChar.wav")
    
    healthBarIn = loadImage('assets\\textures\\healthBarIn.png')
    menuOne = loadImage('assets\\textures\\menus\\menuScreenOne.png')
    menuTwo = loadImage('assets\\textures\\menus\\menuScreenTwo.png')
    menuThree = loadImage('assets\\textures\\menus\\menuScreenThree.png')
    menuFour = loadImage('assets\\textures\\menus\\menuScreenFour.png')
    playerShape = loadImage('assets\\textures\\char.png')
    
    ralewayFont = createFont("assets\\fonts\\Raleway-ExtraLight.ttf", 35)
    textFont(ralewayFont)
    
    engine.load()
    
    weap = weapon(1, 36, 1, 8)
    
    fx = PostFX(this)
    fx.preload(BloomPass)
    fx.preload(RGBSplitPass)
    fx.preload(VignettePass)
    
#--------------------------------------------------------------------------------------------

def draw() :
    global temp
    if len(cameraList) == 0 :
        cameraList.append(cameraPlayer())
    if len(playerList) == 0 :
        playerList.append(player())
    
    engine.renderEnvironment()
    engine.updateObjects()
    engine.renderObjects()
    engine.postProcessing()
    engine.engineVars()
    engine.deathScreen()

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
    if key == "e" :
        keyList["E"] = True
    if key == "m" :
        keyList["M"] = True
    if key == "r" :
        keyList["R"] = True
    if key == " " :
        keyList["Space"] = True

    if key == "1" :
        keyList["1"] = True
    if key == "2" :
        keyList["2"] = True
    if key == "3" :
        keyList["3"] = True
    if key == "4" :
        keyList["4"] = True
    if key == "5" :
        keyList["5"] = True

def keyReleased() :
    if key == "w" :
        keyList["W"] = False
    if key == "a" :
        keyList["A"] = False
    if key == "s" :
        keyList["S"] = False
    if key == "d" :
        keyList["D"] = False
    if key == "e" :
        keyList["E"] = False
    if key == "m" :
        keyList["M"] = False
    if key == "r" :
        keyList["R"] = False
    if key == " " :
        keyList["Space"] = False
        
    if key == "1" :
        keyList["1"] = False
    if key == "2" :
        keyList["2"] = False
    if key == "3" :
        keyList["3"] = False
    if key == "4" :
        keyList["4"] = False
    if key == "5" :
        keyList["5"] = False

def mousePressed() :
    if mouseButton == LEFT :
        keyList["LeftMouse"] = True

def mouseReleased() :
    if mouseButton == LEFT :
        keyList["LeftMouse"] = False
