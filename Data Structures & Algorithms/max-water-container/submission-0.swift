class Solution {
    func maxArea(_ heights: [Int]) -> Int {
        var result = 0
        var l = 0
        var r = heights.count - 1
        while l < r {
            let area = (r - l) * min(heights[l], heights[r])
            result = max(result, area)
            if (heights[l] < heights[r]) {
                l += 1
            } else {
                r -= 1
            }
        }
        return result
    }
}
