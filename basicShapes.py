from curses.ascii import isblank
import pygame as p

def setup():
    global screen, clock
    p.init()
    # Screen resolution
    screen = p.display.set_mode((600, 600))
    clock = p.time.Clock()
    
def main():
    done = False
    isBlue = True
    color = ((0,0,0))
    while not done:
        screen.fill((0,0,0))
        #go through event queue
        for e in p.event.get():
            if e.type == p.QUIT:
                done = True
            if e.type == p.KEYDOWN and e.key == p.K_DOWN:
                isBlue = not isBlue
        if (isBlue):
            color = ((0,0,255))
        else:
            color = ((0,0,0))
        rectangle1 = p.Rect(0,0,400,200)
        p.draw.rect(screen, color, rectangle1)
        p.display.flip() #redraws the display
        clock.tick(30) #30fps
    
setup()
main()