import pygame

pygame.init()

width, height = 800,600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Pong Game")

def main():
    run = True

    while run:

        for event in pygame.event.get():
            if event.type == pygame.quit:
                run = False
                break

if __name__ == "__main__":
    main()