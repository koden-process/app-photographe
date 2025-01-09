import os
import shutil


def list_files(folder: str, filetype: str = '') -> list:
	files = os.listdir(f'{folder}')
	files = [file for file in files if not file.startswith('.')]
	if filetype is not None:
		files = [file for file in files if file.endswith(filetype)]
	return files


def is_image(filename: str) -> bool:
	result = False

	if filename.endswith('.JPG'):
		result = True

	if filename.endswith('.jpg'):
		result = True

	return result


def move_files(listing: list):
	for row in listing:
		old_path, filename, new_path, new_filename = row
		if not os.path.exists(new_path):
			os.makedirs(new_path)
		shutil.copy(f'{old_path}/{filename}', f'{new_path}/{new_filename}')
