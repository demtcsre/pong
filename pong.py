import pygame

pygame.init()

width, height = 800,600
fps = 120
bg_color = (0,0,139)
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Pong Game")

pad_w, pad_h = 20, 200

class Paddle():
    color = (102,102,255)
    vel = 25

    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.static = True

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x,self.y,self.width,self.height))

    def moveUp(self):
        if not self.static and self.y > 0:
            self.y -= self.vel
            
    def moveDown(self):
        if not self.static and self.y < height - self.height:
            self.y += self.vel

class Ball():
    def __init__(self):
        pass

def draw(screen, paddles):
    screen.fill(bg_color)
    for paddle in paddles:
        paddle.draw(screen)
    pygame.display.update()

def main():
    run = True
    clock = pygame.time.Clock()

    l_padd = Paddle(10, height//2 - pad_h//2, pad_w, pad_h)
    r_padd = Paddle(width - 10 - pad_w, height//2 - pad_h//2, pad_w, pad_h)
    padds = [l_padd, r_padd]

    while run:

        pygame.display.flip()
        clock.tick(fps)

        draw(screen, padds)

        for event in pygame.event.get():
            if event.type == pygame.quit:
                run = False
                break

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                if event.key == pygame.K_w:
                    l_padd.static = False
                    l_padd.moveUp()
                if event.key == pygame.K_s:
                    l_padd.static = False
                    l_padd.moveDown()
                if event.key == pygame.K_UP:
                    r_padd.static = False
                    r_padd.moveUp()
                if event.key == pygame.K_DOWN:
                    r_padd.static = False
                    r_padd.moveDown()
                    
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    l_padd.static = True
                if event.key == pygame.K_s:
                    l_padd.static = True
                if event.key == pygame.K_UP:
                    r_padd.static = True
                if event.key == pygame.K_DOWN:
                    r_padd.static = True


if __name__ == "__main__":
    main()