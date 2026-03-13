import pygame
import random

WIDTH, HEIGHT = 900, 900
# BORDER_LENGTH, BORDER_GIRTH = 280, 280
CHAR_WIDTH, CHAR_HEIGHT = 28, 28
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

BULLET_VEL = 5
ENEMY_VEL = 1

ADD_ENEMY = pygame.USEREVENT + 1
HIT_ENEMY = pygame.USEREVENT + 2

BORDER_N1 = pygame.Rect(WIDTH//2 - 35, 0, 5, HEIGHT//2 - 35)
BORDER_N2 = pygame.Rect(WIDTH//2 + 35, 0, 5, HEIGHT//2 - 35)

BORDER_S1 = pygame.Rect(WIDTH//2 - 35, HEIGHT//2 + 35, 5, HEIGHT//2 - 35)
BORDER_S2 = pygame.Rect(WIDTH//2 + 35, HEIGHT//2 + 35, 5, HEIGHT//2 - 35)

BORDER_W1 = pygame.Rect(0, HEIGHT//2 - 35, HEIGHT//2 - 30, 5)
BORDER_W2 = pygame.Rect(0, HEIGHT//2 + 35, HEIGHT//2 - 30, 5)

BORDER_E1 = pygame.Rect(WIDTH//2 + 35, HEIGHT//2 - 35, HEIGHT//2 - 30, 5)
BORDER_E2 = pygame.Rect(WIDTH//2 + 35, HEIGHT//2 + 35, HEIGHT//2 - 30, 5)

def draw_window(defender, bullets_U, bullets_D, bullets_L, bullets_R, enemies_dict):
    WIN.fill(BLACK)
    pygame.draw.rect(WIN, WHITE, BORDER_N1)
    pygame.draw.rect(WIN, WHITE, BORDER_N2)
    pygame.draw.rect(WIN, WHITE, BORDER_S1)
    pygame.draw.rect(WIN, WHITE, BORDER_S2)
    pygame.draw.rect(WIN, WHITE, BORDER_W1)
    pygame.draw.rect(WIN, WHITE, BORDER_W2)
    pygame.draw.rect(WIN, WHITE, BORDER_E1)
    pygame.draw.rect(WIN, WHITE, BORDER_E2)


    for bullet in bullets_U:
        pygame.draw.rect(WIN, WHITE, bullet)
    for bullet in bullets_D:
        pygame.draw.rect(WIN, WHITE, bullet)
    for bullet in bullets_L:
        pygame.draw.rect(WIN, WHITE, bullet)
    for bullet in bullets_R:
        pygame.draw.rect(WIN, WHITE, bullet)

    for enemies in enemies_dict.values(): 
        for enemy in enemies:
            if enemy[1] == 1:
                color = RED
            if enemy[1] == 2:
                color = GREEN
            if enemy[1] == 3:
                color = BLUE
            if enemy[1] == 4:
                color = YELLOW
            pygame.draw.rect(WIN, color, enemy[0])

    pygame.draw.rect(WIN, WHITE, defender) # Always want defender to be on top, personal pref, might change later

    pygame.display.update()

def handle_bullets(bullets_U, bullets_D, bullets_L, bullets_R, enemies_dict):
    
   
    
    for bullet in (bullets_U):
        if bullet.y <= 0:
            bullets_U.remove(bullet)
        bullet.y -= BULLET_VEL

    for bullet in (bullets_D):
        if bullet.y >= HEIGHT:
            bullets_D.remove(bullet)
        bullet.y += BULLET_VEL

    for bullet in (bullets_L):
        if bullet.x <= 0:
            bullets_L.remove(bullet)
        bullet.x -= BULLET_VEL
        
    for bullet in (bullets_R):
        if bullet.x >= WIDTH:
            bullets_R.remove(bullet)
        bullet.x += BULLET_VEL

def handle_enemies(defender, enemies_dict, bullets_U, bullets_D, bullets_L, bullets_R):

    # Gets current minimum
    max_num = 0 # Will need to change this
    for lists in enemies_dict.values():
        for enemy in lists:
            if enemy[1] > max_num:
                max_num = enemy[1]

    for name, enemies in enemies_dict.items():
        for enemy in enemies:
            if name == "enemy_U":
                if enemy[0].y + ENEMY_VEL < defender.y:
                    enemy[0].y += ENEMY_VEL

                    for bullet in bullets_U:
                        if enemy[1] == max_num and enemy[0].colliderect(bullet):
                            enemies_dict["enemy_U"].remove(enemy)

            if name == "enemy_D":
                if enemy[0].y - ENEMY_VEL > defender.y:
                    enemy[0].y -= ENEMY_VEL

                    for bullet in bullets_D:
                        if enemy[1] == max_num and enemy[0].colliderect(bullet):
                            enemies_dict["enemy_D"].remove(enemy)
            if name == "enemy_L":
                if enemy[0].x + ENEMY_VEL < defender.x:
                    enemy[0].x += ENEMY_VEL

                    for bullet in bullets_L:
                        if enemy[1] == max_num and enemy[0].colliderect(bullet):
                            enemies_dict["enemy_L"].remove(enemy)
            if name == "enemy_R":
                if enemy[0].x - ENEMY_VEL > defender.x:
                    enemy[0].x -= ENEMY_VEL
                    
                    for bullet in bullets_R:
                        if enemy[1] == max_num and enemy[0].colliderect(bullet):
                            enemies_dict["enemy_R"].remove(enemy)

# def generate_enemies(enemies_dict):
#     choice = random.choice(list(enemies_dict.keys()))
#     new_enemy_cords = cords[choice]
#     new_enemy = pygame.Rect(new_enemy_cords[0], new_enemy_cords[1], new_enemy_cords[2], new_enemy_cords[3])

#     enemies_dict[choice].append(new_enemy)

def main():
    defender = pygame.Rect(WIDTH//2 - 12, HEIGHT//2 - 12, CHAR_WIDTH, CHAR_HEIGHT)

    bullets_U = []
    bullets_D = []
    bullets_L = []
    bullets_R = []

    enemies_dict = {
        "enemy_U": [[pygame.Rect(WIDTH//2 - 5, 10, 15, 15), 1]], 
        "enemy_D": [[pygame.Rect(WIDTH//2 - 5, HEIGHT - 25, 15, 15), 3]], 
        "enemy_L": [[pygame.Rect(10, HEIGHT//2 - 5, 15, 15), 2]], 
        "enemy_R": [[pygame.Rect(WIDTH - 25, HEIGHT//2 - 5, 15, 15), 4]]
        }
    cords = {
        "enemy_U": [WIDTH//2 - 5, 10, 15, 15], 
        "enemy_D": [WIDTH//2 - 5, HEIGHT - 25, 15, 15], 
        "enemy_L": [10, HEIGHT//2 - 5, 15, 15], 
        "enemy_R": [WIDTH - 25, HEIGHT//2 - 5, 15, 15]
        }
    
    numbers = [1, 2, 3, 4]

        
    # enemies = [pygame.Rect(WIDTH//2 - 5, 10, 15, 15)] # TOP # Probably turn into a dict and assign {"enemy_U": pygame.Rect...}

    # enemies_U = [] # TOP
    # enemies_D = [] # BOTTOM
    # enemies_L = [] # LEFT
    # enemies_R = [] # RIGHT


    clock = pygame.time.Clock()
    run = True
    pygame.time.set_timer(ADD_ENEMY, 2500)
    last_pos = ""
    
    while run:
        clock.tick(FPS)

        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

                if event.key == pygame.K_UP and len(bullets_U) == 0:
                    bullet = pygame.Rect(WIDTH//2, HEIGHT//2, 5, 10)
                    bullets_U.append(bullet)

                if event.key == pygame.K_DOWN and len(bullets_D) == 0:
                    bullet = pygame.Rect(WIDTH//2, HEIGHT//2, 5, 10)
                    bullets_D.append(bullet)

                if event.key == pygame.K_LEFT and len(bullets_L) == 0:
                    bullet = pygame.Rect(WIDTH//2, HEIGHT//2, 10, 5)
                    bullets_L.append(bullet)

                if event.key == pygame.K_RIGHT and len(bullets_R) == 0:
                    bullet = pygame.Rect(WIDTH//2, HEIGHT//2, 10, 5)
                    bullets_R.append(bullet)


            if event.type == ADD_ENEMY:
                for i in range (2):
                    choice = random.choice([item for item in enemies_dict.keys() if item != last_pos])
                    number = random.choice(numbers)
                    new_enemy_cords = cords[choice]
                    new_enemy = pygame.Rect(new_enemy_cords[0], new_enemy_cords[1], new_enemy_cords[2], new_enemy_cords[3])
                    last_pos = choice

                    enemies_dict[choice].append([new_enemy, number])

        #     if event.type == pygame.MOUSEBUTTONDOWN:
        #         if pygame.mouse.get_pressed()[0]: # MOUSE1

        #             bullet = pygame.Rect(defender.x - CHAR_WIDTH//2, defender.y - CHAR_HEIGHT//2, 10, 5)
        #             bullets.append(bullet)

        # print(bullets)

        # SPAWN_ENEMY()
        handle_bullets(bullets_U, bullets_D, bullets_L, bullets_R, enemies_dict)
        handle_enemies(defender, enemies_dict, bullets_U, bullets_D, bullets_L, bullets_R)
        draw_window(defender, bullets_U, bullets_D, bullets_L, bullets_R, enemies_dict)

    main()

if __name__ == "__main__":
    main()