import os


def list_folders(path) -> list:
	dossiers = os.listdir(path)
	dossiers = [dossier for dossier in dossiers if not dossier.startswith('.')]
	return dossiers

def list_files(folder:str, filetype = '') -> list:
	files = os.listdir(f'{folder}')
	files = [file for file in files if not file.startswith('.')]
	if filetype is not None:
		files = [file for file in files if file.endswith(filetype)]
	return files