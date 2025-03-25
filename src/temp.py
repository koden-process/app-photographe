import os
import sys

from functions.file_handle import create_json_file, upload_to_bucket
from functions.folder_handle import checkandcreate_folder
from functions.product_handle import ProductProcessor

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

bucket = 'gs://photos-seb'
batch = 'c98ac41b-8980-498c-a6b1-5b09c7e39a56'
path_totreat = '../artefacts/totreat'
path_photos = f'../artefacts/photos/{batch}'
path_minitatures = f'../artefacts/miniatures/{batch}/'  # avec le slash final !
path_products = f'../artefacts/products/{batch}'
prefixe = 'https://storage.googleapis.com/photos-seb'

upload_to_bucket(path_minitatures, bucket)
processor = ProductProcessor(path=path_photos, prefixe=prefixe)
result = processor.process_folders()
checkandcreate_folder(path_products)
create_json_file(f'{path_products}/product.json', result)
