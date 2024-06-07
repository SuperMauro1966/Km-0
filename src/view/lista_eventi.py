from menu.menu import BaseMenu
from controller.user_role import UserRole

def eventi():
    role = BaseMenu.ruolo_utente

    if role == UserRole.ADMIN:
        print("Sei un admin")
        print("Nessun evento al momento disponibile")
        input("Premi invio per continuare")
    elif role == UserRole.VEND:
        print("Sei un venditore")
        print("Nessun evento al momento disponibile")
    elif role == UserRole.CLIENTE:
        print("Sei un cliente")