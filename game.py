import pygame
import sys
import paddle, sphere

pygame.init()
screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()
font_title = pygame.font.Font('./font/arcade.ttf', 80)
font_key = pygame.font.Font('./font/Pixeltype.ttf', 55)
font_player = pygame.font.Font('./font/Pixeltype.ttf', 40)
font_instruction = pygame.font.Font('./font/arcade.ttf', 40)
font_winner = pygame.font.Font('./font/ka1.ttf', 50)
game_on = False
winner = -1

def collision():
    return pygame.sprite.spritecollide(ball.sprite, paddles, False)

def check_game(ball):
    if ball.sprite.rect.left < -5:
        return 1, False
    elif ball.sprite.rect.right >= 805:
        return 0, False
    return -1, True
   

bg_image = pygame.image.load('./Background/Background.png').convert_alpha()
bg_image_rect = bg_image.get_rect(center = (400, 200))

paddles = pygame.sprite.Group()
paddles.add(paddle.Paddle_Left())
paddles.add(paddle.Paddle_Right())

ball = pygame.sprite.GroupSingle()
ball.add(sphere.Ball())

home_bg = pygame.Surface((800, 400))
home_bg.fill('#1a1a1a')

title = font_title.render('Paddle Pong', False, '#cfcfcf')
title_rect = title.get_rect(center = (400, 80))

key_w = font_key.render('W', False, '#787878')
key_w_rect = key_w.get_rect(center = (120, 200))

key_s = font_key.render('S', False, '#787878')
key_s_rect = key_s.get_rect(center = (120, 260))

key_i = font_key.render('I', False, '#787878')
key_i_rect = key_i.get_rect(center = (680, 200))

key_k = font_key.render('K', False, '#787878')
key_k_rect = key_k.get_rect(center = (680, 260))

player_one_text = font_player.render('Player 1', False, '#787878')
player_one_text_rect = player_one_text.get_rect(center = (120, 330))

player_two_text = font_player.render('Player 2', False, '#787878')
player_two_text_rect = player_two_text.get_rect(center = (680, 330))

instruction = font_instruction.render('press SPACE to start', False, '#cfcfcf')
instruction_rect = instruction.get_rect(center = (400, 280))

winner_1 = font_winner.render('Player 1 wins!', False, '#cfcfcf')
winner_1_rect = winner_1.get_rect(center = (400, 180))

winner_2 = font_winner.render('Player 2 wins!', False, '#cfcfcf')
winner_2_rect = winner_2.get_rect(center = (400, 180))

while True:
    counter = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        
        if game_on == False and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_on = True
                ball.update(reset=True)
    
    if game_on == True:
        screen.blit(bg_image, bg_image_rect)

        paddles.draw(screen)
        paddles.update()

        ball.draw(screen)
        ball.update(paddle=collision())

        winner, game_on = check_game(ball)
    
    else:
        screen.blit(home_bg, (0, 0))
        screen.blit(title, title_rect)

        if (counter // 1000) % 2 == 0:
                screen.blit(instruction, instruction_rect)

        if winner == -1:
            if (counter // 1000) % 2 == 0:
                screen.blit(instruction, instruction_rect)
            
            screen.blit(key_w, key_w_rect)
            pygame.draw.rect(screen, '#787878', key_w_rect.inflate(28, 13), 3,  border_radius=5)

            screen.blit(key_s, key_s_rect)
            pygame.draw.rect(screen, '#787878', key_s_rect.inflate(28, 13), 3,  border_radius=5)

            screen.blit(key_i, key_i_rect)
            pygame.draw.rect(screen, '#787878', key_i_rect.inflate(35, 13), 3,  border_radius=5)

            screen.blit(key_k, key_k_rect)
            pygame.draw.rect(screen, '#787878', key_k_rect.inflate(28, 13), 3,  border_radius=5)

            screen.blit(player_one_text, player_one_text_rect)
            screen.blit(player_two_text, player_two_text_rect)
        
        if winner == 0:
            screen.blit(winner_1, winner_1_rect)
        
        elif winner == 1:
            screen.blit(winner_2, winner_2_rect)


    pygame.display.update()
    clock.tick(60)
