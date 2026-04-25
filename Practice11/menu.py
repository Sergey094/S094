import pygame
import subprocess
import sys
import os

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Main Menu")

font = pygame.font.SysFont(None, 40)

# Кнопки (пути остаются как есть)
buttons = [
    ("Paint", "Paint/main.py"),
    ("Race", "Race/main.py"),
    ("Snake", "Snake/main.py"),
    ("Exit", None)
]

def draw_buttons():
    screen.fill((50, 50, 50))

    for i, (text, _) in enumerate(buttons):
        label = font.render(text, True, (255, 255, 255))
        rect = label.get_rect(center=(WIDTH//2, 100 + i*70))
        screen.blit(label, rect)

    pygame.display.flip()

def run_script(path):
    if path:
        # абсолютный путь к файлу
        full_path = os.path.abspath(path)

        # папка, где лежит файл (ВАЖНО!)
        working_dir = os.path.dirname(full_path)

        subprocess.Popen(
            [sys.executable, full_path],
            cwd=working_dir   # 👈 фикс: правильная директория
        )

running = True
while running:
    draw_buttons()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()

            for i, (_, path) in enumerate(buttons):
                rect = pygame.Rect(200, 80 + i*70, 200, 50)

                if rect.collidepoint(mx, my):
                    if path is None:
                        running = False
                    else:
                        run_script(path)

pygame.quit()