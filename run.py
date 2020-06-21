import pygame
import constants

from Button import Button
from Slider import Slider

def init_screen():
    pygame.init()
    pygame.display.set_caption("Sorting Visualizer")

    display = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.WINDOW_HEIGHT))

    display.fill(pygame.Color("White"))
    pygame.display.update()

    return display

DISPLAY = init_screen()

BUBBLE_SORT_BTN = Button((0, 0, 0), constants.WINDOW_WIDTH, 0, 140, 40, "BUBBLE SORT", 22, True)
QUICK_SORT_BTN = Button((0, 0, 0), constants.WINDOW_WIDTH + 150, 0, 140, 40, "QUICK SORT", 22)
INSERT_SORT_BTN = Button((0, 0, 0), constants.WINDOW_WIDTH + 300, 0, 140, 40, "INSERTION SORT", 22)

START_BTN = Button((0, 0, 0), constants.WINDOW_WIDTH + constants.MENU_WIDTH / 2 - 125, constants.WINDOW_HEIGHT / 2 - 150, 250, 100, "START")
GENERATE_BTN = Button((0, 0, 0), constants.WINDOW_WIDTH + constants.MENU_WIDTH / 2 - 125, constants.WINDOW_HEIGHT / 2, 250, 50, "GENERATE", 30)

COMPLEX_SLIDER = Slider("Complexity", 2, 512, 2, 1100)

def check_events():
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEMOTION:
            if BUBBLE_SORT_BTN.is_over(pos):
                BUBBLE_SORT_BTN.set_hover()
            elif not BUBBLE_SORT_BTN.is_pressed:
                BUBBLE_SORT_BTN.del_hover()

            if QUICK_SORT_BTN.is_over(pos):
                QUICK_SORT_BTN.set_hover()
            elif not QUICK_SORT_BTN.is_pressed:
                QUICK_SORT_BTN.del_hover()

            if INSERT_SORT_BTN.is_over(pos):
                INSERT_SORT_BTN.set_hover()
            elif not INSERT_SORT_BTN.is_pressed:
                INSERT_SORT_BTN.del_hover()

            if START_BTN.is_over(pos):
                START_BTN.set_hover()
            else:
                START_BTN.del_hover()

            if GENERATE_BTN.is_over(pos):
                GENERATE_BTN.set_hover()

            else:
                GENERATE_BTN.del_hover()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if BUBBLE_SORT_BTN.is_over(pos):
                INSERT_SORT_BTN.is_pressed = False
                QUICK_SORT_BTN.is_pressed = False
                BUBBLE_SORT_BTN.is_pressed = True
                return True

            if QUICK_SORT_BTN.is_over(pos):
                INSERT_SORT_BTN.is_pressed = False
                BUBBLE_SORT_BTN.is_pressed = False
                QUICK_SORT_BTN.is_pressed = True
                return True

            if INSERT_SORT_BTN.is_over(pos):
                QUICK_SORT_BTN.is_pressed = False
                BUBBLE_SORT_BTN.is_pressed = False
                INSERT_SORT_BTN.is_pressed = True
                return True

            if START_BTN.is_over(pos):
                START_BTN.is_pressed = True

            if GENERATE_BTN.is_over(pos):
                GENERATE_BTN.is_pressed = True

            #Slider
            if COMPLEX_SLIDER._button_rect.collidepoint(pos):
                COMPLEX_SLIDER.is_hit = True

        if event.type == pygame.MOUSEBUTTONUP:
            COMPLEX_SLIDER.is_hit = False

        if event.type == pygame.QUIT:
            pygame.quit()

    return False

def draw_menu():
    DISPLAY.fill(pygame.Color("White"), (constants.WINDOW_WIDTH, 0, constants.MENU_WIDTH, constants.WINDOW_HEIGHT))

    START_BTN.draw(DISPLAY)
    BUBBLE_SORT_BTN.draw(DISPLAY)
    QUICK_SORT_BTN.draw(DISPLAY)
    INSERT_SORT_BTN.draw(DISPLAY)

    GENERATE_BTN.draw(DISPLAY)
    COMPLEX_SLIDER.draw(DISPLAY)

    pygame.display.update(constants.WINDOW_WIDTH, 0, constants.MENU_WIDTH, constants.WINDOW_HEIGHT)


def draw_rects(algorithm, complexity, elem_a=None, elem_b=None):
    DISPLAY.fill(pygame.Color("White"), (0, 0, constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT))

    rand_array = algorithm.rand_array
    ratio = int(constants.WINDOW_WIDTH / complexity)

    space = int(constants.WINDOW_WIDTH / complexity)

    for i, value in enumerate(rand_array):
        pygame.draw.rect(DISPLAY, (0, 0, 0), (ratio * i, constants.WINDOW_HEIGHT, space, -value))
        #import pdb; pdb.set_trace()

    check_events()

    pygame.display.update(0, 0, constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT)

def set_sorting_algorithm(complexity):
    from Algorithm import BubbleSort, QuickSort, InsertionSort

    if BUBBLE_SORT_BTN.is_pressed:
        return BubbleSort(complexity)
    elif QUICK_SORT_BTN.is_pressed:
        return QuickSort(complexity)
    elif INSERT_SORT_BTN.is_pressed:
        return InsertionSort(complexity)

def main():
    complexity = 2
    #2^n
    running = True
    while(running):
        is_type_changed = check_events()

        if is_type_changed:
            sorting_algorithm = set_sorting_algorithm(complexity)
            draw_rects(sorting_algorithm, complexity)

        if START_BTN.is_pressed:
            try:
                sorting_algorithm.run()
                del sorting_algorithm
            except:
                pass
            finally:
                START_BTN.is_pressed = False
                sorting_algorithm = set_sorting_algorithm(complexity)

        if GENERATE_BTN.is_pressed:
            sorting_algorithm = set_sorting_algorithm(complexity)

            draw_rects(sorting_algorithm, complexity)
            GENERATE_BTN.is_pressed = False

        if COMPLEX_SLIDER.is_hit:
            COMPLEX_SLIDER.move()

            new_complexity = COMPLEX_SLIDER.power
            if new_complexity != complexity:
                complexity = new_complexity

                sorting_algorithm = set_sorting_algorithm(complexity)

                draw_rects(sorting_algorithm, complexity)

        draw_menu()


if __name__ == "__main__":
    main()