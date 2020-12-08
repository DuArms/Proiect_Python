from UserInteraction.GameBoardArea import *
from UserInteraction.MenuArea import *



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

                if    in_pyrect(game_area,mouse_pozition):
                    game_table_click(hex_crd, mouse_pozition)

                if  in_pyrect(menu_area,mouse_pozition):
                  draweble_table = menu_click(mouse_pozition,buttons,draweble_table)
                    # init_game()

        draw(screen, draweble_table, buttons, imgs)

    # print(pygame.mouse.get_pos())

    # running = False

    # Done! Time to quit.
    pygame.quit()
