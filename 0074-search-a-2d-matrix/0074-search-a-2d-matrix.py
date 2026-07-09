class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if matrix[i][0]<=target<=matrix[i][-1]:
                for j in range(len(matrix[i])):
                    if matrix[i][j]==target:
                        return True
            if matrix[i][0]>target:
                break
        return False