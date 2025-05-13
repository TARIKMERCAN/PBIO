# =============================================================================
# PROGRAM: FASTA DNA Sequence Generator with Statistics and Name Embedding
# CONTEXT: University bioinformatics assignment using LLM-generated starter code
# PURPOSE: Generates a random DNA sequence of user-defined length using A, C, G, T.
#          User's name is inserted at a random position. Sequence is saved in
#          FASTA format with correct wrapping. Statistics of the DNA
#          are also displayed.
# AUTHOR: s24127
# =============================================================================

import random

# === CONSTANTS ===
VALID_NUCLEOTIDES = ['A', 'T', 'C', 'G']
LINE_WIDTH = 60

# === USER INPUT ===

# ORIGINAL:
# length = int(input("Enter the sequence length: "))

# MODIFIED (added loop and validation for proper numeric and positive input)
while True:
    try:
        length = int(input("Enter the sequence length: "))
        if length > 0:
            break
        else:
            print("Length must be a positive integer.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# ORIGINAL:
# seq_id = input("Enter the sequence ID: ")

# MODIFIED (added sanitization to make filename safe)
seq_id = input("Enter the sequence ID: ").strip()
for ch in ['<', '>', ':', '"', '/', '\\', '|', '?', '*', ' ']:
    seq_id = seq_id.replace(ch, '_')

# ORIGINAL:
# description = input("Provide a description of the sequence: ")

# MODIFIED (added retry loop and non-empty check)
while True:
    description = input("Provide a description of the sequence: ").strip()
    if description:
        break
    else:
        print("Description cannot be empty.")

# ORIGINAL:
# name = input("Enter your name: ")

# MODIFIED (added .strip to clean whitespace)
name = input("Enter your name: ").strip()

# === DNA SEQUENCE GENERATION ===

# ORIGINAL:
# sequence = ''.join(random.choices("ACGT", k=length))

# MODIFIED (used constant list for better flexibility)
sequence = ''.join(random.choices(VALID_NUCLEOTIDES, k=length))

# ORIGINAL:
# insert_pos = random.randint(0, length)
# sequence_with_name = sequence[:insert_pos] + name + sequence[insert_pos:]

# MODIFIED (same logic but wrapped in function for modularity)
def embed_name_in_sequence(dna, name):
    index = random.randint(0, len(dna))
    return dna[:index] + name + dna[index:]

sequence_with_name = embed_name_in_sequence(sequence, name)

# === WRITE TO FASTA FILE ===

# ORIGINAL:
# with open(filename, 'w') as f:
#     f.write(f">{seq_id} {description}\n")
#     f.write(sequence_with_name + "\n")

# MODIFIED (added line wrapping and consistent formatting)
def write_fasta(filename, header, sequence):
    with open(filename, 'w') as f:
        f.write(header + "\n")
        for i in range(0, len(sequence), LINE_WIDTH):
            f.write(sequence[i:i+LINE_WIDTH] + "\n")

fasta_filename = f"{seq_id}.fasta"
fasta_header = f">{seq_id} {description}"
write_fasta(fasta_filename, fasta_header, sequence_with_name)

# === DNA STATISTICS  ===

# ORIGINAL:
# A = sequence.count('A')
# C = sequence.count('C')
# G = sequence.count('G')
# T = sequence.count('T')
# cg_ratio = (C + G) / (A + T)

# MODIFIED (used dictionary for cleaner structure and reuse)
def calculate_statistics(dna):
    stats = {n: dna.count(n) for n in VALID_NUCLEOTIDES}
    total = sum(stats.values())
    percentages = {k: (v / total) * 100 for k, v in stats.items()}
    cg_ratio = (stats['C'] + stats['G']) / total * 100
    return percentages, cg_ratio

percentages, cg_ratio = calculate_statistics(sequence)

# === DISPLAY RESULTS ===

# ORIGINAL:
# print("Statistics...")

# MODIFIED (more readable formatting)
print(f"\nThe sequence was saved to the file {fasta_filename}")
print("Sequence statistics:")
for base in VALID_NUCLEOTIDES:
    print(f"{base}: {percentages[base]:.1f}%")
print(f"%CG: {cg_ratio:.1f}")
