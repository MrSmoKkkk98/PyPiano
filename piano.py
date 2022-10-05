"""
1. set up surface
2. create buttons
3. add sounds
"""

import pygame

pygame.init()
res = (1080, 720)
screen = pygame.display.set_mode(res)
# stores the width of the
# screen into a variable
width = screen.get_width()

# stores the height of the
# screen into a variable
height = screen.get_height()

white_color = (255, 255, 255)
black_color = (0, 0, 0)
color_light = (170, 170, 170)
color_dark = (100, 100, 100)

whitekey_height = 20.76923076923077*10
whitekey_width = 13.84615384615385
smallfont = pygame.font.SysFont('Corbekl', 15)
text = smallfont.render('A0', True, white_color)


def game_loop():
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 0 <= mouse[0] <= 0+whitekey_width and height-whitekey_height <= mouse[1] <= height:
                    running = False

        screen.fill((220, 215, 200))
        mouse = pygame.mouse.get_pos()
        if 0 <= mouse[0] <= 0+whitekey_width and height-whitekey_height <= mouse[1] <= height:
            pygame.draw.rect(screen, color_light, [
                             0, height-whitekey_height, whitekey_width, whitekey_height])

        else:
            pygame.draw.rect(screen, color_dark, [
                             0, height-whitekey_height, whitekey_width, whitekey_height])

        screen.blit(text, (0, height-whitekey_height/2))
        pygame.display.update()
    pygame.quit()
    exit()


game_loop()
