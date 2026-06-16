class Solution {
    func lengthOfLastWord(_ s: String) -> Int {
        guard s.count > 1 else { return 1 }
        let chars = Array(s)
        var end = chars.count - 1
        var length = 0
        var space = 0
        while end >= 0 {
            if chars[end] == " " {
                if length > 0 {
                    return length
                }
            } else {
                length += 1
            }
            end = end - 1
        }
            return 0
    }
}
