import json
import numpy as np

binder_length = 460
with open("IIL37D73kisoformBboundIL37D73kisoformB_6ba5f_scores_rank_001_alphafold2_multimer_v3_model_2_seed_000.json", "r") as f:
    data = json.load(f)
pae = np.array([data])

upper = pae[:binder_length,binder_length:].reshape(-1)
lower = pae[binder_length:,:binder_length].reshape(-1)

#print(upper, lower)

pae_i = np.mean(np.concatenate([upper,lower]))
print(pae_i)

