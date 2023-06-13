import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    kokaton = pg.image.load("ex01/fig/3.png")
    kokaton = pg.transform.flip(kokaton, True, False)
    angle = 0
    angle_mode = 0
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [-(tmr % 1600), 0])
        if angle_mode == 0:
            angle += 0.1
        else:
            angle -= 0.1
        
        if angle >= 10:
            angle_mode = 1
        elif angle <= 0:
            angle_mode = 0
        kokaton_display = pg.transform.rotozoom(kokaton, angle, 1.0)
        screen.blit(kokaton_display, [300, 200])
        pg.display.update()
        tmr += 1        
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()