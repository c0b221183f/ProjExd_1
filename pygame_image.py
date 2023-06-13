import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bg_img_2 = pg.image.load("ex01/fig/pg_bg.jpg")
    bg_img_2 = pg.transform.flip(bg_img_2, True, False)
    kokaton = pg.image.load("ex01/fig/3.png")
    kokaton = pg.transform.flip(kokaton, True, False)
    angle = 0
    angle_mode = 0
    bg_x = 0
    bg_x_2 = 1600
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return


        #display bg
        bg_x -= 1
        bg_x_2 -= 1
        screen.blit(bg_img, [bg_x, 0])
        screen.blit(bg_img_2, [bg_x_2, 0])

        if bg_x <= -1600 :
            bg_x = 1600
        if bg_x_2 <= -1600:
            bg_x_2 = 1600


        # display kokaton
        if angle_mode == 0:
            angle += 0.25
        else:
            angle -= 0.25
        
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