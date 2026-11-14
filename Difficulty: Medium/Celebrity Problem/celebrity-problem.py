class Solution:
    def celebrity(self, mat):
        n = len(mat)

        # Start with person 0 as the possible celebrity
        candidate = 0

        # Find the only possible candidate
        for i in range(1, n):
            if mat[candidate][i] == 1:
                # Candidate knows i, so candidate cannot be celebrity
                candidate = i

        # Verify the candidate
        for i in range(n):
            if i != candidate:
                # Celebrity must not know anyone
                if mat[candidate][i] == 1:
                    return -1

                # Everyone must know the celebrity
                if mat[i][candidate] == 0:
                    return -1

        return candidate