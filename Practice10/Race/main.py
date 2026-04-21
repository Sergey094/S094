import pygame
import sys
import random
import os

pygame.init()

# ------------------ PATHS ------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def load_image(filename, color=None, w=None, h=None):
    try:
        path = os.path.join(BASE_DIR, filename)
        img = pygame.image.load(path)

        if w and h:
            img = pygame.transform.scale(img, (w, h))

        return img

    except:
        surf = pygame.Surface((w or 50, h or 50))
        surf.fill(color or (255, 0, 0))
        return surf

# ------------------ SCREEN ------------------
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Race Game")

clock = pygame.time.Clock()

# ------------------ COLORS ------------------
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

# ------------------ ASSETS ------------------
bg = load_image("AnimatedStreet.png", (100, 100, 100), WIDTH, HEIGHT)
player_img = load_image("Player.png", (0, 0, 255), 50, 80)
enemy_img = load_image("Enemy.png", (255, 0, 0), 50, 80)
coin_img = load_image("coin.png", (255, 255, 0), 30, 30)

font = pygame.font.SysFont(None, 30)
big_font = pygame.font.SysFont(None, 60)

# ------------------ GAME STATE ------------------
PLAYING = 0
GAME_OVER = 1
state = PLAYING

# ------------------ OBJECTS ------------------
player = pygame.Rect(175, 500, 50, 80)
enemy = pygame.Rect(random.randint(0, 350), -100, 50, 80)
coin = pygame.Rect(random.randint(0, 350), -300, 30, 30)

speed = 5
score = 0
coins = 0

# ------------------ RESET ------------------
def reset_game():
    global speed, score, coins, state

    player.x, player.y = 175, 500
    enemy.x, enemy.y = random.randint(0, 350), -100
    coin.x, coin.y = random.randint(0, 350), -300

    speed = 5
    score = 0
    coins = 0
    state = PLAYING

# ------------------ MAIN LOOP ------------------
running = True
while running:
    clock.tick(60)

    # ================= GAME =================
    if state == PLAYING:

        screen.blit(bg, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # движение игрока
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.x -= 6
        if keys[pygame.K_RIGHT]:
            player.x += 6

        # враг
        enemy.y += speed
        if enemy.y > HEIGHT:
            enemy.y = -100
            enemy.x = random.randint(0, 350)
            score += 1

        # монета
        coin.y += speed // 2
        if coin.y > HEIGHT:
            coin.y = -300
            coin.x = random.randint(0, 350)

        # столкновения
        if player.colliderect(enemy):
            state = GAME_OVER

        if player.colliderect(coin):
            coins += 1
            coin.y = -300
            coin.x = random.randint(0, 350)

        # скорость
        speed = min(10, 5 + score * 0.1)

        # draw
        screen.blit(player_img, player)
        screen.blit(enemy_img, enemy)
        screen.blit(coin_img, coin)

        text = font.render(f"Score: {score} Coins: {coins}", True, WHITE)
        screen.blit(text, (10, 10))

        pygame.display.update()

    # ================= GAME OVER =================
    else:

        screen.fill((200, 50, 50))

        title = big_font.render("GAME OVER", True, WHITE)
        restart = font.render("Press R to Restart", True, YELLOW)
        quit_text = font.render("Press ESC to Quit", True, WHITE)

        screen.blit(title, (60, 150))
        screen.blit(restart, (70, 250))
        screen.blit(quit_text, (70, 300))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    reset_game()

                if event.key == pygame.K_ESCAPE:
                    running = False

pygame.quit()
sys.exit()