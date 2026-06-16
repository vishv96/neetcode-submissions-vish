class Solution {
    func lengthOfLastWord(_ s: String) -> Int {
        let words = s.split(separator:" ")
        if let lastWorld = words.last {
            return lastWorld.count
        }
        return 0
    }
}
