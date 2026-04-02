import pygame
import random
import sys
import os

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


pygame.init()
pygame.mixer.init()
pygame.init()

info = pygame.display.Info()
WIDTH = info.current_w
HEIGHT = info.current_h

BLOCK = 30   # ❗ fixed size (simple & stable)

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

pause = False

# ----------------
# LOADING SCREEN
# ----------------

def loading_screen():

    start_time = pygame.time.get_ticks()

    font = pygame.font.SysFont(None, 70)

    while True:

        # background
        screen.blit(loading_img, (0, 0))

        # 🔤 TEXT CREATE
        text = "LOADING..."
        shadow = font.render(text, True, (120, 100, 0))
        main = font.render(text, True, (255, 255, 150))

        # 📍 CENTER POSITION
        text_rect = main.get_rect(center=(WIDTH // 5, HEIGHT // 2))

        # shadow + main
        screen.blit(shadow, (text_rect.x + 3, text_rect.y + 3))
        screen.blit(main, text_rect)

        pygame.display.update()

        # ⏱️ 2 seconds wait
        if pygame.time.get_ticks() - start_time > 2000:
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


# ----------------
# START MENU
# ----------------

def start_menu():

    play_btn = pygame.Rect(200,300,200,60)
    exit_btn2 = pygame.Rect(200,380,200,60)

    while True:

        screen.blit(grass,(0,0))

        draw_3d_text("SNAKE GAME",70,120,150)

        pygame.draw.rect(screen,(120,70,20),play_btn,border_radius=10)
        pygame.draw.rect(screen,(120,70,20),exit_btn2,border_radius=10)

        draw_3d_text("PLAY",40,260,315)
        draw_3d_text("EXIT",40,260,395)

        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                mx,my = pygame.mouse.get_pos()

                if play_btn.collidepoint(mx,my):
                    return

                if exit_btn2.collidepoint(mx,my):
                    pygame.quit()
                    sys.exit()

# ----------------
# LOAD IMAGES
# ----------------

grass = pygame.image.load(os.path.join(BASE_DIR, "images/grass.png"))
frog_img = pygame.image.load(os.path.join(BASE_DIR, "images/frog.png"))
loading_img = pygame.image.load(os.path.join(BASE_DIR, "images/loading.jpg"))
gameover_img = pygame.image.load(os.path.join(BASE_DIR, "images/gameover.png"))

grass = pygame.transform.scale(grass, (WIDTH, HEIGHT))
frog_img = pygame.transform.scale(frog_img, (BLOCK, BLOCK))
loading_img = pygame.transform.scale(loading_img, (WIDTH, HEIGHT))
gameover_img = pygame.transform.scale(gameover_img, (WIDTH, HEIGHT))

# ----------------
# SOUND
# ----------------

eat_sound = pygame.mixer.Sound(os.path.join(BASE_DIR, "music/eat.mp3"))
gameover_sound = pygame.mixer.Sound(os.path.join(BASE_DIR, "music/gameover.mp3"))

pygame.mixer.music.load(os.path.join(BASE_DIR, "music/background.mp3"))
pygame.mixer.music.play(-1)
# ----------------
# HIGH SCORE
# ----------------

if not os.path.exists("highscore.txt"):
    open("highscore.txt","w").write("0")

def load_highscore():
    return int(open("highscore.txt").read())

def save_highscore(score):
    if score > load_highscore():
        open("highscore.txt","w").write(str(score))

# ----------------
# TEXT
# ----------------

def draw_3d_text(text,size,x,y):

    font = pygame.font.SysFont(None,size)

    shadow = font.render(text,True,(120,100,0))
    main = font.render(text,True,(255,255,150))

    screen.blit(shadow,(x+3,y+3))
    screen.blit(main,(x,y))

# ----------------
# LOADING SCREEN
# ----------------

def loading_screen():

    progress = 0

    while progress <= 100:

        # background image
        screen.blit(loading_img, (0, 0))

        # text


        # 🔲 loading bar background (bottom)
        pygame.draw.rect(screen, (50, 50, 50), (100, 520, 400, 25), border_radius=10)

        # 🟨 loading bar fill (yellow)
        pygame.draw.rect(screen, (255, 255, 0), (100, 520, 4 * progress, 25), border_radius=10)

        # % text
        font = pygame.font.SysFont(None, 35)
        percent_text = font.render(f"{progress}%", True, (255, 255, 255))
        screen.blit(percent_text, (270, 550))

        pygame.display.update()

        pygame.time.delay(20)  # speed control

        progress += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

# ----------------
# START MENU
# ----------------

def start_menu():

    play_btn = pygame.Rect(200,300,200,60)
    exit_btn2 = pygame.Rect(200,380,200,60)

    while True:

        screen.blit(grass,(0,0))

        draw_3d_text("SNAKE GAME",70,120,150)

        pygame.draw.rect(screen,(120,70,20),play_btn,border_radius=10)
        pygame.draw.rect(screen,(120,70,20),exit_btn2,border_radius=10)

        draw_3d_text("PLAY",40,260,315)
        draw_3d_text("EXIT",40,260,395)

        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                mx,my = pygame.mouse.get_pos()

                if play_btn.collidepoint(mx,my):
                    return

                if exit_btn2.collidepoint(mx,my):
                    pygame.quit()
                    sys.exit()

# ----------------
# TOUCH CONTROLS
# ----------------


left_btn = pygame.Rect(90,820,70,50)
right_btn = pygame.Rect(200,820,70,50)
up_btn = pygame.Rect(150,745,70,50)
down_btn = pygame.Rect(150,890,70,50)

pause_btn = pygame.Rect(1200,820,70,50)

exit_btn = pygame.Rect(560,10,30,30)

# ----------------
# SNAKE
# ----------------

snake = [(300,300),(270,300),(240,300)]
direction = "RIGHT"

score = 0
speed = 6

frog = (random.randrange(0,WIDTH,BLOCK),
        random.randrange(0,HEIGHT,BLOCK))

frog_scale = 1
grow = True

# ----------------
# GAME OVER
# ----------------

def game_over():

    global score,snake,direction,speed

    save_highscore(score)

    restart_btn = pygame.Rect(200,350,200,60)
    exit_btn2 = pygame.Rect(200,430,200,60)

    gameover_sound.play()

    while True:

        screen.blit(gameover_img,(0,0))

        draw_3d_text("GAME OVER",70,150,150)
        draw_3d_text("SCORE : "+str(score),50,180,230)

        pygame.draw.rect(screen,(120,70,20),restart_btn,border_radius=10)
        pygame.draw.rect(screen,(120,70,20),exit_btn2,border_radius=10)

        draw_3d_text("RESTART",40,230,365)
        draw_3d_text("EXIT",40,260,445)

        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                mx,my = pygame.mouse.get_pos()

                if restart_btn.collidepoint(mx,my):

                    snake[:] = [(300,300),(270,300),(240,300)]
                    direction = "RIGHT"
                    score = 0
                    speed = 6
                    return

                if exit_btn2.collidepoint(mx,my):
                    pygame.quit()
                    sys.exit()
# ----------------
# MAIN GAME
# ----------------

def move_snake():

    global snake

    x,y = snake[0]

    if direction == "RIGHT":
        x += BLOCK
    if direction == "LEFT":
        x -= BLOCK
    if direction == "UP":
        y -= BLOCK
    if direction == "DOWN":
        y += BLOCK

    if x >= WIDTH: x = 0
    if x < 0: x = WIDTH-BLOCK
    if y >= HEIGHT: y = 0
    if y < 0: y = HEIGHT-BLOCK

    new_head = (x,y)

    if new_head in snake:
        game_over()

    snake.insert(0,new_head)

def eat():

    global frog,score,speed

    head_rect = pygame.Rect(snake[0][0], snake[0][1], BLOCK, BLOCK)
    frog_rect = pygame.Rect(frog[0], frog[1], BLOCK, BLOCK)

    if head_rect.colliderect(frog_rect):

        eat_sound.play()
        score += 1

        frog = (random.randrange(0,WIDTH,BLOCK),
                random.randrange(0,HEIGHT,BLOCK))

        if score % 10 == 0:
            speed += 1

    else:
        snake.pop()

def draw_snake():

    for i,pos in enumerate(snake):

        x,y = pos

        pygame.draw.rect(screen,(0,120,0),(x,y,BLOCK,BLOCK),border_radius=8)
        pygame.draw.rect(screen,(255,255,0),(x,y,BLOCK,BLOCK),3,border_radius=8)

        if i == 0:

            pygame.draw.circle(screen,(255,255,255),(x+8,y+10),4)
            pygame.draw.circle(screen,(255,255,255),(x+22,y+10),4)

            pygame.draw.line(screen,(255,0,0),(x+15,y+15),(x+30,y+15),2)

def draw_frog():

    size = int(BLOCK * frog_scale)
    frog_anim = pygame.transform.scale(frog_img,(size,size))
    screen.blit(frog_anim,frog)

def draw_score():


    font = pygame.font.SysFont(None,40)

    text = font.render("Score : "+str(score),True,(255,255,255))
    screen.blit(text,(10,10))

    high = font.render("High : "+str(load_highscore()),True,(255,255,0))
    screen.blit(high,(380,10))

    # EXIT BUTTON
    exit_btn = pygame.Rect(960, 10, 30, 30)

# ----------------
# MAIN LOOP
# ----------------
def main():
    global direction, pause

    running = True

    while running:

        # 🎯 EVENTS
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:

                mx, my = pygame.mouse.get_pos()

                # 🎮 CONTROL BUTTONS
                if left_btn.collidepoint(mx, my):
                    direction = "LEFT"

                elif right_btn.collidepoint(mx, my):
                    direction = "RIGHT"

                elif up_btn.collidepoint(mx, my):
                    direction = "UP"

                elif down_btn.collidepoint(mx, my):
                    direction = "DOWN"

                elif pause_btn.collidepoint(mx, my):
                    pause = not pause

                elif exit_btn.collidepoint(mx, my):
                    pygame.quit()
                    sys.exit()

        # 🚀 GAME LOGIC
        if not pause:
            move_snake()
            eat()

        # 🎨 DRAW EVERYTHING (VERY IMPORTANT ORDER)

        screen.blit(grass, (0, 0))

        draw_frog()
        draw_snake()
        draw_score()

        # ⏸️ PAUSE TEXT
        if pause:
            draw_3d_text("PAUSED", 60, 200, 250)

        # ❌ EXIT BUTTON
        pygame.draw.rect(screen, (200, 0, 0), exit_btn)
        pygame.draw.line(screen, (255,255,255), (562,12), (588,38), 6)
        pygame.draw.line(screen, (255,255,255), (588,12), (562,38), 6)

        # 🎮 CONTROL BUTTONS
    # DRAW CONTROL BUTTONS

        # 🌫️ Create transparent surface for buttons
        btn_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)

        # 🎮 Draw buttons (WHITE + ALPHA)
        pygame.draw.rect(btn_surface, (255, 255, 255, 80), left_btn)
        pygame.draw.rect(btn_surface, (255, 255, 255, 80), right_btn)
        pygame.draw.rect(btn_surface, (255, 255, 255, 80), up_btn)
        pygame.draw.rect(btn_surface, (255, 255, 255, 80), down_btn)
        pygame.draw.rect(btn_surface, (255, 255, 255, 80), pause_btn)

        # ✨ ADD BORDERS (new)
        pygame.draw.rect(btn_surface, (255, 255, 255, 180), left_btn, 3)
        pygame.draw.rect(btn_surface, (255, 255, 255, 160), right_btn, 3)
        pygame.draw.rect(btn_surface, (255, 255, 255, 160), up_btn, 3)
        pygame.draw.rect(btn_surface, (255, 255, 255, 160), down_btn, 3)
        pygame.draw.rect(btn_surface, (255, 255, 255, 160), pause_btn, 3)

        # 👉 Blit to main screen
        screen.blit(btn_surface, (0, 0))

        # 🔤 TEXT (same as yours)
        font = pygame.font.SysFont(None, 40)

        screen.blit(font.render("<", True, (255, 255, 255)), (100, 830))
        screen.blit(font.render(">", True, (255, 255, 255)), (240, 830))
        screen.blit(font.render("^", True, (255, 255, 255)), (175, 750))
        screen.blit(font.render("v", True, (255, 255, 255)), (175, 910))
        screen.blit(font.render("II", True, (255, 255, 255)), (1230, 830))
        pygame.display.update()

        clock.tick(speed)



if __name__ == "__main__":
    loading_screen()
    start_menu()
    main()
