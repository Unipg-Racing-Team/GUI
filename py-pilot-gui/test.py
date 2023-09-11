import pygame
import sys
import random

# Inizializza pygame
pygame.init()

# Colori
NERO = (0, 0, 0)
GRIGIO = (100, 100, 100)
BIANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROSSO = (200, 0, 0)

# Dimensioni schermo
LARGHEZZA = 800
ALTEZZA = 600

# Crea la finestra
screen = pygame.display.set_mode((LARGHEZZA, ALTEZZA))
pygame.display.set_caption("Interfaccia Pilota")


# Funzione per mostrare il testo nella finestra
def mostra_testo(texto, posizione, dimensione=40, colore=BIANCO):
    font = pygame.font.SysFont(None, dimensione)
    img = font.render(texto, True, colore)
    rect = img.get_rect(center=posizione)
    screen.blit(img, rect)


# Funzione per disegnare una barra progressiva
def disegna_barra(posizione, valore, max_valore, soglia=30, larghezza=200, altezza=20):
    colore_barra = GRIGIO if valore >= soglia else ROSSO
    lunghezza_interna = int(larghezza * valore / max_valore)
    pygame.draw.rect(
        screen, colore_barra, (posizione[0], posizione[1], lunghezza_interna, altezza)
    )
    pygame.draw.rect(
        screen, BIANCO, (posizione[0], posizione[1], larghezza, altezza), 2
    )


# Funzione per disegnare un cerchio che rappresenta una percentuale
def disegna_cerchio(posizione, percentuale):
    colore = GRIGIO
    superficie_temp = pygame.Surface((160, 160), pygame.SRCALPHA)
    pygame.draw.arc(
        superficie_temp, colore, (0, 0, 160, 160), 0, percentuale / 100 * 3.14 * 2, 6
    )
    screen.blit(superficie_temp, (posizione[0] - 80, posizione[1] - 80))
    mostra_testo(f"{percentuale}%", posizione, 40, BIANCO)


# Funzione per disegnare una spia che può essere verde (attiva) o rossa (non attiva)
def disegna_spia(posizione, attivo):
    colore = VERDE if attivo else ROSSO
    pygame.draw.circle(screen, colore, posizione, 15)
    pygame.draw.circle(screen, BIANCO, posizione, 15, 1)


# Funzione per aggiornare i valori in modo dinamico
def aggiorna_valori():
    global valore_velocita, valore_accell, valore_freno, valori_barre

    # Incremento casuale della velocità
    velocita_attuale = int(valore_velocita.split(" ")[0])
    velocita_aggiornata = min(max(velocita_attuale + random.randint(-2, 2), 0), 250)
    valore_velocita = f"{velocita_aggiornata} km/h"

    # Incrementa o decrementa casualmente l'accelerazione e il freno
    valore_accell = min(max(valore_accell + random.randint(-5, 5), 0), 100)
    valore_freno = min(max(valore_freno + random.randint(-5, 5), 0), 100)

    # Aggiorna anche i valori delle barre in modo dinamico
    for i in range(len(valori_barre)):
        testo, valore, max_valore = valori_barre[i]
        nuovo_valore = min(max(valore + random.randint(-5, 5), 0), max_valore)
        valori_barre[i] = (testo, nuovo_valore, max_valore)


valore_velocita = "120 km/h"
valore_accell = 50
valore_freno = 75
spia_attiva = True
valori_barre = [
    ("Temp Inverter", 20, 100),
    ("Temp Batterie", 100, 100),
    ("Temp Motori", 100, 100),
]

# Ciclo principale del programma
running = True
while running:
    # Gestione degli eventi
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Colorazione dello sfondo
    screen.fill(NERO)

    # Aggiorna i valori per rendere l'interfaccia dinamica
    aggiorna_valori()

    # Disegna l'interfaccia
    mostra_testo(valore_velocita, (LARGHEZZA // 2, ALTEZZA // 8), 70, BIANCO)
    disegna_spia((LARGHEZZA // 2, ALTEZZA // 8 + 130), spia_attiva)
    disegna_cerchio((LARGHEZZA // 2 - 220, ALTEZZA // 2 + 20), valore_accell)
    disegna_cerchio((LARGHEZZA // 2 + 220, ALTEZZA // 2 + 20), valore_freno)

    spazio = 50
    larghezza_barra = 200
    pos_y = ALTEZZA - 80
    for i, (testo, valore, max_valore) in enumerate(valori_barre):
        x_pos = spazio + (larghezza_barra + spazio) * i
        mostra_testo(testo, (x_pos + larghezza_barra / 2, pos_y - 40), 40, BIANCO)
        disegna_barra((x_pos, pos_y), valore, max_valore, soglia=30)

    # Aggiornamento della visualizzazione
    pygame.display.flip()

    pygame.time.wait(100)  # Attendere 100ms prima di aggiornare di nuovo

# Uscita dal programma
pygame.quit()
sys.exit()
