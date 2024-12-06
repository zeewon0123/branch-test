import pygame
import sys

pygame.init()
pygame.display.set_caption('Jumping dino')
MAX_WIDTH = 800
MAX_HEIGHT = 400


def main():
    # set screen, fps
    screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))
    fps = pygame.time.Clock()

    # dino
    imgdog1 = pygame.image.load('dogwalk1.png')
    imgdog2 = pygame.image.load('dogwalk2.png')
    dog_height = imgdog1.get_size()[1]
    dog_bottom = MAX_HEIGHT - dog_height
    dog_x = 50
    dog_y = dog_bottom
    jump_top = 400
    leg_swap = True
    is_bottom = True
    is_go_up = False

    # tree
    imgTree = pygame.image.load('tree.png')
    tree_height = imgTree.get_size()[1]
    tree_x = MAX_WIDTH
    tree_y = MAX_HEIGHT - tree_height

    while True:
        screen.fill((255, 255, 255))

        # event check
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if is_bottom:
                    is_go_up = True
                    is_bottom = False

        # dino move
        if is_go_up:
            dog_y -= 10.0
        elif not is_go_up and not is_bottom:
            dog_y += 10.0

        # dino top and bottom check
        if is_go_up and dog_y <= jump_top:
            is_go_up = False

        if not is_bottom and dog_y >= dog_bottom:
            is_bottom = True
            dog_y = dog_bottom

        # tree move
        tree_x -= 12.0
        if tree_x <= 0:
            tree_x = MAX_WIDTH

        # draw tree
        screen.blit(imgTree, (tree_x, tree_y))

        # draw dino
        if leg_swap:
            screen.blit(imgdog1, (dog_x, dog_y))
            leg_swap = False
        else:
            screen.blit(imgdog2, (dog_x, dog_y))
            leg_swap = True

        # update
        pygame.display.update()
        fps.tick(60)


if __name__ == '__main__':
    main()
