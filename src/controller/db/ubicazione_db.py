from controller.models.ubicazione import Ubicazione
from base_storage import BaseStorage

def _crea(ubicazione: Ubicazione):
    pass

def _aggiorna(ubicazione: Ubicazione):
    pass

def _leggi(ubicazione: Ubicazione):
    pass

def _elimina(ubicazione: Ubicazione):
    pass

class UbicazioneDB(BaseStorage, Ubicazione):
    _create = _crea
    _update = _aggiorna
    _read  = _leggi
    _delete = _elimina