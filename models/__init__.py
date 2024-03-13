#!/usr/bin/python3
import models
from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
