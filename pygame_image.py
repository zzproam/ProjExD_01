import sys
import pygame as pg
def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")  # 練習１：背景画像Surfaceの生成
    bg_img_2=pg.transform.flip(bg_img, True, False)
    kk_img = pg.image.load("ex01/fig/3.png")  # 練習２：こうかとん画像Surfaceの生成
    kk_img = pg.transform.flip(kk_img, True, False)  # 練習２：こうかとんの左右反転
    kk_imgs = [kk_img, pg.transform.rotozoom(kk_img, 10, 1.0)]  # 練習３：こうかとんSurfaceのリスト
    
    tmr = 0
    bird_deg=0
    count=0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x = tmr%3200  # 練習６：動く背景画像
        screen.blit(bg_img, [-x, 0])  # 練習４：背景画像の表示
        screen.blit(bg_img_2, [1600-x, 0])  # 練習６：動く背景画像
        screen.blit(bg_img_2, [3200-x, 0])
        screen.blit(bg_img, [3200-x, 0])
        screen.blit(kk_imgs[bird_deg], [300, 200])  # 練習５：こうかとんはばたく
        print(-x,1600-x,bird_deg)
        pg.display.update()
        
            
        tmr += 1
       
            
        count+=1
        if bird_deg==0 and count%20==0:
            bird_deg=1
        elif bird_deg==1 and count%20==0:
            bird_deg=0
        clock.tick(10000)
        


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()