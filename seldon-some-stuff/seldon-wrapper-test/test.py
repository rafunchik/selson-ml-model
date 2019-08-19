import pickle

import numpy as np
import torch

fname = "implicit.pickle"

with open(fname, 'rb') as fle:
     loaded_model = pickle.load(fle)
user_ids = np.array([106])

item_ids = np.array([176180, 176180, 172472])

some_predictions = loaded_model.predict(user_ids, item_ids)
print(some_predictions)

