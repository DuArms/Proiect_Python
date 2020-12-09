
from UserInteraction.MenuArea import *

# pygame.mixer.init()
# pygame.mixer.music.load("./resurse/song.mp3")
# pygame.mixer.music.play(-1)

pygame.display.set_caption("TrapTheMouse")
pygame.display.set_icon(GameGUI.poza_soarece)

if __name__ == "__main__":
    draweble_table = init_game()

    # Run until the user asks to quit
    running = True
    while running:

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_pozition = pygame.mouse.get_pos()

                if    in_pyrect(game_gui.game_area,mouse_pozition):
                    game_table_click(game_gui, mouse_pozition,opponent_lvl)

                if  in_pyrect(game_gui.menu_area,mouse_pozition):
                  game_gui , opponent_lvl = menu_click(mouse_pozition,game_gui)

        game_gui.draw()

    # print(pygame.mouse.get_pos())

    # running = False

    # Done! Time to quit.
    pygame.quit()
