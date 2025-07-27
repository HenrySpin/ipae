import numpy as np

# Example PAE matrix for 3 chains with lengths [430, 430, 518]
chain_lengths = [430, 430, 518]
total_length = sum(chain_lengths)

# Input the PAE matrix for testing (values 0–30 Å)
pae = np.array([])

# Compute chain boundaries
chain_boundaries = []
start = 0
for L in chain_lengths:
    chain_boundaries.append((start, start + L))
    start += L

# Collect all inter-chain PAE blocks
all_interface_values = []

for i in range(len(chain_boundaries)):
    for j in range(i+1, len(chain_boundaries)):
        if i == j:
            continue  # skip intra-chain

        start_i, end_i = chain_boundaries[i]
        start_j, end_j = chain_boundaries[j]

        # Extract and flatten both directions: i->j and j->i
        upper = pae[start_i:end_i, start_j:end_j].reshape(-1)
        lower = pae[start_j:end_j, start_i:end_i].reshape(-1)

        all_interface_values.extend(upper)
        all_interface_values.extend(lower)

# Compute the mean of all inter-chain PAE values
pae_i = np.mean(all_interface_values)
print(f"Cumulative interface PAE (pae_i) across {len(chain_lengths)} chains: {pae_i:.2f}")
