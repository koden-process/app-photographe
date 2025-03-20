import os
import shutil
from datetime import datetime
from exif import Image


def list_files(folder: str, filetype: str = '') -> list:
    files = os.listdir(f'{folder}')
    files = [file for file in files if not file.startswith('.')]
    if filetype is not None:
        files = [file for file in files if file.endswith(filetype)]
    return files


def is_image(filename: str) -> bool:
    result = False

    if filename.endswith('.JPG'):
        result = True

    if filename.endswith('.jpg'):
        result = True

    return result


def move_files(listing: list):
    for row in listing:
        old_path, filename, new_path, new_filename = row
        if not os.path.exists(new_path):
            os.makedirs(new_path)
        shutil.copy(f'{old_path}/{filename}', f'{new_path}/{new_filename}')


def extract_infos( path_file: str ) -> dict:
    with open(path_file, "rb") as img_file:
        img = Image(img_file)
        if img.has_exif:
            return img


def extract_datetime_from_infos( infos: dict ) -> str:
    if infos.has_exif and hasattr(infos, "datetime"):
        date_time = datetime.strptime(infos.datetime, "%Y:%m:%d %H:%M:%S")
        return date_time


def upload_to_bucket( path_file: str, bucket_name: str ):
    if not os.path.exists(path_file):
        print(f"Erreur : {path_file} n'existe pas.")
        return

    command = f'gsutil -m rsync -r "{path_file}" "{bucket_name}"'
    print(f"Exécution de la commande : {command}")
    os.system(command)
