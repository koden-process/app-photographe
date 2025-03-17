import os
import sys
import uuid

from functions.csv_handle import generate_csv, generate_filename, merge_csv_files, split_csv_files
from functions.file_handle import move_files
from functions.misc import list_move_files

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

path = '../artefacts/totreat'
batch = uuid.uuid4()

generate_csv(path)
generate_filename(path)
listing = list_move_files(path, batch)
move_files(listing)
split_csv_files(path, batch)

path = f'../artefacts/photos/{batch}'
merge_csv_files(path)
