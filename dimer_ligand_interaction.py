# This is a special case of n = 3 from the n_peptides.py. In general, use that rather.
import numpy as np

# Assume these are your lengths (from token_chain_ids or sequence)
chain_lengths = [430, 518, 573]  # A, B, C
chain_labels = ['A', 'B', 'C']   # Consistent with token_chain_ids
chain_roles = ['receptor', 'dimer', 'receptor']

# Compute boundaries
chain_boundaries = []
start = 0
for length in chain_lengths:
    chain_boundaries.append((start, start + length))
    start += length

# Assume you have full PAE matrix from AF3
pae = np.array([])  # or from AlphaFold JSON

# Collect only dimer <> receptor interactions
interface_pae_values = []

for i in range(len(chain_labels)):
    for j in range(i+1, len(chain_labels)):
        if i == j:
            continue  # skip intra-chain
        if chain_roles[i] == 'receptor' and chain_roles[j] == 'receptor':
            continue  # skip receptor–receptor interaction

        start_i, end_i = chain_boundaries[i]
        start_j, end_j = chain_boundaries[j]

        upper = pae[start_i:end_i, start_j:end_j].reshape(-1)
        lower = pae[start_j:end_j, start_i:end_i].reshape(-1)

        interface_pae_values.extend(upper)
        interface_pae_values.extend(lower)

# Final cumulative mean
pae_i = np.mean(interface_pae_values)
print(f"Filtered interface PAE (dimer-receptor only): {pae_i:.2f}")
