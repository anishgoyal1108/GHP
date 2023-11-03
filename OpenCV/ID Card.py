import pygame

pygame.init()

width, height = 1280, 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("ID Card")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

font = pygame.font.SysFont("Arial", 18)

name = input("What's your name? ")
age = input("How old are you? ")
school = input("What school do you go to? ")
major = input("What's your major? ")
elective = input("What's your elective? ")
color = input("What's your personality color? ")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill(WHITE)

    pygame.draw.rect(window, GRAY, (20, 20, width - 40, height - 40))
    pygame.draw.rect(window, BLACK, (20, 20, width - 40, 30))

    text_surface = font.render("Governor's Honors Program ID Card", True, WHITE)
    window.blit(text_surface, (width // 2 - text_surface.get_width() // 2, 25))

    text_surface = font.render("Name: {}".format(name), True, BLACK)
    window.blit(text_surface, (40, 70))

    text_surface = font.render("Age: {}".format(age), True, BLACK)
    window.blit(text_surface, (40, 100))

    text_surface = font.render("School: {}".format(school), True, BLACK)
    window.blit(text_surface, (40, 130))

    text_surface = font.render("Major: {}".format(major), True, BLACK)
    window.blit(text_surface, (40, 160))

    text_surface = font.render("Elective: {}".format(elective), True, BLACK)
    window.blit(text_surface, (40, 190))

    text_surface = font.render("Personality Color: {}".format(color), True, BLACK)
    window.blit(text_surface, (40, 220))

    pygame.display.flip()

pygame.quit()