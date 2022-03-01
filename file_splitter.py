# this script copies randomnized images into the output folder in the desired train/val/test split ratio
# for further instructions and documentation see https://pypi.org/project/split-folders/

import splitfolders
splitfolders.ratio('../classifying_illuminated_charters/data/collect_recto_verso', output="../classifying_illuminated_charters/data/train_recto_verso", seed=1337, ratio=(.8, 0.1,0.1)) 