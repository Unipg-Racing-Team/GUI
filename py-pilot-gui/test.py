import pygame
import sys

# Inizializza pygame
pygame.init()

# Colori
BIANCO = (255, 255, 255)
NERO = (0, 0, 0)
VERDE = (0, 200, 0)
ROSSO = (200, 0, 0)
GRIGIO_SCURO = (40, 40, 40)
AZZURRO = (0, 174, 239)

# Dimensioni schermo
LARGHEZZA = 800
ALTEZZA = 600

# Crea la finestra
screen = pygame.display.set_mode((LARGHEZZA, ALTEZZA))
pygame.display.set_caption("Interfaccia Pilota")


def mostra_testo(texto, posizione, dimensione=30, colore=BIANCO):
    font = pygame.font.SysFont(None, dimensione)
    img = font.render(texto, True, colore)
    rect = img.get_rect(center=posizione)
    screen.blit(img, rect)


def disegna_barra(posizione, valore, max_valore, soglia=30, larghezza=200, altezza=15):
    colore_barra = VERDE if valore >= max_valore * soglia / 100 else ROSSO
    lunghezza_interna = int(larghezza * valore / max_valore)
    pygame.draw.rect(
        screen, colore_barra, (posizione[0], posizione[1], lunghezza_interna, altezza)
    )


def disegna_cerchio(posizione, percentuale, colore=VERDE):
    pygame.draw.circle(screen, colore, posizione, 70)
    # Uso una superficie temporanea per creare l'effetto del cerchio "pieno"
    superficie_temp = pygame.Surface((140, 140), pygame.SRCALPHA)
    pygame.draw.circle(superficie_temp, colore, (70, 70), 70)
    pygame.draw.circle(superficie_temp, GRIGIO_SCURO, (70, 70), 65)
    pygame.draw.arc(
        superficie_temp,
        GRIGIO_SCURO,
        (0, 0, 140, 140),
        0,
        (1 - percentuale / 100) * 3.14 * 2,
        65,
    )
    screen.blit(superficie_temp, (posizione[0] - 70, posizione[1] - 70))


valore_velocita = "120 km/h"
valore_accell = 100
valore_freno = 50
valori_barre = [
    ("Temp Inverter", 100, 100),
    ("Temp Batterie", 100, 100),
    ("Temp Motori", 100, 100),
]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(GRIGIO_SCURO)
    pygame.draw.rect(
        screen, BIANCO, (LARGHEZZA // 2 - 125, ALTEZZA // 5 - 55, 250, 110), 8
    )
    mostra_testo(valore_velocita, (LARGHEZZA // 2, ALTEZZA // 5), 60)

    # Richiamo funzioni
    disegna_cerchio((LARGHEZZA // 2 - 200, ALTEZZA // 2 + 30), valore_accell, VERDE)
    disegna_cerchio((LARGHEZZA // 2 + 200, ALTEZZA // 2 + 30), valore_freno, ROSSO)
    mostra_testo("Frenata", (LARGHEZZA // 2 - 200, ALTEZZA // 2 + 30), 25)
    mostra_testo("Accellerazione", (LARGHEZZA // 2 + 200, ALTEZZA // 2 + 30), 25)

    spazio = 50
    larghezza_barra = 200
    pos_y = ALTEZZA - 80
    for i, (testo, valore, max_valore) in enumerate(valori_barre):
        x_pos = spazio + (larghezza_barra + spazio) * i
        mostra_testo(testo, (x_pos + larghezza_barra / 2, pos_y - 30))
        disegna_barra((x_pos, pos_y), valore, max_valore)

    pygame.display.flip()

pygame.quit()
sys.exit()
