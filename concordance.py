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
av = vector(ZZ, a_len, a_len * [a_len])

# Place the column vector on the left of the trimmed Toeplitz matrix
m_aug = matrix(av).transpose().augment(trimmed_toep)
# Apply a circular permutation (a circular shift) by matmul by a basic circulant permutation matrix
# 9 zeroes, 1 one, then 25 more zeroes, which gives a circular permutation of "plus 8" (I think?)
# which is what is seen in the ptx output: it is a "forward shift" eight positions so that the whitespace
# after the alphabet wraps back around to be before the A on the top row, and then a further 8
# shifts so that the whitespace is centred, and the context behind it (up to the letter Z) on the top
# are "pulled back in" across the leftmost edge behind the whitespace)
cv = vector(ZZ, [0] * (2 * ext + 1) + [1] + [0] * (a_len - ext - 1))
m_perm = matrix.circulant(cv)
conc = m_aug * m_perm

# Add a column to the matrix, which will become the space in the middle

if __name__ == "__main__":
    for r in matrix_to_alpha(conc):
        print(" ".join(r))
