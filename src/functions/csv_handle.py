import os
import pandas as pd
import uuid
from functions.file_handle import extract_datetime_from_infos, extract_infos, is_image, list_files
from functions.folder_handle import list_folders
from pathlib import Path


def save_to_csv(path_file: Path, listing):
    df = pd.DataFrame(listing, columns = ['folder', 'file', 'datetime'])
    df.to_csv(path_file, index = False)


def split_csv_files(base_path: str, batch: str):
    folders = list_folders(base_path)
    for folder in folders:
        input_file = Path(base_path) / folder / 'listing.csv'
        df = pd.read_csv(input_file)
        if 'date' in df.columns:
            dates = df['date'].unique()
            for date in dates:
                file_name = uuid.uuid4()
                output_folder = Path(base_path) / '../photos' / str(batch) / str(date)
                output_folder.mkdir(parents = True, exist_ok = True)
                output_file = output_folder / f'{file_name}.csv'
                df_filtered = df[df['date'] == date]
                df_filtered.to_csv(output_file, index = False)


def merge_csv_files(base_path: str):
    folders = list_folders(base_path)
    for folder in folders:
        path = Path(base_path) / folder
        files = list_files(path, '.csv')
        df = pd.concat([pd.read_csv(path / file) for file in files])
        output_file = path / 'merged.csv'
        df.to_csv(output_file, index = False)


def generate_filename(base_path: str):
    folders = list_folders(base_path)
    for folder in folders:
        input_file = Path(base_path) / folder / 'listing.csv'
        df = pd.read_csv(input_file)
        df["datetime"] = pd.to_datetime(df["datetime"])
        df["date"] = df["datetime"].dt.date
        df["uuid"] = [f"{str(uuid.uuid4())}{os.path.splitext(file)[1].lower()}" for file in df["file"]]
        df.to_csv(input_file, index = False)


def generate_csv( base_path: str ):
    folders = list_folders(base_path)
    for folder in folders:
        path_folder = f'{base_path}/{folder}'
        listing = []
        files = list_files(path_folder)
        for file in files:
            path_file = f'{base_path}/{folder}/{file}'
            if is_image(path_file) is True:
                infos = extract_infos(path_file)
                datetime = extract_datetime_from_infos(infos)
                listing.append([folder, file, datetime])
        df = pd.DataFrame(listing, columns=['folder', 'file', 'datetime'])
        df.to_csv(path_folder + '/listing.csv', index=False)
