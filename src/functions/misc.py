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
