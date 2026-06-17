class Solution {
    func topKFrequent(_ nums: [Int], _ k: Int) -> [Int] {
        var count = [Int: Int]()
        var freq = Array(repeating: [Int](), count: nums.count + 1)
        var result = [Int]()

        for n in nums {
            count[n, default: 0] += 1
        }
        
        for (key, value) in count {
            freq[value].append(key)
        }

        var i = freq.count - 1
        var counter = 0
        while i > 0  {
            if freq[i].count > 0  {
                for c in freq[i] {
                    result.append(c)
                    if result.count == k {
                        return result
                    }
                }
            }
            i = i - 1
        }

        return result
    }

}