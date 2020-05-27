import pygame
import constants

display = pygame.display.set_mode()

def init_screen():
    global display

    pygame.init()
    display = pygame.display.set_mode((constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT))
    display.fill(pygame.Color("White"))

    return display

def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

def draw_rects(type_algorithm, elem_a, elem_b):
    display.fill(pygame.Color("White"))

    rand_array = type_algorithm.get_rand_array()

    space = int(constants.WINDOW_WIDTH / constants.ARRAY_SIZE)

    for i, value in enumerate(rand_array):
        pygame.draw.rect(display, (0,0,0), (constants.RATIO * i, constants.WINDOW_HEIGHT, space, -value))
        #import pdb; pdb.set_trace()

    check_events()
    pygame.display.update()


def main():
    from SortingAlgorithm import BubbleSort

    display = init_screen()
    pygame.display.set_caption("Sorting Visualizer")

    sorting_algorithm = BubbleSort()
    sorting_algorithm.run()


if __name__ == "__main__":
    main()
