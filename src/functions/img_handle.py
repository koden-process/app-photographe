import os
from PIL import Image
from functions.file_handle import list_files
from functions.folder_handle import checkandcreate_folder, list_folders


def extract_infos(folder: str, file: str) -> dict:
    base = '../artefacts/totreat'
    path = f'{base}/{folder}/{file}'

    with open(path, "rb") as img_file:
        img = Image(img_file)
        if img.has_exif:
            return img


def extract_datetime_from_infos(infos: dict) -> str:
    if infos.has_exif and hasattr(infos, "datetime"):
        date_time = datetime.strptime(infos.datetime, "%Y:%m:%d %H:%M:%S")
        return date_time


def process_images( path_img_src ):
    img_src = Path(path_img_src)
    folders = list_folders(img_src)
    for folder in folders:
        folder_path = Path(base_path) / folder
        listing = []
        files = list_files(folder_path)
        for file in files:
            if is_image(file):
                infos = extract_infos(folder, file)
                datetime = extract_datetime_from_infos(infos)
                listing.append([folder, str(file), datetime])
        save_listing(folder_path, listing)


def create_thumbs( path ):
    folders = list_folders(path)
    for folder in folders:
        date_path = f'{path}/{folder}'

        dest_path = date_path.replace('photos', 'miniatures')
        checkandcreate_folder(dest_path)

        files = list_files(date_path, '.jpg')

        for file in files:
            img = Image.open(f'{date_path}/{file}')
            img.thumbnail((100, 100))
            img.save(f'{dest_path}/{file}')
