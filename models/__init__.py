# models/__init__.py
import models
from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

