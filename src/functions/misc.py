import pandas as pd

from functions.folder_handle import list_folders


def list_move_files(path, batch):
    listing = []
    folders = list_folders(path)
    for folder in folders:
        path_csv = f'{path}/{folder}/listing.csv'
        df = pd.read_csv(path_csv)
        for row in df.itertuples(index = False):
            filename = row.file
            new_folder = row.date
            new_filename = row.uuid
            old_path = f'{path}/{folder}'
            new_path = f'../artefacts/photos/{batch}/{new_folder}'
            listing.append([old_path, filename, new_path, new_filename])
    return listing


def sorting( path ):
    time_threshold = 15

    folders = list_folders(path)
    for folder in folders:
        file_path = f'{path}/{folder}/merged.csv'
        done_path = f'{path}/{folder}/done.csv'

        df = pd.read_csv(file_path)
        df['datetime'] = pd.to_datetime(df['datetime'])
        df = df.sort_values(by='datetime')
        df['time_diff'] = df['datetime'].diff().dt.total_seconds()
        df['folder'] = (df['time_diff'] > time_threshold).cumsum()
        df = df.drop(columns=['time_diff'])
        df.to_csv(done_path, index=False)
