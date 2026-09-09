class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        innerL, innerR = 0, len(matrix[0]) - 1
        while l <= r:
            targetMid = (l + r) // 2
            if matrix[targetMid][0] > target:
                r = targetMid - 1
            elif matrix[targetMid][innerR] < target:
                l = targetMid + 1
            else:
                break
        while innerL <= innerR:
            mid = (innerL + innerR) // 2
            if matrix[targetMid][mid] < target:
                innerL = mid + 1
            elif matrix[targetMid][mid] > target:
                innerR = mid - 1
            else:
                return True
        return False
