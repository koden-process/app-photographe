from functions.file_handle import create_json_file
from functions.folder_handle import checkandcreate_folder
from functions.product_handle import ProductProcessor

batch = '8209f2a0-892a-407e-bde6-497213b3b1ef'
path_photos = f'../artefacts/photos/{batch}'
path_products = f'../artefacts/products/{batch}'
prefixe = 'https://storage.googleapis.com/photos-seb'

processor = ProductProcessor(path=path_photos, prefixe=prefixe)
result = processor.process_folders()
checkandcreate_folder(path_products)
create_json_file(f'{path_products}/product.json', result)
