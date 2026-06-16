class Solution {
    func hasDuplicate(_ nums: [Int]) -> Bool {
        var dup = Set<Int>()
        for i in nums {
            if dup.contains(i) {
                return true
            } 
             dup.insert(i)
        }
        return false
    }
}
