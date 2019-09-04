import pygame as pg


def update_screen():
    pg.display.flip()


def update_background(screen):
    screen.fill((105, 105, 105))


def main():
    pg.init()
    logo = pg.image.load("icon.png")
    pg.display.set_icon(logo)
    pg.display.set_caption("Game")
    screen = pg.display.set_mode((500, 500))
    running = True
    update_background(screen)
    update_screen()

    # Main Loop
    while running:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                
                if pg.key.get_pressed()[pg.K_ESCAPE]:  # Simple Player Exit
                    running = False
            if event.type == pg.QUIT:
                running = False


if __name__ == "__main__":
    main()
