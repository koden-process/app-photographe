import os
import sys
import uuid

from functions.csv_handle import generate_csv, generate_filename, merge_csv_files, split_csv_files
from functions.file_handle import move_files
from functions.img_handle import create_thumbs
from functions.misc import list_move_files, sorting

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

batch = "8209f2a0-892a-407e-bde6-497213b3b1ef"
path_totreat = '../artefacts/totreat'
path_photos = f'../artefacts/photos/{batch}'

create_thumbs(path_photos)
