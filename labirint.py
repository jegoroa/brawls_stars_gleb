from pygame import*

BLACK = (0, 0, 0)

class BasicSpite(sprite.Sprite):
    def __init__(self,x,y,w,h,filename):
        self.image = image.load(filename)
        self.image = transform.scale(self.image,(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.xspeed = 0
        self.yspeed = 0

    def draw(self):
        win.blit(self.image,(self.rect.x,self.rect.y))


class Hero(BasicSpite):
    def wall_check(self,dx,dy):
        self.check_rect = Rect(self.rect.x+dx,
                        self.rect.y-dy,
                        self.rect.width,self.rect.height)

        for wall in walls:
            if wall.rect.colliderect(self.check_rect):
                return True
        return False

    def update(self):    
        keys = key.get_pressed()

        if keys[K_a]: self.xspeed = -1.5
        elif keys[K_d]: self.xspeed = 1.5
        else: self.xspeed = 0

        if keys[K_w]: self.yspeed = 1.5
        elif keys[K_s]: self.yspeed = -1.5
        else: self.yspeed = 0

        if not self.wall_check(self.xspeed,self.yspeed):
            self.rect.x += self.xspeed
            self.rect.y -= self.yspeed
        
        self.draw()

class Enemy(BasicSpite):
    def update(self):
        self.rect.x += self.xspeed
        if self.rect.x > 1300 or self.rect.x < 0:
            self.xspeed = -self.xspeed
        self.rect.y += self.yspeed
        if self.rect.y > 720 or self.rect.y < 260:
            self.yspeed = -self.yspeed
        if self.rect.colliderect(gg.rect):
            exit()

        self.draw()

class Finish(BasicSpite):
    def update(self):
        if self.rect.colliderect(gg.rect):
            end_game()

        self.draw()    

class Wall(sprite.Sprite):
    def __init__(self, x, y, w, h):
        super().__init__()
        walls.add(self)
        self.rect = Rect(x,y,w,h)

    def update(self):
        draw.rect(win, RED, self.rect)


BLUE = (18, 39, 224)
RED = (250, 0, 0)

gg = Hero(x=0,y=0,w=100,h=80,filename="hero.png") 
finish = Finish(1200,630,100,100,filename='Finish.png')
vrag = Enemy(600,260,100,100,filename='bull.png')
vrag2 = Enemy(20,260,100,100,filename='bull.png')
vrag.xspeed = 1
vrag2.yspeed = 1
walls = sprite.Group()
Wall(x=300,y=50,w=1400,h=40)
Wall(x=0,y=220,w=1100,h=40)
Wall(x=300,y=380,w=1300,h=40)
Wall(x=925,y=400,w=40,h=200)
Wall(x=145,y=560,w=785,h=40)


win = display.set_mode((1920,1080))

def end_game():
    global game_finished
    game_finished = True


game_finished = False
finish_pic = image.load('boss.jpg')
finish_pic = transform.scale(finish_pic,(1366,768))

while True:

    for e in event.get():
        if e.type ==QUIT:
            exit()
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                exit()

    win.fill(BLACK)
    gg.update()  

    walls.update()
    finish.update()
    vrag.update()
    vrag2.update()

    if game_finished:
        win.blit(finish_pic,(0,0))

    display.update()
    


