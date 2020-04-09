from string import ascii_uppercase as a
from matrix_edits import matrix_to_alpha

a_len = len(a)  # length of alphabet: 26
ext = 8  # number of spaces: ptx uses 8

# First column in reverse alphabetical order, will be reversed back later
c = list(reversed(range(a_len + ext)))
r = list(range(a_len + ext - 1))

# Make a Toeplitz matrix then flip u.d. so its first column is ascending
# rather than descending. Trim off the bottom of this matrix by taking
# only the first 26 columns (so the first column is the alphabet, A-Z)
trimmed_toep = matrix.toeplitz(c, r)[::-1][:a_len]

if __name__ == "__main__":
    for r in matrix_to_alpha(trimmed_toep):
        print(" ".join(r))
