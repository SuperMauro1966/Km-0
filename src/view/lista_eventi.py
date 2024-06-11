from controller.user import ottieni_ruolo
from controller.user_role import UserRole

def eventi():
    role = ottieni_ruolo()
    if role == UserRole.ADMIN:
        print("Sei un admin")
        print("Nessun evento al momento disponibile")
        input("Premi invio per continuare")
    elif role == UserRole.VEND:
        print("Sei un venditore")
        print("Nessun evento al momento disponibile")
        input("Premi invio per continuare")
    elif role == UserRole.CLIENTE:
        print("Sei un cliente")
        print("Nessun evento al momento disponibile")
        input("Premi invio per continuare")