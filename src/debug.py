import pygame

pygame.init()
font = pygame.font.Font(None, 30)

def debug(info, y = 10, x = 10):
    curr_display = pygame.display.get_surface()
    message = font.render(str(info), True, 'White')
    rect = message.get_rect(topleft= (x,y) )
    pygame.draw.rect(curr_display, 'Black', rect)
    curr_display.blit(message, rect)