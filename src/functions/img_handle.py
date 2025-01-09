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


def process_images(path_img_src: Path):
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
