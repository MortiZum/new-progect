
pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Лабиринт")
background = transform.scale(image.load('kosmos.jpg'), (800, 600))
while True:

    for e in pygame.event.get():

        if e.type == pygame.QUIT:

            raise SystemExit("QUIT")


    pygame.display.update()
