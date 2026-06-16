class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        var dict = [Int:Int]()
        for i in 0..<nums.count {
            let val = target - nums[i]
            print(val)
            if let index = dict[val] {
                return [index, i]
            }
            dict[nums[i]] = i
        }
        return []
    }
}
