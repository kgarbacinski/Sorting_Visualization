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

display = init_screen()

button_bubble_sort = Button((0,0,0), constants.WINDOW_WIDTH, 0, 140, 40, "BUBBLE SORT", 25, True)
button_bubble_sort.set_hover()

button_quick_sort = Button((0, 0, 0), constants.WINDOW_WIDTH + 150, 0, 140, 40, "QUICK SORT", 25)

button_start = Button((0,0,0), constants.WINDOW_WIDTH + constants.MENU_WIDTH / 2 - 125, constants.WINDOW_HEIGHT / 2 - 150, 250, 100, "START")
button_generate = Button((0,0,0), constants.WINDOW_WIDTH + constants.MENU_WIDTH / 2 - 125, constants.WINDOW_HEIGHT / 2, 250, 50, "GENERATE", 30)

complex_slider = Slider("Complexity", 2, 512, 2, 1100)

def check_events():
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEMOTION:
            if button_bubble_sort.is_over(pos):
                button_bubble_sort.set_hover()
            elif not button_bubble_sort.is_pressed:
                button_bubble_sort.del_hover()

            if button_quick_sort.is_over(pos):
                button_quick_sort.set_hover()
            elif not button_quick_sort.is_pressed:
                button_quick_sort.del_hover()


            if button_start.is_over(pos):
                button_start.set_hover()
            else:
                button_start.del_hover()

            if button_generate.is_over(pos):
                button_generate.set_hover()

            else:
                button_generate.del_hover()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_bubble_sort.is_over(pos):
                button_quick_sort.is_pressed = False
                button_bubble_sort.is_pressed = True
                return True

            if button_quick_sort.is_over(pos):
                button_bubble_sort.is_pressed = False
                button_quick_sort.is_pressed = True
                return True

            if button_start.is_over(pos):
                button_start.is_pressed = True

            if button_generate.is_over(pos):
                button_generate.is_pressed = True

            #Slider
            if complex_slider._button_rect.collidepoint(pos):
                complex_slider.is_hit = True

        if event.type == pygame.MOUSEBUTTONUP:
            complex_slider.is_hit = False

        if event.type == pygame.QUIT:
            pygame.quit()

    return False

def draw_menu():
    display.fill(pygame.Color("White"),(constants.WINDOW_WIDTH, 0, constants.MENU_WIDTH, constants.WINDOW_HEIGHT))

    button_start.draw(display)
    button_bubble_sort.draw(display)
    button_quick_sort.draw(display)

    button_generate.draw(display)
    complex_slider.draw(display)

    pygame.display.update(constants.WINDOW_WIDTH, 0, constants.MENU_WIDTH, constants.WINDOW_HEIGHT)


def draw_rects(algorithm, complexity, elem_a=None, elem_b=None):
    display.fill(pygame.Color("White"), (0, 0, constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT))

    rand_array = algorithm.rand_array
    ratio = int(constants.WINDOW_WIDTH / complexity)

    space = int(constants.WINDOW_WIDTH / complexity)

    for i, value in enumerate(rand_array):
        pygame.draw.rect(display, (0,0,0), (ratio * i, constants.WINDOW_HEIGHT, space, -value))
        #import pdb; pdb.set_trace()

    check_events()

    pygame.display.update(0, 0, constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT)

def set_sorting_algorithm(complexity):
    from SortingAlgorithm import BubbleSort, QuickSort

    if button_bubble_sort.is_pressed:
        return BubbleSort(complexity)
    elif button_quick_sort.is_pressed:
        return QuickSort(complexity)

def main():
    complexity = 2
    #2^n
    running = True
    while(running):
        is_type_changed = check_events()

        if is_type_changed:
            sorting_algorithm = set_sorting_algorithm(complexity)
            draw_rects(sorting_algorithm, complexity)

        if button_start.is_pressed:
            try:
                sorting_algorithm.run()
                del sorting_algorithm
            except:
                pass
            finally:
                button_start.is_pressed = False

        if button_generate.is_pressed:
            sorting_algorithm = set_sorting_algorithm(complexity)

            draw_rects(sorting_algorithm, complexity)
            button_generate.is_pressed = False

        if complex_slider.is_hit:
            complex_slider.move()

            new_complexity = complex_slider.power
            if new_complexity != complexity:
                complexity = new_complexity

                sorting_algorithm = set_sorting_algorithm(complexity)

                draw_rects(sorting_algorithm, complexity)

        draw_menu()


if __name__ == "__main__":
    main()