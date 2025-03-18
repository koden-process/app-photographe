import os


def list_folders(path: str) -> list:
    dossiers = os.listdir(path)
    dossiers = [dossier for dossier in dossiers if not dossier.startswith('.')]
    return dossiers


def checkandcreate_folder( dest_path: str ):
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)
