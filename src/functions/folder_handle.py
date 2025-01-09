import os


def list_folders(path: str) -> list:
    dossiers = os.listdir(path)
    dossiers = [dossier for dossier in dossiers if not dossier.startswith('.')]
    return dossiers
