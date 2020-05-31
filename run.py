import pygame
import constants

from Button import Button

def init_screen():
    pygame.init()
    pygame.display.set_caption("Sorting Visualizer")

    display = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.WINDOW_HEIGHT))

    display.fill(pygame.Color("White"))
    pygame.display.update()

    return display

display = init_screen()
button_start = Button((0,0,0), constants.WINDOW_WIDTH + constants.MENU_WIDTH / 2 - 125, constants.WINDOW_HEIGHT / 2 - 150, 250, 100, "START")
button_generate = Button((0,0,0), constants.WINDOW_WIDTH + constants.MENU_WIDTH / 2 - 125, constants.WINDOW_HEIGHT / 2, 250, 50, "GENERATE", 30)

def check_events():
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEMOTION:
            if button_start.is_over(pos):
                button_start.set_hover()
            else:
                button_start.del_hover()

            if button_generate.is_over(pos):
                button_generate.set_hover()

            else:
                button_generate.del_hover()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_start.is_over(pos):
                button_start.is_pressed = True

            if button_generate.is_over(pos):
                button_generate.is_pressed = True


        if event.type == pygame.QUIT:
            pygame.quit()

    return True

def draw_menu():
    display.fill(pygame.Color("White"),(constants.WINDOW_WIDTH, 0, constants.MENU_WIDTH, constants.WINDOW_HEIGHT))
    button_start.draw(display)
    button_generate.draw(display)
    pygame.display.update(constants.WINDOW_WIDTH, 0, constants.MENU_WIDTH, constants.WINDOW_HEIGHT)


def draw_rects(algorithm, elem_a=None, elem_b=None):
    display.fill(pygame.Color("White"), (0, 0, constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT))

    rand_array = algorithm.rand_array

    space = int(constants.WINDOW_WIDTH / constants.ARRAY_SIZE)

    for i, value in enumerate(rand_array):
        pygame.draw.rect(display, (0,0,0), (constants.RATIO * i, constants.WINDOW_HEIGHT, space, -value))
        #import pdb; pdb.set_trace()

    check_events()

    pygame.display.update(0, 0, constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT)

def main():
    from SortingAlgorithm import BubbleSort

    running = True
    while(running):
        check_events()
        if button_start.is_pressed:
            try:
                sorting_algorithm.run()
                del sorting_algorithm
            except:
                pass
            finally:
                button_start.is_pressed = False

        if button_generate.is_pressed:
            sorting_algorithm = BubbleSort()
            draw_rects(sorting_algorithm)
            button_generate.is_pressed = False

        draw_menu()

if __name__ == "__main__":
    main()
