import pgzrun
from random import randint
WIDTH=600
HEIGHT=600
TITLE='Shoot the Alien'

message= ""
score= 0

Sprite= Actor ('alien')
def draw ():
    screen.clear()
    screen.fill('DARK BLUE')
    Sprite.draw()
    screen.draw.text(message,center=(400,10),fontsize=30)
    screen.draw.text('score ='+str(score),center=(50,10),fontsize=30)

def placealien ():
    Sprite.x=randint(50,(WIDTH-50))
    Sprite.y=randint(50,(HEIGHT-50))

def on_mouse_down (pos):
    global message
    global score
    if Sprite.collidepoint(pos):
        message="Good Shot!"
        score=score + 1
    else:
        message="You Missed!"
        score=score - 1



def update ():
    pass
placealien()
pgzrun.go()