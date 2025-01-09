import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

path = '../artefacts/totreat'
batch = uuid.uuid4()

generate_csv(path)
generate_filename()

path = '../artefacts/totreat'
listing = list_move_files(path, batch)
move_files(listing)

path = '../artefacts'
split_csv(path, batch)

path = f'../artefacts/photos/{batch}'
merge_csv(path, batch)
