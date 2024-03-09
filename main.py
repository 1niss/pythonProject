
# Import de la librairie pygame
import pygame
import random

# Pour avoir les constantes de Pygame
from pygame import *


# Taille de notre Ã©cran
LARGEUR_ECRAN = 800
HAUTEUR_ECRAN = 600


class Vaisseau(pygame.sprite.Sprite):

    # Constructeur
    def __init__(self):
        super(Vaisseau, self).__init__()
        self.surf = pygame.image.load("templates/image.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()


    def update(self, pressed_keys):

        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)

        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)

        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)

        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        if pressed_keys[K_SPACE]:
            if len(le_missile.sprites()) < 1:
                missile = Missile(self.rect.center)
                le_missile.add(missile)
                tous_sprites.add(missile)


        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > LARGEUR_ECRAN:
            self.rect.right = LARGEUR_ECRAN
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= HAUTEUR_ECRAN:
            self.rect.bottom = HAUTEUR_ECRAN



class Missile(pygame.sprite.Sprite):

    def __init__(self, center_missile):
        global player
        super(Missile, self).__init__()
        self.surf = pygame.image.load("templates/missile.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=center_missile
        )
        son_missile.play()
    def update(self):

        self.rect.move_ip(15, 0)

        if self.rect.left > LARGEUR_ECRAN:
            self.kill()



class Enemmi(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemmi, self).__init__()
        self.surf = pygame.image.load("templates/ennemi.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)

        self.rect = self.surf.get_rect(
            center=(
                LARGEUR_ECRAN + 50,
                random.randint(0, HAUTEUR_ECRAN),
            )
        )
        # Chaque ennemi Ã  une vitesse au hazard, entre 5 et 20
        self.speed = random.randint(5, 20)

    # Mise Ã  jour du vaisseau ennemi
    def update(self):
        # DÃ©placement du vaisseau vers la gauche
        self.rect.move_ip(-self.speed, 0)
        # Si le vaisseau sort de l'Ã©cran, on l'efface
        if self.rect.right < 0:
            self.kill()



class Explosion(pygame.sprite.Sprite):

    def __init__(self, center_vaisseau):
        super(Explosion, self).__init__()
        # On affiche l'explosion pendant 10 cycles
        self._compteur = 10
        self.surf = pygame.image.load("templates/explosion.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=center_vaisseau
        )
        son_explosion.play()
    # Mise Ã  jour de l'explosion
    def update(self):

        self._compteur = self._compteur - 1
        # Une fois Ã  0, on efface l'explosion
        if self._compteur == 0:
            self.kill()

            class Etoile(pygame.sprite.Sprite):
                def __init__(self):
                    super(Etoile, self).__init__()
                    self.surf = pygame.image.load("ressources/etoile.png").convert()
                    self.surf.set_colorkey((255, 255, 255), RLEACCEL)
                    # Position de dÃ©part alÃ©atoire, Ã  droite de l'Ã©cran
                    self.rect = self.surf.get_rect(
                        center=(
                            LARGEUR_ECRAN + 20,
                            random.randint(0, HAUTEUR_ECRAN),
                        )
                    )
class Etoile(pygame.sprite.Sprite):
    def __init__(self):
        super(Etoile, self).__init__()
        self.surf = pygame.image.load("templates/etoile.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        # Position de dÃ©part alÃ©atoire, Ã  droite de l'Ã©cran
        self.rect = self.surf.get_rect(
            center=(
                LARGEUR_ECRAN + 20,
                random.randint(0, HAUTEUR_ECRAN),
            )
        )

    def update(self):

        self.rect.move_ip(-5, 0)

        if self.rect.right < 0:
            self.kill()
class Score(pygame.sprite.Sprite):
    def __init__(self):
        super(Score, self).__init__()
        self._scoreCourant = 0
        self._setText()

    def _setText(self):
        self.surf = police_score.render(
            'Score : ' + str(self._scoreCourant), False, (255, 255, 255))
        self.rect = self.surf.get_rect(
            center=(LARGEUR_ECRAN / 2, 15)
        )

    def update(self):
        self._setText()

    # Pour incrÃ©menter le score quand on touche un ennemi
    def incremente(self, valeur):
        self._scoreCourant = self._scoreCourant + valeur



pygame.font.init()

police_score = pygame.font.SysFont('Comic Sans MS', 30)

pygame.mixer.init()

son_missile = pygame.mixer.Sound("templates/laser.ogg")
son_explosion = pygame.mixer.Sound("templates/explosion.ogg")
# RÃ©glage de l'horloge
clock = pygame.time.Clock()

# Initialisation de la librairie
pygame.init()
pygame.display.set_caption("The Shoot'em up 1.0 !")



AJOUTE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(AJOUTE_ENEMY, 500)
AJOUTE_ETOILE = pygame.USEREVENT + 2
pygame.time.set_timer(AJOUTE_ETOILE, 100)




ecran = pygame.display.set_mode([LARGEUR_ECRAN, HAUTEUR_ECRAN])



tous_sprites = pygame.sprite.Group()
# Le missile
le_missile = pygame.sprite.Group()
# Les ennemis
les_ennemies = pygame.sprite.Group()
# Les explosions
les_explosions = pygame.sprite.Group()
# les etoiles
les_etoiles = pygame.sprite.Group()
vaisseau= Vaisseau()
tous_sprites.add(vaisseau)
#score
score = Score()
tous_sprites.add(score)
# Game loop
continuer = True
while continuer:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False

        elif event.type == AJOUTE_ENEMY:

            nouvel_enemmi = Enemmi()
            # Ajout aux groupes
            les_ennemies.add(nouvel_enemmi)
            tous_sprites.add(nouvel_enemmi)
        elif event.type == AJOUTE_ETOILE:

            nouvel_etoile = Etoile()
            les_etoiles.add(nouvel_etoile)
            tous_sprites.add(nouvel_etoile)


    ecran.fill((0, 0, 0))


    if pygame.sprite.spritecollideany(vaisseau, les_ennemies):
        vaisseau.kill()
        explosion = Explosion(vaisseau.rect.center)
        les_explosions.add(explosion)
        tous_sprites.add(explosion)
        continuer = False


    for missile in le_missile:
        liste_ennemis_touches = pygame.sprite.spritecollide(
            missile, les_ennemies, True)
        if len(liste_ennemis_touches) > 0:
            missile.kill()
            score.incremente(len(liste_ennemis_touches))
        for ennemi in liste_ennemis_touches:
            explosion = Explosion(ennemi.rect.center)
            les_explosions.add(explosion)
            tous_sprites.add(explosion)

    # Pile des touches appuyÃ©es
    touche_appuyee = pygame.key.get_pressed()

    # Mise Ã  jour des Ã©lÃ©ments
    vaisseau.update(touche_appuyee)
    le_missile.update()
    les_ennemies.update()
    les_explosions.update()
    les_etoiles.update()
    score.update()


    for mon_sprite in tous_sprites:
        ecran.blit(mon_sprite.surf, mon_sprite.rect)

    # On passe notre surface pour l'afficher
    pygame.display.flip()


    clock.tick(30)
pygame.time.delay(3000)

pygame.quit()