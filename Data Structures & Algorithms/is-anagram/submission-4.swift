class Solution {
    func isAnagram(_ s: String, _ t: String) -> Bool {

        guard s.count == t.count else {
            return false
        }

        var first = [Character: Int]()
        var second = [Character: Int]()

        for c in s {
            if let count = first[c] {
                first[c] = count + 1
            } else {
                first[c] = 1
            }
        }

        for c in t {
            if let count = second[c] {
                second[c] = count + 1
            } else {
                second[c] = 1
            }
        }

        for (key, count) in first {
            guard let sCount = second[key]  else {
                return false
            }
            if count != sCount {
                return false
            }
        }
        
        return true
    }
}
