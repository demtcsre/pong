import pygame

pygame.init()

width, height = 800,600
fps = 60
bg_color = (0,0,139)

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Pong Game")
screen.fill(bg_color)

pad_w, pad_h = 20, 200
ball_rad = 10

class Paddle():
    color = (102,102,255)
    vel = 5

    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x,self.y,self.width,self.height))

    def move(self, up = True):
        if up:
            self.y -= self.vel
        else:
            self.y += self.vel

class Ball():
    vel = 5
    color = (255,255,255)

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.x_vel = self.vel
        self.y_vel = 0

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x,self.y), self.radius)

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

def draw(screen, paddles, ball):
    screen.fill(bg_color)
    
    for paddle in paddles:
        paddle.draw(screen)

    for i in range(0, height, height//20):
        pygame.draw.rect(screen, (0,0,0), ((width//2 - 5), i, 10, height//20))

    ball.draw(screen)
    pygame.display.update()

def paddle_move_keys(keys, l_p, r_p):
    if keys[pygame.K_w] and l_p.y >= l_p.vel:
        l_p.move(up=True)
    if keys[pygame.K_s] and l_p.y + l_p.vel <= height - l_p.height:
        l_p.move(up=False)
    if keys[pygame.K_UP] and r_p.y >= r_p.vel:
        r_p.move(up=True)
    if keys[pygame.K_DOWN] and r_p.y + r_p.vel <= height - r_p.height:
        r_p.move(up=False)

def main():
    run = True
    clock = pygame.time.Clock()

    l_p = Paddle(10, height//2 - pad_h//2, pad_w, pad_h)
    r_p = Paddle(width - 10 - pad_w, height//2 - pad_h//2, pad_w, pad_h)
    padds = [l_p, r_p]
    ball= Ball(width//2, height//2, ball_rad)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.quit:
                run = False
                break

        clock.tick(fps)
        draw(screen, padds, ball)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
        paddle_move_keys(keys, l_p, r_p)

        pygame.display.update()

if __name__ == "__main__":
    main()