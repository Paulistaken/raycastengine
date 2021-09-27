import pygame, os
win = pygame.display.set_mode((700,700))
pygame.display.set_icon(pygame.image.load(os.path.join("assets", "icon.png")).convert())
pygame.display.set_caption("Level Edit Mode")
run = True
clock = pygame.time.Clock()
pygame.font.init()
def maketext(text, size):
    font = pygame.font.SysFont("Arial", size)
    nmb = str(text)
    nmb_text = font.render(nmb, 100, pygame.Color("white"))
    return nmb_text
map = []
ui = True
def loadlevel():
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
class buttonclass:
    def __init__(self, pos, type="Loadlevel"):
        self.pos = pos
        self.type = type
    def update(self, screen):
        global map
        global ui
        if self.type == "Loadlevel":
           mpx, mpy = pygame.mouse.get_pos()
           m1, m2, m3 = pygame.mouse.get_pressed()
           mouserect = pygame.Rect(mpx - 25, mpy - 25, 50, 50)
           if mouserect.colliderect(self.pos):
               pygame.draw.rect(screen, (0, 255, 0), self.pos)
               if m1:
                   loadlevel()
                   ui = False
           else:
               pygame.draw.rect(screen, (255, 0, 0), self.pos)
           screen.blit(maketext("Load Level!", 64), (self.pos.x, self.pos.y))
        if self.type == "9x9":
            mpx, mpy = pygame.mouse.get_pos()
            m1, m2, m3 = pygame.mouse.get_pressed()
            mouserect = pygame.Rect(mpx - 25, mpy - 25, 50, 50)
            if mouserect.colliderect(self.pos):
                pygame.draw.rect(screen, (0, 255, 0), self.pos)
                if m1:
                    for y in range(9):
                        row = []
                        for x in range(9):
                            if y == 0 or x == 0 or y == 8 or x == 8:
                                row.append(1)
                            else:
                                row.append(0)
                        map.append(row)
                    ui = False
            else:
                pygame.draw.rect(screen, (255, 0, 0), self.pos)
            screen.blit(maketext("9x9!", 64), (self.pos.x, self.pos.y))
        if self.type == "18x18":
            mpx, mpy = pygame.mouse.get_pos()
            m1, m2, m3 = pygame.mouse.get_pressed()
            mouserect = pygame.Rect(mpx - 25, mpy - 25, 50, 50)
            if mouserect.colliderect(self.pos):
                pygame.draw.rect(screen, (0, 255, 0), self.pos)
                if m1:
                    for y in range(18):
                        row = []
                        for x in range(18):
                            if y == 0 or x == 0 or y == 17 or x == 17:
                                row.append(1)
                            else:
                                row.append(0)
                        map.append(row)
                    ui = False
            else:
                pygame.draw.rect(screen, (255, 0, 0), self.pos)
            screen.blit(maketext("18x18!", 64), (self.pos.x, self.pos.y))
        if self.type == "27x27":
            mpx, mpy = pygame.mouse.get_pos()
            m1, m2, m3 = pygame.mouse.get_pressed()
            mouserect = pygame.Rect(mpx - 25, mpy - 25, 50, 50)
            if mouserect.colliderect(self.pos):
                pygame.draw.rect(screen, (0, 255, 0), self.pos)
                if m1:
                    for y in range(27):
                        row = []
                        for x in range(27):
                            if y == 0 or x == 0 or y == 26 or x == 26:
                                row.append(1)
                            else:
                                row.append(0)
                        map.append(row)
                    ui = False
            else:
                pygame.draw.rect(screen, (255, 0, 0), self.pos)
            screen.blit(maketext("27x27!", 64), (self.pos.x, self.pos.y))
py = 0
px = 0
loadlevelbutton = buttonclass(pygame.Rect(100, 100, 300, 100))
a9by9button = buttonclass(pygame.Rect(100, 220, 300, 100), "9x9")
a18by18button = buttonclass(pygame.Rect(100, 340, 300, 100), "18x18")
a27by27button = buttonclass(pygame.Rect(100, 460, 300, 100), "27x27")
while ui:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ui = False
    clock.tick(60)
    win.fill((0,0,0))
    loadlevelbutton.update(win)
    a9by9button.update(win)
    a18by18button.update(win)
    a27by27button.update(win)
    pygame.display.update()
ppx = 0
ppy = 0
while run:
    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_d]:
        ppx += 10
    if key_pressed[pygame.K_a]:
        ppx -= 10
    if key_pressed[pygame.K_w]:
        ppy -= 10
    if key_pressed[pygame.K_s]:
        ppy += 10
    mpx, mpy = pygame.mouse.get_pos()
    m1, m2, m3 = pygame.mouse.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    clock.tick(60)
    win.fill((0,0,0))
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == 1:
                pygame.draw.rect(win, (255, 255, 255), pygame.Rect(x * 50 - ppx, y * 50 - ppy, 50, 50))
            else:
                if x % 2 == 0 and y % 2 == 1:
                    pygame.draw.rect(win, (100, 100, 100), pygame.Rect(x * 50 - ppx, y * 50 - ppy, 50, 50))
                elif x % 2 == 1 and y % 2 == 0:
                    pygame.draw.rect(win, (100, 100, 100), pygame.Rect(x * 50 - ppx, y * 50 - ppy, 50, 50))
                else:
                    pygame.draw.rect(win, (50, 50, 50), pygame.Rect(x * 50 - ppx, y * 50 - ppy, 50, 50))
    if mpx+ppx >= 0 and mpx+ppx <= len(map[0])*50 and mpy+ppy >= 0 and mpy+ppy <= len(map)*50:
        pygame.draw.rect(win, (0, 255, 0), pygame.Rect(mpx-12.5, mpy-12.5, 25, 25))
        try:
            if m1:
                map[int((mpy + ppy) / 50)][int((mpx + ppx) / 50)] = 1
            if m3:
                map[int((mpy + ppy) / 50)][int((mpx + ppx) / 50)] = 0
        except:
            pass
    else:
        pygame.draw.rect(win, (255, 0, 0), pygame.Rect(mpx-12.5, mpy-12.5, 25, 25))
    pygame.display.update()
with open(os.path.join("level.txt"), "w") as f:
    for y in map:
        for x in y:
            f.write(str(x))
        f.writelines('\n')