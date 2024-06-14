from abc import ABC

class BaseStorage(ABC):
    _create = None
    _update = None
    _read = None
    _delete = None

    def create(self):
        if self._create:
            self._create()

    def update(self):
            if self._update:
                self._update()

    def read(self):
        if self._read:
            self._read()

    def delete(self):
        if self._delete:
            self._delete()
