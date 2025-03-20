from functions.file_handle import upload_to_bucket

batch = '8209f2a0-892a-407e-bde6-497213b3b1ef'
path_minitatures = f'../artefacts/miniatures/{batch}/'
bucket = 'gs://photos-seb'

# https://storage.googleapis.com/photos-seb/

upload_to_bucket(path_minitatures, bucket)
