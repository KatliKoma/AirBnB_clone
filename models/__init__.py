#!/usr/bin/python3
"""
module executes when models package is imported
"""


from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
