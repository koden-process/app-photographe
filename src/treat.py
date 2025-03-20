import os
import sys
import uuid

from functions.csv_handle import generate_csv, generate_filename, merge_csv_files, split_csv_files
from functions.file_handle import create_json_file, move_files
from functions.folder_handle import checkandcreate_folder
from functions.img_handle import create_thumbs
from functions.misc import list_move_files, sorting
from functions.product_handle import ProductProcessor

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

bucket = 'gs://photos-seb'
batch = uuid.uuid4()
path_totreat = '../artefacts/totreat'
path_photos = f'../artefacts/photos/{batch}'
path_minitatures = f'../artefacts/miniatures/{batch}/'  # avec le slash final !
path_products = f'../artefacts/products/{batch}'
prefixe = 'https://storage.googleapis.com/photos-seb'

generate_csv(path_totreat)
generate_filename(path_totreat)
listing = list_move_files(path_totreat, batch)
move_files(listing)
split_csv_files(path_totreat, batch)
merge_csv_files(path_photos)
sorting(path_photos)
create_thumbs(path_photos)
upload_to_bucket(path_minitatures, bucket)
processor = ProductProcessor(path=path_photos, prefixe=prefixe)
result = processor.process_folders()
checkandcreate_folder(path_products)
create_json_file(f'{path_products}/product.json', result)
