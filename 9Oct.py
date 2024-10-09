class Solution:
    def constructLinkedMatrix(self, mat):
        m = len(mat)
        n = len(mat[0])
        nodeMatrix = [[None for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                nodeMatrix[i][j] = Node(mat[i][j])

        for i in range(m):
            for j in range(n):
                if j < n - 1:
                    nodeMatrix[i][j].right = nodeMatrix[i][j + 1]  
                if i < m - 1:
                    nodeMatrix[i][j].down = nodeMatrix[i + 1][j]  

        return nodeMatrix[0][0]
