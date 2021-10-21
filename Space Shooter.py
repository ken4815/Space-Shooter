import pygame
import os
pygame.font.init()
# import Pygame_Library
pygame.display.set_caption("Space Shooter")
# Color
Black = (0, 0, 0)
Green = (0, 255, 0)
Red = (255, 0, 0)
Pink = (255, 100, 180)
Winner_Color = (50, 75, 250)  # Blue
Width, Height = 1000, 500
Windows = pygame.display.set_mode((Width, Height))

SpaceShip_1_Hit = pygame.USEREVENT + 1
SpaceShip_1_Hit2 = pygame.USEREVENT + 2
SpaceShip_2_Hit = pygame.USEREVENT + 3
SpaceShip_2_Hit2 = pygame.USEREVENT + 4
FPS = 60
Bullet_Vel = 7
Max_Bullet = 10
Border = pygame.Rect(Width//2, 0, 5, Height)

# Font import
FONT = pygame.font.SysFont('impact', 30)
FONT2 = pygame.font.SysFont('corbel', 20)
FONT3 = pygame.font.SysFont('impact', 45)

# Picture import
Player_1 = pygame.image.load(os.path.join('material', 'PikPng.com_pixel-spaceship-png_3880069.png'))
Player_2 = pygame.image.load(os.path.join('material', 'pngaaa.com-3006421.png'))
BackGround = pygame.transform.scale\
    (pygame.image.load(os.path.join('material', 'stardew-valley-moon-landscape-pixel-art-hd-wallpaper-preview.jpg')),
     (Width, Height))


Player_Resize_1 = pygame.transform.rotate(pygame.transform.scale (Player_1, (100, 40)), 270)
Player_Resize_2 = pygame.transform.rotate(pygame.transform .scale (Player_2, (55, 80)), 90)
# Drawing part
def drawing(Spaceship1, Spaceship2, s1_bullet, s2_bullet, Player_1_Score, Player_2_Score, s1_bullet2, s2_bullet2, ):
    Windows.blit(BackGround, (0, 0))

    pygame.draw.rect(Windows, Pink , Border)
    Player_1_Score_Text = FONT.render("Score:" + str(Player_1_Score), True, Green)
    Player_2_Score_Text = FONT.render("Score:" + str(Player_2_Score), True, Red)
    Name = FONT2.render("Ken_Pakkapong" , True, (255, 255, 255))



    Windows.blit(Player_1_Score_Text,
                 (Width - Player_1_Score_Text.get_width() - 10, 10))
    Windows.blit(Player_2_Score_Text,
                 (Width - Player_2_Score_Text.get_width() - 900, 10))
    Windows.blit(Name, (10, 475))


    Windows.blit(Player_Resize_1, (Spaceship1.x, Spaceship1.y))
    Windows.blit(Player_Resize_2, (Spaceship2.x, Spaceship2.y))

    for bullet in s1_bullet:
        pygame.draw.rect(Windows, Green, bullet)

    for bullet in s2_bullet:
        pygame.draw.rect(Windows, Red, bullet)

    for bullet in s1_bullet2:
        pygame.draw.rect(Windows, Red, bullet)

    for bullet in s2_bullet2:
        pygame.draw.rect(Windows, Black, bullet)

    pygame.display.update()
# Moving part
def Player_1_prssed(key, Spaceship_1):
    key = pygame.key.get_pressed()
    # A(left) key press
    if key[pygame.K_a] and Spaceship_1.x - 4 > 0:
        Spaceship_1.x -= 4  # Velocity of SpaceShip
    # D(Right) key press
    if key[pygame.K_d] and Spaceship_1.x + 4 < Border.x:
        Spaceship_1.x += 4
    # W(Up) key press
    if key[pygame.K_w] and Spaceship_1.y - 4 > 0:
        Spaceship_1.y -= 4
    # S(Down) key press
    if key[pygame.K_s] and Spaceship_1.y + 4 + Spaceship_1.height < Height:
        Spaceship_1.y += 4


def Player_2_prssed(key, Spaceship_2):
    key = pygame.key.get_pressed()
    # (left) key press
    if key[pygame.K_LEFT] and Spaceship_2.x - 4 > Border.x + Border.width:
        Spaceship_2.x -= 4  # Velocity of SpaceShip
    # (Right) key press
    if key[pygame.K_RIGHT] and Spaceship_2.x + 4 + Spaceship_2.height < Width:
        Spaceship_2.x += 4
    # (Up) key press
    if key[pygame.K_UP] and Spaceship_2.y - 4 > 0:
        Spaceship_2.y -= 4
    # (Down) key press
    if key[pygame.K_DOWN] and Spaceship_2.y + 4 + Spaceship_2.height < Height:
        Spaceship_2.y += 4


def damage_bullet(s1_bullet, s2_bullet, Spaceship_1, Spaceship_2, s1_bullet2, s2_bullet2):  # BulletHit Part
    for bullet in s1_bullet:
        bullet.x += Bullet_Vel
        if Spaceship_2.colliderect(bullet):
            pygame.event.post(pygame.event.Event(SpaceShip_2_Hit))
            s1_bullet.remove(bullet)
        elif bullet.x > Width:
            s1_bullet.remove(bullet)

    for bullet in s2_bullet:
        bullet.x -= Bullet_Vel
        if Spaceship_1.colliderect(bullet):
            pygame.event.post(pygame.event.Event(SpaceShip_1_Hit))
            s2_bullet.remove(bullet)
        elif bullet.x > Width:
            s2_bullet.remove(bullet)

    for bullet in s1_bullet2:
        bullet.x += 15
        if Spaceship_2.colliderect(bullet):
            pygame.event.post(pygame.event.Event(SpaceShip_1_Hit2))
            s1_bullet2.remove(bullet)
        elif bullet.x > Width:
            s1_bullet2.remove(bullet)

    for bullet in s2_bullet2:
        bullet.x -= 4
        if Spaceship_1.colliderect(bullet):
            pygame.event.post(pygame.event.Event(SpaceShip_2_Hit2))
            s2_bullet2.remove(bullet)
        elif bullet.x > Width:
            s2_bullet2.remove(bullet)

def winner_text(text):
    drawing_text = FONT3.render(text, True, Winner_Color)
    Windows.blit(drawing_text,
                 (Width/2 - drawing_text.get_width()/2, Height/2 - drawing_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(1000)

# MainGame Code
def mainSystems():
    Spaceship_1 = pygame.Rect(100, 200, 100, 40)
    Spaceship_2 = pygame.Rect(850, 200, 100, 40)

    s1_bullet = []
    s2_bullet = []
    s1_bullet2 = []
    s2_bullet2 = []
    Player_1_Score = 0
    Player_2_Score = 0
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()  # QuitGame loop

            if event.type == pygame.KEYDOWN:  # Bullet adjust
                if event.key == pygame.K_SPACE and len(s1_bullet) < Max_Bullet:
                    bullet = pygame.Rect(Spaceship_1.x, Spaceship_1.y + Spaceship_1.height/2 - 2, 10, 2)
                    s1_bullet.append(bullet)

                if event.key == pygame.K_KP0 and len(s2_bullet) < Max_Bullet:
                    bullet = pygame.Rect(Spaceship_2.x, Spaceship_2.y + Spaceship_2.height/6 , 15, 5)
                    s2_bullet.append(bullet)

                if event.key == pygame.K_t and len(s1_bullet2) < 10:  # Special Bullet
                    bullet = pygame.Rect(Spaceship_1.x, Spaceship_1.y + Spaceship_1.height + 10 , 10, 1)
                    s1_bullet2.append(bullet)

                if event.key == pygame.K_KP1 and len(s2_bullet2) < 4:  # Special Bullet
                    bullet = pygame.Rect(Spaceship_2.x, Spaceship_2.y + Spaceship_2.height/2 - 2, 25, 20)
                    s2_bullet2.append(bullet)
            # Bullet damage part
            if event.type == SpaceShip_2_Hit:
                Player_2_Score += 1

            if event.type == SpaceShip_1_Hit:
                Player_1_Score += 2

            if event.type == SpaceShip_1_Hit2:
                Player_2_Score += 1.5

            if event.type == SpaceShip_2_Hit2:
                Player_1_Score += 5
        # Score part
        winner = ""
        if Player_1_Score >= 20:
            winner = "Player1 Wins"

        if Player_2_Score >= 20:
            winner = "Player2 Wins"

        if winner != "":
            winner_text(winner)

            break

        key = pygame.key.get_pressed()
        Player_1_prssed(key, Spaceship_1)
        Player_2_prssed(key, Spaceship_2)
        damage_bullet(s1_bullet, s2_bullet, Spaceship_1, Spaceship_2, s1_bullet2, s2_bullet2)
        drawing(Spaceship_1, Spaceship_2, s1_bullet, s2_bullet, Player_1_Score, Player_2_Score, s1_bullet2, s2_bullet2)

    mainSystems()


if __name__ == "__main__":
    mainSystems()