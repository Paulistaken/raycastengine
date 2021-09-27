import pygame, math, os, spritesheet, random
win = pygame.display.set_mode((700,700))
pygame.display.set_icon(pygame.image.load(os.path.join("assets", "icon.png")).convert())
pygame.display.set_caption("Game Mode")
pygame.font.init()
os.path.dirname("raytracerengine-v.01-alpha")
gunimges = spritesheet.spritesheet(os.path.join("assets", "gunsprts.png"))
map = []
gunstate = 0
with open(os.path.join("level.txt"), "r") as f:
       rows = f.readlines()
       for x in rows:
              row = x[:-1]
              arow = []
              for z in row:
                     if z == "1":
                            arow.append(1)
                     else:
                            arow.append(0)
              map.append(arow)
colormap = []
for y in range(len(map)):
       row = []
       for x in range(len(map[y])):
              if map[y][x] == 1:
                     row.append((random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)))
              else:
                     row.append((0,0,0))
       colormap.append(row)
class vekt:
    def __init__(self, x, y, z, px, py, pz):
        self.x = x
        self.y = y
        self.z = z
        self.sx = px
        self.sy = py
        self.sz = pz
    def coll2d(self, ov):
        if self.x + self.sx > ov.x and self.x < ov.x + ov.sx and self.y + self.sy > ov.y and self.y < ov.y + ov.sy:
            return True
        return False
def moveangle(angle,speed):
    diry = math.sin(math.radians(angle))
    dirx = math.cos(math.radians(angle))
    dirs = vekt(dirx*speed,diry*speed,0,0,0,0)
    return dirs
run = True
clock = pygame.time.Clock()
showminimap = True
boxes = []
pygame.display.set_allow_screensaver(True)
def update_fps():
       font = pygame.font.SysFont("Arial", 18)
       fps = str(int(clock.get_fps()))
       fps_text = font.render(fps, 1, pygame.Color("coral"))
       return fps_text
def update_ammo():
       font = pygame.font.SysFont("Arial", 48)
       nmb = str(player.ammo)
       nmb_text = font.render(nmb, 100, pygame.Color("white"))
       return nmb_text
def maketext(text, size):
    font = pygame.font.SysFont("Arial", size)
    nmb = str(text)
    nmb_text = font.render(nmb, 100, pygame.Color("white"))
    return nmb_text
for y in range(len(map)):
       for x in range(len(map[y])):
              if map[y][x] == 1:
                     boxes.append(vekt(x*100,y*100,0,100,100,100))
def getwallcols():
       for x in boxes:
              if x.coll2d(vekt(playerpos.x + 25, playerpos.y + 25, 0, 50, 50, 50)):
                     return True
       return False
class playerclass:
       def __init__(self, pos, rot, speed):
              self.pos = pos
              self.rot = rot
              self.speed = speed
              self.maxspeed = speed
              self.maxshootdelay = 15
              self.shootdelay = 0
              self.ammo = 8
              self.ammoanimdir = 0
              self.ammoanimstate = 0
              self.rlddelay = 0
              self.zstate = 0.8
              self.walkdelaytype = 0
              self.zrot = 0
              self.sensitivity = 0.8
              self.maxsensitivity = 0.8
              self.gunposz = 0
              self.akimbo = False
       def update(self):
              self.gunposz = 0
              global gunstate
              moving = False
              self.pos.z = self.zstate + self.zrot
              gunstate = 0
              playerrot = self.rot
              playerpos = self.pos
              self.sensitivity = self.maxsensitivity
              m1, m2, m3 = pygame.mouse.get_pressed()
              self.speed = self.maxspeed
              if m3:
                     self.speed = self.maxspeed/2
                     self.sensitivity = self.sensitivity * 4
              if m1:
                     self.speed = self.maxspeed / 1.5
              if key_pressed[pygame.K_UP]:
                     self.maxsensitivity += 0.01
              if key_pressed[pygame.K_DOWN]:
                     self.maxsensitivity -= 0.01
              if key_pressed[pygame.K_LEFT]:
                     playerrot += 3
              if key_pressed[pygame.K_RIGHT]:
                     playerrot -= 3
              if key_pressed[pygame.K_w]:
                     dirs = moveangle(playerrot, player.speed)
                     playerpos.x += dirs.x
                     if getwallcols():
                            playerpos.x -= dirs.x
                     playerpos.y += dirs.y
                     if getwallcols():
                            playerpos.y -= dirs.y
                     moving = True
              if key_pressed[pygame.K_s]:
                     dirs = moveangle(playerrot, player.speed)
                     playerpos.x -= dirs.x
                     if getwallcols():
                            playerpos.x += dirs.x
                     playerpos.y -= dirs.y
                     if getwallcols():
                            playerpos.y += dirs.y
                     moving = True
              if key_pressed[pygame.K_a]:
                     dirs = moveangle(playerrot - 90, player.speed)
                     playerpos.x -= dirs.x
                     if getwallcols():
                            playerpos.x += dirs.x
                     playerpos.y -= dirs.y
                     if getwallcols():
                            playerpos.y += dirs.y
                     moving = True
              pygame.mouse.set_pos((350, 350))
              pygame.mouse.set_visible(False)
              mpx, mpy = pygame.mouse.get_pos()
              distx = 350 - mpx
              disty = 350 - mpy
              playerrot += distx / self.sensitivity
              self.zrot += disty / (self.sensitivity/3)
              if self.zrot > 700:
                     self.zrot = 700
              if self.zrot < -700:
                     self.zrot = -700
              if key_pressed[pygame.K_d]:
                     dirs = moveangle(playerrot + 90, player.speed)
                     playerpos.x -= dirs.x
                     if getwallcols():
                            playerpos.x += dirs.x
                     playerpos.y -= dirs.y
                     if getwallcols():
                            playerpos.y += dirs.y
                     moving = True
              if moving:
                     if self.walkdelaytype == 0:
                            if self.zstate >= -3:
                                   self.zstate -= 0.5
                            else:
                                   self.walkdelaytype = 1
                     elif self.walkdelaytype == 1:
                            if self.zstate <= 3:
                                   self.zstate += 0.5
                            else:
                                   self.walkdelaytype = 0
              if key_pressed[pygame.K_r]:
                     self.ammo = 0
              if key_pressed[pygame.K_RCTRL] or m1:
                     if self.ammo >= 1:
                            if self.shootdelay <= 0:
                                   self.shootdelay = self.maxshootdelay
                                   self.ammo -= 1
              if self.shootdelay > 0:
                     if self.shootdelay >= self.maxshootdelay - 1:
                            gunstate = 1
                            self.pos.z += 2
                            self.gunposz = -15
                     elif self.shootdelay >= self.maxshootdelay - 6:
                            gunstate = 2
                            self.pos.z += -2
                            self.gunposz = -30
                     elif self.shootdelay >= self.maxshootdelay - 8:
                            gunstate = 1
                            self.pos.z += 2
                            self.gunposz = -15
                     self.shootdelay -= 1
              else:
                     if self.ammo <= 0:
                            if self.rlddelay % 2 == 0:
                                   if self.ammoanimdir == 0:
                                          self.ammoanimstate += 1
                                          if self.ammoanimstate >= 12:
                                                 self.ammoanimdir = 1
                                   else:
                                          self.ammoanimstate -= 1
                                          if self.ammoanimstate <= 0:
                                                 self.ammo = 8
                            self.rlddelay += 1
                            gunstate = self.ammoanimstate
              if self.ammo > 0:
                     self.rlddelay = 0
                     self.ammoanimstate = 0
                     self.ammoanimdir = 0
              self.rot = playerrot
              self.pos = playerpos
              self.gunposz -= self.zstate
player = playerclass(vekt(100,100,0,100, 100, 100), 90, 5)
ui = True
class buttonclass:
    def __init__(self, pos, type="Play"):
        self.pos = pos
        self.type = type
    def update(self, screen):
        global map
        global ui
        if self.type == "Play":
            mpx, mpy = pygame.mouse.get_pos()
            m1, m2, m3 = pygame.mouse.get_pressed()
            mouserect = pygame.Rect(mpx - 25, mpy - 25, 50, 50)
            if mouserect.colliderect(self.pos):
                pygame.draw.rect(screen, (0, 255, 0), self.pos)
                if m1:
                    ui = False
            else:
                pygame.draw.rect(screen, (255, 0, 0), self.pos)
            screen.blit(maketext("Play!!!", 64), (self.pos.x, self.pos.y))
playbutton = buttonclass(pygame.Rect(200,150,300,100))
while ui:
       m1, m2, m3 = pygame.mouse.get_pressed()
       mpx, mpy = pygame.mouse.get_pos()
       for event in pygame.event.get():
              if event.type == pygame.QUIT:
                     ui = False
       clock.tick(60)
       win.fill((0,0,0))
       key_pressed = pygame.key.get_pressed()
       playbutton.update(win)
       win.blit(maketext("3d rendering test!!!", 100), (10, 0))
       win.blit(maketext("I know the ui is teribly bad", 50), (10, 300))
       win.blit(maketext("It is just a test", 50), (10, 370))
       win.blit(maketext("Sincerly - the maker", 50), (10, 440))
       win.blit(maketext("Controls:", 30), (10, 500))
       win.blit(maketext("Movement-AWSD, Lookind around-Mouse or LEFT and RIGHT arrows;", 25), (10, 560))
       win.blit(maketext("Shooting-M1 or ctrl, Aiming-M2, Sensitivity- UP and DOWN arrows;", 25), (10, 620))
       if key_pressed[pygame.K_ESCAPE]:
              ui = False
       pygame.display.update()
while run:
       m1, m2, m3 = pygame.mouse.get_pressed()
       playerpos = player.pos
       playerrot = player.rot
       florpos = playerpos.z + 350
       for event in pygame.event.get():
              if event.type == pygame.QUIT:
                     run = False
       clock.tick(60)
       win.fill((0,0,0))
       pygame.draw.rect(win, (64, 64, 64), pygame.Rect(0, florpos, 3000, 3000))
       pygame.draw.rect(win, (84, 84, 84), pygame.Rect(0, 0, 3000, florpos))
       key_pressed = pygame.key.get_pressed()
       if key_pressed[pygame.K_ESCAPE]:
              run = False
       player.update()
       showminimap = False
       if key_pressed[pygame.K_m]:
              showminimap = True
       rays = []
       if m3:
              for x in range(35):
                     dirs = moveangle(playerrot - x + 17.5, 5)
                     raypos = vekt(playerpos.x + 50, playerpos.y + 50, playerpos.z, 0, 0, 0)
                     doshow = True
                     for z in range(800):
                            if z >= 600 and x % 6 == 0:
                                   break
                            if doshow:
                                   raypos.x += dirs.x
                                   raypos.y += dirs.y
                                   if map[int(raypos.y / 100)][int(raypos.x / 100)]:
                                          if z >= 1:
                                                 sizey = (5500 / (z / 3))*2
                                                 color = colormap[int(raypos.y / 100)][int(raypos.x / 100)]
                                                 color = (color[0] / (z / 20), color[1] / (z / 20), color[2] / (z / 20))
                                          else:
                                                 sizey = 700
                                                 color = colormap[int(raypos.y / 100)][int(raypos.x / 100)]
                                          if color[0] > 255:
                                                 color = (255, color[1], color[2])
                                          if color[1] > 255:
                                                 color = (color[0], 255, color[2])
                                          if color[2] > 255:
                                                 color = (color[0], color[1], 255)
                                          pygame.draw.rect(win, color,
                                                           pygame.Rect(x * 20, 350 - (sizey/2) + playerpos.z, 20,
                                                                       sizey))
                                          doshow = False
                                   if showminimap:
                                          rays.append(pygame.Rect(raypos.x - playerpos.x + 300,
                                                                  raypos.y - playerpos.y + 300, 10, 10))
                            else:
                                   break
       else:
              for x in range(70):
                     dirs = moveangle(playerrot - x + 35, 5)
                     raypos = vekt(playerpos.x + 50, playerpos.y + 50, playerpos.z, 0, 0, 0)
                     doshow = True
                     for z in range(800):
                            if z >= 400 and x % 24 == 0:
                                   break
                            if z >= 600 and x % 12 == 0:
                                   break
                            if doshow:
                                   raypos.x += dirs.x
                                   raypos.y += dirs.y
                                   if map[int(raypos.y / 100)][int(raypos.x / 100)]:
                                          if z >= 1:
                                                 sizey = 5500 / (z / 3)
                                                 color = colormap[int(raypos.y / 100)][int(raypos.x / 100)]
                                                 color = (color[0] / (z / 20), color[1] / (z / 20), color[2] / (z / 20))
                                          else:
                                                 sizey = 700
                                                 color = colormap[int(raypos.y / 100)][int(raypos.x / 100)]
                                          if color[0] > 255:
                                                 color = (255, color[1], color[2])
                                          if color[1] > 255:
                                                 color = (color[0], 255, color[2])
                                          if color[2] > 255:
                                                 color = (color[0], color[1], 255)
                                          pygame.draw.rect(win, color,
                                                           pygame.Rect(x * 10, 350 - (sizey / 2) + playerpos.z, 10,
                                                                       sizey))
                                          doshow = False
                                   if showminimap:
                                          rays.append(pygame.Rect(raypos.x - playerpos.x + 300,
                                                                  raypos.y - playerpos.y + 300, 10, 10))
                            else:
                                   break
       gunimg = gunimges.image_at((gunstate * 28, 0, 28, 28), -1)
       gunimg = pygame.transform.scale(gunimg, (700, 700))
       if m3:
              gunimg = pygame.transform.scale(gunimg, (1400, 1400))
              win.blit(gunimg, (-350, player.gunposz - 350))
       else:
              gunimg = pygame.transform.scale(gunimg, (700, 700))
              win.blit(gunimg, (0, player.gunposz + 20))
       if showminimap:
              for y in range(len(map)):
                     for x in range(len(map[y])):
                            if map[y][x] == 1:
                                   pygame.draw.rect(win, (255, 255, 255), pygame.Rect((x * 100) - playerpos.x + 300, (y * 100) - playerpos.y + 300, 100, 100))
              pygame.draw.rect(win, (0, 0, 255), pygame.Rect(playerpos.x - playerpos.x + 325, playerpos.y - playerpos.y + 325, 50, 50))
              for x in rays:
                     pygame.draw.rect(win, (255,0,0),x)
       win.blit(update_fps(), (10, 0))
       win.blit(update_ammo(), (600, 600))
       win.blit(maketext(f'Sensitivity:{player.sensitivity}', 16), (300, 0))
       pygame.display.update()
pygame.quit()