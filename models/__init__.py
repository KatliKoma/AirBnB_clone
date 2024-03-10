#!/usr/bin/python3
"""Initialize the storage for models directory"""
from models.engine.file_storage import FileStorage


storage_instance = FileStorage()
storage_instance.reload()

