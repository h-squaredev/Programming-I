'''
UFMT - Ciencia da Computacao
Programacao de computadores
prof. Ivairton
Programacao 1
Data: 21/09/2025

Aluno 1: Humberto Henrique Castro Rocha - 202512722003
Aluno 2: Joao Victor Brito do Nascimento - 202511722014

Trabalho Final 2 - Desenvolvimento de um jogo em Python

'''

# Biblioteca PyGame
import pygame
# Biblioteca para geracao de numeros pseudoaleatorios
import random
# Modulo da biblioteca PyGame que permite o acesso as teclas utilizadas
from pygame.locals import * 

# Classe que representar o jogador
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((50, 75)) #Define o retangulo que representa o player
        self.surf = pygame.image.load("Trabalho2_Prog1/imagens/virus_player.png") #Carrega a imagem do player
        self.surf = pygame.transform.scale(self.surf, (120, 75)) #Redimensiona a imagem do player
        self.rect = self.surf.get_rect()

    '''
    # Determina acao de movimento conforme teclas pressionadas
    def update(self, pressed_keys):-
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -1)
        if pressed_keys[K_DOWN]: 
            self.rect.move_ip(0, 1)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-1, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(1, 0)
    '''

    #Determina acao de movimento conforme o movimento do mouse
    def update_mouse(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.rect.center = (mouse_x, mouse_y)

        # Mantem o jogador nos limites da tela do jogo
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 900:
            self.rect.right = 900
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= 600:
            self.rect.bottom = 600


# Classe que representa os inimigos
class Enemy(pygame.sprite.Sprite):
    def __init__(self, center_pos):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((20, 10)) #Definicao do retangulo
        self.surf = pygame.image.load("Trabalho2_Prog1/imagens/dragon_firewall.png") #Carrega a imagem do inimigo
        self.surf = pygame.transform.scale(self.surf, (140, 90)) #Redimensiona a imagem do inimigo
        self.rect = self.surf.get_rect( #Coloca na extrema direita (entre 900 e 1300) e sorteia sua posicao em relacao a coordenada y (entre 0 e 600)
            center=(random.randint(900, 1250), random.randint(0, 600))
        )
      # Usamos o 'center_pos' recebido para definir a posição
        self.rect = self.surf.get_rect(center = center_pos)
        self.lifespan = 800  # Tempo de vida do inimigo em frames

    def update(self):
        # Decrementa o tempo de vida a cada frame
        self.lifespan -= 1
        if self.lifespan <= 0:
            self.kill() # Remove o inimigo quando o tempo de vida acaba


# Classe que representa os projeteis inimigos
class Bullet(pygame.sprite.Sprite):
    def __init__(self, speed):
        super(Bullet, self).__init__()
        self.surf = pygame.Surface((20, 10)) #Definicao do retangulo
        self.surf = pygame.image.load("Trabalho2_Prog1/imagens/bullet.png") #Carrega a imagem do projetil
        self.surf = pygame.transform.scale(self.surf, (100, 30)) #Redimensiona a imagem do projetil
        self.rect = self.surf.get_rect( #Coloca na extrema direita (entre 820 e 1300) e sorteia sua posicao em relacao a coordenada y (entre 0 e 600)
            center=(random.randint(900, 1200), random.randint(0, 600))
        )
        self.speed = speed  # Define a velocidade do projetil 

    # Funcao que atualiza a posiçao do projetil em funcao da sua velocidade e termina com ele quando ele atinge o limite esquerdo da tela (x < 0)
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

# Classe que representa o placar do jogo
class Scoreboard:
    def __init__(self):
        self.score = 0
        self.font = pygame.font.SysFont("Arial", 30)

    def increase_score(self, points):
        self.score += points

    def render(self, surface):
        score_text = self.font.render(f"PONTUAÇÃO: {self.score}", True, (0, 0, 0))
        surface.blit(score_text, (10, 10))

# função para aumentar a dificuldade
def dificuldade(current_score):
    if current_score > 2000:
        return 11 #velocidade 11
    elif current_score > 1800:
        return 10 # velocidade 10
    elif current_score > 1600:
        return 9 # velocidade 9
    elif current_score > 1400:
        return 8 # velocidade 8
    elif current_score > 1200:
        return 7 # velocidade 7
    elif current_score > 1000:
        return 6 # velocidade 6
    elif current_score > 800:
        return 5 # velocidade 5
    elif current_score > 600:
        return 4 # velocidade 4
    elif current_score > 400:
        return 3 # velocidade 3
    elif current_score > 200:
        return 2 # velocidade 2
    else: 
        return 1 # velocidade inicial

# Inicializa pygame
pygame.init()

# Cria a tela com resolução 1200x600px
screen = pygame.display.set_mode((1200, 600))

# Cria um evento para adicao de projeteis e inimigos
ADDBULLET = pygame.USEREVENT + 1
pygame.time.set_timer(ADDBULLET, 500) #Define um intervalo para a criacao de cada projetil (milisegundos)

# Cria o placar
score = Scoreboard()
ADDSCORE = pygame.USEREVENT + 10
pygame.time.set_timer(ADDSCORE, 1000) #Define um intervalo para o incremento do placar (milisegundos)


# Cria o jogador (nosso retangulo)
player = Player()

# Define o plano de fundo do jogo
background_image = pygame.image.load("Trabalho2_Prog1/imagens/background.png").convert()
background_image = pygame.transform.scale(background_image, (1200, 600))

enemies = pygame.sprite.Group() #Cria o grupo de inimigos
bullets = pygame.sprite.Group() #Cria o grupo de projeteis
all_sprites = pygame.sprite.Group() #Cria o grupo de todos os Sprites
all_sprites.add(player) #Adicionar o player no grupo de todos os Sprites

running = True #Flag para controle do jogo
game_over_flag = False #Flag para controle do "gameover"

while running:

    # A velocidade do projétil é ajustada a cada frame com base na pontuação
    current_bullet_speed = dificuldade(score.score)

    #Laco para verificacao do evento que ocorreu
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE: #Verifica se a tecla ESC foi pressionada
                running = False
        elif event.type == QUIT: #Verifica se a janela foi fechada
            running = False
        elif(event.type == ADDBULLET): #Verifica se e o evento de criar um projetil
            new_bullet = Bullet(current_bullet_speed) #Cria um novo projetil
            bullets.add(new_bullet) #Adiciona o projetil no grupo de projeteis
            all_sprites.add(new_bullet) #Adiciona o projetil no grupo de todos os Sprites

            new_enemy = Enemy(new_bullet.rect.center) # Cria um novo inimigo na posicao do projetil
            enemies.add(new_enemy) #Adiciona o inimigo no grupo de inimigos
            all_sprites.add(new_enemy) #Adiciona o inimigo no grupo de todos os Sprites

        if event.type == ADDSCORE and not game_over_flag: 
            score.increase_score(10) #Incrementa o placar


    if not game_over_flag: #Enquanto nao for "game over", o jogo roda normalmente

        screen.blit(background_image, (0, 0)) #Atualiza a exibicao do plano de fundo do jogo (neste caso nao surte efeito)
        #pressed_keys = pygame.key.get_pressed() #Captura as as teclas pressionadas
        #player.update(pressed_keys) #Atualiza a posicao do player conforme teclas usadas
        player.update_mouse() #Atualiza a posicao do player conforme movimento do mouse
        enemies.update() #Atualiza posicao dos inimigos
        bullets.update() #Atualiza posicao dos projeteis
        score.render(screen) #Renderiza o placar na tela

        #Desenha todos os Sprites na tela
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect) #Atualiza a exibicao de todos os Sprites

        if pygame.sprite.spritecollideany(player, bullets): #Verifica se ocorreu a colisao do player com um dos inimigos
            player.kill() #Se ocorrer a colisao, encerra o player
            game_over_flag = True #Define a flag de "game over"

    else:
        screen.blit(background_image, (0, 0)) #Atualiza a exibicao do plano de fundo do jogo (neste caso nao surte efeito)

        # Exibe a mensagem de fim de jogo e a pontuacao final
        game_over = pygame.font.SysFont("Arial", 72).render("GAME OVER", True, (255, 0, 0)) #Cria a mensagem de fim de jogo
        game_over_rect = game_over.get_rect(center=(600, 300)) #Define a posicao da mensagem
        screen.blit(game_over, game_over_rect) #Exibe a mensagem na tela

        final_score = pygame.font.SysFont("Arial", 48).render(f"SUA PONTUAÇÃO: {score.score}", True, (0, 0, 0)) #Cria a mensagem com a pontuacao final
        final_score_rect = final_score.get_rect(center=(600, 400)) #Define a posicao da mensagem
        screen.blit(final_score, final_score_rect) #Exibe a mensagem
            
       
        

    pygame.display.flip() #Atualiza a projecao do jogo
