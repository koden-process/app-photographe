import os
import uuid
from pathlib import Path

import pandas as pd

from src.functions.file_handle import list_files
from src.functions.folder_handle import list_folders


def save_to_csv(path_file: Path, listing):
    df = pd.DataFrame(listing, columns = ['folder', 'file', 'datetime'])
    df.to_csv(path_file, index = False)


def split_csv_files(base_path: str, batch: str):
    folders = list_folders(base_path)
    for folder in folders:
        input_file = Path(base_path) / 'totreat' / folder / 'listing.csv'
        df = pd.read_csv(input_file)
        if 'date' in df.columns:
            dates = df['date'].unique()
            for date in dates:
                file_name = uuid.uuid4()
                output_folder = Path(base_path) / 'photos' / batch / str(date)
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
