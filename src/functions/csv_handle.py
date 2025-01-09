import os
import uuid

import pandas as pd

from src.functions.file_handle import is_image, list_files
from src.functions.folder_handle import list_folders
from src.functions.img_handle import extract_datetime_from_infos, extract_infos


def generate_csv(path: str):
    folders = list_folders(path)
    for folder in folders:
        path_folder = f'{path}/{folder}'
        listing = []
        files = list_files(folder)
        for file in files:
            path_file = f'{path}/{folder}/{file}'
            if is_image(path_file) is True:
                infos = extract_infos(folder, file)
                datetime = extract_datetime_from_infos(infos)
                listing.append([folder, file, datetime])
        df = pd.DataFrame(listing, columns = ['folder', 'file', 'datetime'])
        df.to_csv(path_folder + '/listing.csv', index = False)


def split_csv(path: str, batch: str):
    folders = list_folders(path)
    for folder in folders:
        df = pd.read_csv(f'{path}/totreat/{folder}/listing.csv')
        if 'date' in df.columns:
            dates = df['date'].unique()

            for date in dates:
                file_name = uuid.uuid4()
                output_file = f'{path}/photos/{batch}/{date}/{file_name}.csv'
                df_filtered = df[df['date'] == date]
                df_filtered.to_csv(output_file, index = False)


def merge_csv(path: str):
    folders = list_folders(path)
    for folder in folders:
        path = f'{path}/{folder}'
        files = list_files(path, '.csv')
        df = pd.concat([pd.read_csv(f'{path}/{file}') for file in files])
        df.to_csv(f'{path}/merged.csv', index = False)


def generate_filename():
    base = '../artefacts/totreat'
    folders = list_folders(base)
    for folder in folders:
        path = f'{base}/{folder}/listing.csv'
        df = pd.read_csv(path)
        df["datetime"] = pd.to_datetime(df["datetime"])
        df["date"] = df["datetime"].dt.date
        df["uuid"] = [f"{uuid.uuid4()}{os.path.splitext(file)[1].lower()}" for file in df["file"]]
        df.to_csv(path, index = False)
