import pygame

class Personagem:
    def __init__(self, x=0, y=0, tam=40, cor=(0, 255, 0)):
        self.x = x
        self.y = y
        self.tam = tam
        self. cor = cor
    def rect(self):
        return pygame.Rect(self.x, self.y, self.tam, self.tam)

def inicio():
    global tela
    tela = pygame.display.set_mode((800, 600))
def principal():
    x = y = 0
    p = Personagem()
    inimigo = Personagem(x = 760, y=300, cor=(255,0,0))
    coisas = [p, inimigo]
    tiro = None
    while True:
        tela.fill((0, 0, 0))
        for c in coisas:
            pygame.draw.rect(tela, c.cor, (c.x, c.y, c.tam, c.tam))
        inimigo.x -= 10
        if inimigo.x < 0:
            inimigo.x = 790

        pygame.display.flip()
        pygame.event.pump()
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_RIGHT]:
            p.x += 10
        if teclas[pygame.K_LEFT]:
            p.x -= 10
        if teclas[pygame.K_UP]:
            p.y -= 10
        if teclas[pygame.K_DOWN]:
            p.y +=  10
        if teclas[pygame.K_SPACE] and not tiro:
            tiro = Personagem(p.x, p.y, 10, (255, 255,255))
            coisas.append(tiro)

        if tiro:
            tiro.x += 10
            if tiro.x > 800:
                tiro = None
                coisas.pop()
        if inimigo.rect().colliderect(p.rect()):
            print("Voce morreu!!!")
            break

        if tiro and inimigo.rect().colliderect(tiro.rect()):
            print("Voce ganhou!!!")
            break


        if teclas[pygame.K_ESCAPE]:
            break
        pygame.time.delay(30)
inicio()
principal()
pygame.quit()
