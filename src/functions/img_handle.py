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
