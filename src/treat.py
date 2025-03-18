import os
import sys
import uuid

from functions.csv_handle import generate_csv, generate_filename, merge_csv_files, split_csv_files
from functions.file_handle import move_files
from functions.img_handle import create_thumbs
from functions.misc import list_move_files, sorting

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

batch = uuid.uuid4()
path_totreat = '../artefacts/totreat'
path_photos = f'../artefacts/photos/{batch}'

generate_csv(path_totreat)
generate_filename(path_totreat)
listing = list_move_files(path_totreat, batch)
move_files(listing)
split_csv_files(path_totreat, batch)
merge_csv_files(path_photos)
sorting(path_photos)
create_thumbs(path_photos)
