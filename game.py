import sys, pygame
import random


pygame.init()

# window manipulation
width = 1280
height = 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Guess the bday')

#clock (to track fps)
clock = pygame.time.Clock()

running = True

# color of the screen
screencolor = 16, 37, 66

gift = pygame.image.load('assets/gift.png')
gift_rect = gift.get_rect()
gift_rect.x, gift_rect.y = 100, (720-gift_rect.width-20)


#letters
A = pygame.image.load('assets/letters/A.png')
A_rect = A.get_rect()
B = pygame.image.load('assets/letters/B.png')
B_rect = B.get_rect()
C = pygame.image.load('assets/letters/C.png')
C_rect = C.get_rect()
D = pygame.image.load('assets/letters/D.png')
D_rect = D.get_rect()
E = pygame.image.load('assets/letters/E.png')
E_rect = E.get_rect()
F = pygame.image.load('assets/letters/F.png')
F_rect = F.get_rect()
G = pygame.image.load('assets/letters/G.png')
G_rect = G.get_rect()
H = pygame.image.load('assets/letters/H.png')
H_rect = H.get_rect()
I = pygame.image.load('assets/letters/I.png')
I_rect = I.get_rect()
J = pygame.image.load('assets/letters/J.png')
J_rect = J.get_rect()
K = pygame.image.load('assets/letters/K.png')
K_rect = K.get_rect()
L = pygame.image.load('assets/letters/L.png')
L_rect = L.get_rect()
M = pygame.image.load('assets/letters/M.png')
M_rect = M.get_rect()
N = pygame.image.load('assets/letters/N.png')
N_rect = N.get_rect()
O = pygame.image.load('assets/letters/O.png')
O_rect = O.get_rect()
P = pygame.image.load('assets/letters/P.png')
P_rect = P.get_rect()
Q = pygame.image.load('assets/letters/Q.png')
Q_rect = Q.get_rect()
R = pygame.image.load('assets/letters/R.png')
R_rect = R.get_rect()
S = pygame.image.load('assets/letters/S.png')
S_rect = S.get_rect()
T = pygame.image.load('assets/letters/T.png')
T_rect = T.get_rect()
U = pygame.image.load('assets/letters/U.png')
U_rect = U.get_rect()
V = pygame.image.load('assets/letters/V.png')
V_rect = V.get_rect()
W = pygame.image.load('assets/letters/W.png')
W_rect = W.get_rect()
X = pygame.image.load('assets/letters/X.png')
X_rect = X.get_rect()
Y = pygame.image.load('assets/letters/Y.png')
Y_rect = Y.get_rect()
Z = pygame.image.load('assets/letters/Z.png')
Z_rect = Z.get_rect()


#speed
x_vel = 0
y_vel = 0
topspeed = 100

#lists
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 
           'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

falling_letter = letters[random.randint(0, 25)]
state = 'game'


while running:
   
     for event in pygame.event.get():
          #to quit the game when use clicks close button
          if event.type == pygame.QUIT:
               running = False
     if state == 'game':

          screen.fill(screencolor)
          screen.blit(gift, gift_rect)

          keys = pygame.key.get_pressed()
          if keys[pygame.K_RIGHT] and x_vel <= topspeed:
               x_vel += 0.2 
          if keys[pygame.K_LEFT] and x_vel >= -topspeed:
               x_vel -= 0.2
          if keys[pygame.K_LEFT] == False and keys[pygame.K_RIGHT] == False: 
               x_vel *= 0.95

          if gift_rect.x<=0 or gift_rect.x>=(1280-gift_rect.width):
               x_vel = x_vel * -0.5

          
          gift_rect.x += x_vel
     
          screen.blit(gift, gift_rect)

          screen.blit(vars()[falling_letter], vars()[falling_letter + '_rect'])
          if vars()[falling_letter + '_rect'].y <= 600:
               vars()[falling_letter + '_rect'].y += y_vel
          y_vel += 19
     # update the game's frame
     pygame.display.flip()


     # limit framerate to 60fps
     clock.tick(60)

pygame.quit()