class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        # for i in range(len(heights)):
        #     for j in range(i + 1, len(heights)):
        #         width = abs(i - j)
        #         height = min(heights[i], heights[j])
        #         area = max(area, width * height)
        # return area

        l, r = 0, len(heights) - 1
        res = 0
        while l < r:
            res = max(res, (r - l) * min(heights[l], heights[r]))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return res


        