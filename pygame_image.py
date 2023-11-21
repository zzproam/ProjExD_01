import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((900, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bg_img_2 = bg_img
    bird = pg.image.load("ex01/fig/3.png")
    bird = pg.transform.flip(bird,True,False)
    bird = [bird,pg.transform.rotozoom(bird, 10, 1.0)]
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x = tmr%1600
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img_2, [1600-x, 0])
        screen.blit(bird[tmr%2],[300,200])
        pg.display.update()
        tmr += 1        
        clock.tick(100)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()